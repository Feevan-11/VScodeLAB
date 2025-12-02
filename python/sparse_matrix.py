import numpy as np
import struct
import random
from typing import Tuple, List

class SparseMatrixCompressor:
    def __init__(self):
        # 计算粒度（每次处理32行）
        self.granularity = 16
        
    def generate_random_matrix(self, rows: int, cols: int, sparsity: float) -> np.ndarray:
        """生成随机稀疏矩阵（直接使用FP16格式）"""
        # 直接创建FP16格式的矩阵
        matrix = np.zeros((rows, cols), dtype=np.float16)
        
        # 根据稀疏度生成非零元素
        nnz_total = int(rows * cols * (1 - sparsity))
        indices = np.random.choice(rows * cols, nnz_total, replace=False)
        
        # 生成FP16格式的随机值
        values = np.random.uniform(-1.0, 1.0, nnz_total).astype(np.float16)
            
        # 填充非零元素
        for idx in indices:
            i, j = idx // cols, idx % cols
            matrix[i, j] = values[idx % nnz_total]
            
        return matrix
    
    def compress_matrix(self, matrix: np.ndarray, is_matrix_b: bool = False) -> List[bytes]:
        """压缩稀疏矩阵为数据包格式"""
        rows, cols = matrix.shape
        
        packets = []
        
        # 按32行分块处理
        for row_start in range(0, rows, self.granularity):
            row_end = min(row_start + self.granularity, rows)
            current_rows = row_end - row_start
            
            # 处理当前块
            packet_data = bytearray()
            
            # 收集当前块的所有非零元素信息
            all_nnz_info = []
            total_nnz = 0
            
            for i in range(row_start, row_end):
                row_data = matrix[i]
                nnz_indices = np.where(row_data != 0)[0]
                nnz_count = len(nnz_indices)
                
                if nnz_count > 0:
                    all_nnz_info.append({
                        'row_idx': i,
                        'nnz_count': nnz_count,
                        'col_indices': nnz_indices,
                        'values': [row_data[j] for j in nnz_indices]
                    })
                    total_nnz += nnz_count
            
            # 检查是否包含最后一列
            contains_last_col = False
            for info in all_nnz_info:
                if (cols - 1) in info['col_indices']:
                    contains_last_col = True
                    break
            
            # 构建包头（固定512位）
            header = self._build_header(row_end == rows, 
                                      contains_last_col, 
                                      cols, total_nnz)
            packet_data.extend(header)
            
            # 构建行向量信息（固定16行，不足补零）
            row_vector_size = 16 * 4  # 16行 × 4字节
            row_vector_data = bytearray(row_vector_size)
            
            for idx, info in enumerate(all_nnz_info[:16]):  # 最多16行
                # 行索引（2字节）- 使用自然顺序（小端序）
                struct.pack_into('<H', row_vector_data, idx*4, info['row_idx'])
                # 行非零值数量（2字节）- 使用自然顺序（小端序）
                struct.pack_into('<H', row_vector_data, idx*4 + 2, info['nnz_count'])
            
            packet_data.extend(row_vector_data)
            
            # 构建列掩码
            col_mask_data = bytearray()
            mask_count = (cols + 15) // 16
            for info in all_nnz_info[:16]:  # 对应行向量中的行
                # 每行需要mask_count个列掩码
                for mask_idx in range(mask_count):
                    mask_value = 0
                    start_col = mask_idx * 16
                    for col_idx in info['col_indices']:
                        if start_col <= col_idx < start_col + 16:
                            bit_pos = col_idx - start_col
                            mask_value |= (1 << bit_pos)
                    
                    # 使用自然顺序（小端序）
                    col_mask_data.extend(struct.pack('<H', mask_value))
            
            packet_data.extend(col_mask_data)
            
            # 构建非零值序列（FP16）
            value_data = bytearray()
            for info in all_nnz_info[:16]:
                for val in info['values']:
                    # FP16转换 - 使用自然顺序（小端序）
                    value_data.extend(struct.pack('<e', val))
            
            packet_data.extend(value_data)
            
            packets.append(bytes(packet_data))
        
        return packets
    
    def _build_header(self, rlast: bool, clast: bool, 
                     total_cols: int, nnz_count: int) -> bytes:
        """构建包头（固定512位=64字节），右侧补零"""
        # 创建64字节的包头，初始全为零
        header = bytearray(64)  # 64字节 = 512位
        
        # 包头结构（前5字节为有效数据，右侧补零）：
        # 字节0: 类型(2bit) + RLast(1bit) + CLast(1bit) + 列掩码高4bit
        # 字节1: 列掩码低8bit
        # 字节2-3: 值数量(16bit)
        # 字节4: 保留
        
        # 第一个字节：类型(2bit)=0（FP16） + RLast(1bit) + CLast(1bit) + 列掩码高4bit
        first_byte = 0  # FP16类型
        first_byte |= (1 if rlast else 0) << 5
        first_byte |= (1 if clast else 0) << 4
        first_byte |= (total_cols >> 8) & 0x0F
        
        # 在右侧补零（低位地址），所以有效数据放在最前面的5字节
        # 小端序：低地址存放低位字节，符合常规的数据排列
        
        # 有效数据位置（前5字节）
        header[0] = first_byte           # 字节0的有效数据
        header[1] = total_cols & 0xFF   # 字节1的有效数据
        header[2] = (nnz_count >> 8) & 0xFF  # 字节2的有效数据
        header[3] = nnz_count & 0xFF        # 字节3的有效数据
        header[4] = 0                       # 字节4的保留位
        
        # 第5-63字节自动保持为0（右侧补零）
        
        return bytes(header)
    
    def pad_to_512bits(self, data: bytes) -> List[str]:
        """将数据填充到512位（64字节）的倍数，右侧补零，并转换为二进制字符串列表"""
        # 计算需要填充的字节数
        total_bytes = len(data)
        target_bytes = ((total_bytes + 63) // 64) * 64  # 64字节对齐
        pad_bytes = target_bytes - total_bytes
        
        # 在数据右侧补零（低位地址方向）
        padded_data = data + b'\x00' * pad_bytes
        
        # 转换为二进制字符串列表
        binary_lines = []
        
        # 按64字节（512位）分块
        chunk_count = len(padded_data) // 64
        for i in range(chunk_count):
            chunk = padded_data[i*64:(i+1)*64]
            
            # 对每个64字节块，反转字节顺序
            reversed_chunk = bytes(reversed(chunk))
            
            # 转换为二进制字符串
            binary_str = ''
            for byte in reversed_chunk:
                binary_str += format(byte, '08b')
            
            binary_lines.append(binary_str)
        
        return binary_lines
    
    def write_packets_to_file(self, packets: List[bytes], filename: str):
        """将数据包写入文件，每行512位"""
        with open(filename, 'w') as f:
            for packet in packets:
                binary_lines = self.pad_to_512bits(packet)
                
                # 写入所有行
                for line in binary_lines:
                    f.write(line + '\n')

def main(matrix_size = 64,sparsity = 0.9 ):
    compressor = SparseMatrixCompressor()

    # 矩阵参数

    matrix_size = matrix_size  
    sparsity = sparsity    # 90%稀疏度
    
    print("生成随机稀疏矩阵...")
    # 生成矩阵A和B（直接使用FP16格式）
    matrix_a = compressor.generate_random_matrix(matrix_size, matrix_size, sparsity)
    matrix_b = compressor.generate_random_matrix(matrix_size, matrix_size, sparsity)
    
    print(f"矩阵A非零元素: {np.count_nonzero(matrix_a)}")
    print(f"矩阵B非零元素: {np.count_nonzero(matrix_b)}")
    print(f"矩阵A数据类型: {matrix_a.dtype}")
    print(f"矩阵B数据类型: {matrix_b.dtype}")
    
    # 压缩矩阵
    print("压缩矩阵A...")
    packets_a = compressor.compress_matrix(matrix_a, is_matrix_b=False)
    
    print("压缩矩阵B...")
    packets_b = compressor.compress_matrix(matrix_b, is_matrix_b=True)
    
    # 写入数据包文件
    print("写入数据包文件...")
    compressor.write_packets_to_file(packets_a, '.\\sparse\\matrix_a_packets.mif')
    compressor.write_packets_to_file(packets_b, '.\\sparse\\matrix_b_packets.mif')
    
    # 计算每个数据包占用的512位块数
    def calculate_512bit_blocks(packets):
        blocks = []
        for packet in packets:
            total_bytes = len(packet)
            blocks_required = (total_bytes + 63) // 64  # 64字节=512位
            blocks.append(blocks_required)
        return blocks
    
    a_blocks = calculate_512bit_blocks(packets_a)
    b_blocks = calculate_512bit_blocks(packets_b)
    
    # 写入块信息文件
    with open('.\\sparse\\packet_blocks_info.txt', 'w') as f:
        # 矩阵A的数据包块信息
        f.write(' '.join(map(str, a_blocks)) + '\n')
        # 矩阵B的数据包块信息  
        f.write(' '.join(map(str, b_blocks)) + '\n')
    
    print("压缩完成！")
    print(f"矩阵A生成 {len(packets_a)} 个数据包")
    print(f"矩阵B生成 {len(packets_b)} 个数据包")
    print(f"矩阵A数据包块数: {a_blocks}")
    print(f"矩阵B数据包块数: {b_blocks}")
    
    # 显示数据包结构示例
    if len(packets_a) > 0:
        sample_packet = packets_a[0]
        print(f"\n数据包总大小: {len(sample_packet)} 字节")
        print("包头前8字节（十六进制）:", sample_packet[:8].hex())
        print("数据包末尾8字节（十六进制）:", sample_packet[-8:].hex())
        
        # 显示填充后的二进制格式
        binary_lines = compressor.pad_to_512bits(sample_packet)
        if len(binary_lines) > 0:
            print("第一个512位块的前128位:",len(binary_lines))#, binary_lines[471][:511])

if __name__ == "__main__":
    main(matrix_size=64, sparsity=0.9)