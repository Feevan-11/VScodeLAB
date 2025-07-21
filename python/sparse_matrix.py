import numpy as np
import struct
import random

def int_to_bin(value, width):
    """将整数转换为指定位宽的二进制字符串"""
    return bin(value)[2:].zfill(width)

def fp16_to_bin(value):
    """将浮点数转换为16位fp16格式的二进制表示"""
    half = np.float16(value)
    half_bytes = struct.pack('e', half)
    half_int = struct.unpack('H', half_bytes)[0]
    return bin(half_int)[2:].zfill(16)

def chunk_binary(binary_str, max_bits=256):
    """将二进制字符串分割为多行，每行最大max_bits位"""
    chunks = []
    for i in range(0, len(binary_str), max_bits):
        chunk = binary_str[i:i+max_bits]
        chunks.append(chunk)
    return chunks

def generate_sparse_matrix(rows, cols, sparsity):
    """生成随机稀疏矩阵"""
    matrix = np.zeros((rows, cols), dtype=np.float32)
    for i in range(rows):
        for j in range(cols):
            if random.random() < sparsity:
                matrix[i][j] = random.uniform(-10.0, 10.0)
    return matrix

def create_data_packets(matrix, packet_rows=16):
    """将稀疏矩阵打包为二进制数据包"""
    rows, cols = matrix.shape
    packets = []
    
    # 列掩码数量计算
    col_mask_count = (cols + 15) // 16
    
    # 遍历矩阵，每packet_rows行创建一个数据包
    for start_row in range(0, rows, packet_rows):
        end_row = min(start_row + packet_rows, rows)
        actual_rows = end_row - start_row
        
        # 初始化数据包二进制字符串
        packet_binary = ""
        
        # 1. 包头部分 (32位)
        # - 类型 (2bit)：0为fp16
        data_type = 0
        # - RLast (1bit)：是否为行分块最后一个包
        r_last = 1 if end_row == rows else 0
        # - CLast (1bit)：本次计算结束标志
        c_last = 1 if end_row == rows else 0
        # - 列掩码数量 (12bit)
        # - 非零值总数 (16bit)
        
        # 统计非零值并构建行信息
        row_info = []
        nnz_count = 0
        for i in range(start_row, end_row):
            row_nnz = np.count_nonzero(matrix[i])
            row_info.append((i, row_nnz))
            nnz_count += row_nnz
        
        # 填充不足行
        for _ in range(packet_rows - actual_rows):
            row_info.append((0xFFFF, 0))  # 0xFFFF表示无效行
        
        # 构建包头二进制
        header_bin = int_to_bin(data_type, 2)
        header_bin += int_to_bin(r_last, 1)
        header_bin += int_to_bin(c_last, 1)
        header_bin += int_to_bin(col_mask_count, 12)
        header_bin += int_to_bin(nnz_count, 16)
        packet_binary += header_bin
        
        # 2. 行信息部分 (512位 = 16行×32位)
        for (row_idx, row_nnz) in row_info:
            packet_binary += int_to_bin(row_idx, 16)  # 行索引 (16位)
            packet_binary += int_to_bin(row_nnz, 16)  # 行非零值数 (16位)
        
        # 3. 列掩码部分 (每列掩码16位)
        col_masks = [0] * col_mask_count
        for i in range(start_row, end_row):
            for j in range(cols):
                if matrix[i][j] != 0:
                    mask_idx = j // 16
                    bit_pos = j % 16
                    if mask_idx < col_mask_count:  # 防止超出范围
                        col_masks[mask_idx] |= (1 << bit_pos)
        
        # 列掩码转换为二进制
        for mask in col_masks:
            packet_binary += int_to_bin(mask, 16)  # 每个列掩码16位
        
        # 4. 非零值部分 (每个值16位)
        for i in range(start_row, end_row):
            for j in range(cols):
                if matrix[i][j] != 0:
                    packet_binary += fp16_to_bin(matrix[i][j])
        
        # 截断为多行（每行256位）
        packet_chunks = chunk_binary(packet_binary)
        packets.extend(packet_chunks)
    
    return packets

def save_packets_to_file(packets, filename):
    """将数据包保存到文件"""
    with open(filename, 'w') as f:
        for packet in packets:
            f.write(packet + '\n')

if __name__ == "__main__":
    # 参数配置
    OUTPUT_FILE = "sparse_matrix_packets.txt"
    MATRIX_ROWS = 128    # 矩阵行数
    MATRIX_COLS = 128   # 矩阵列数
    SPARSITY = 0.05      # 稀疏度
    PACKET_ROWS = 16     # 每个数据包包含的行数
    
    # 生成随机稀疏矩阵
    print("生成稀疏矩阵...")
    sparse_matrix = generate_sparse_matrix(MATRIX_ROWS, MATRIX_COLS, SPARSITY)
    
    # 创建数据包
    print("打包数据...")
    packets = create_data_packets(sparse_matrix, PACKET_ROWS)
    
    # 保存到文件
    save_packets_to_file(packets, OUTPUT_FILE)
    
    print(f"成功生成{len(packets)}个数据行")
    print(f"输出文件: {OUTPUT_FILE}")
    print(f"总位数: {sum(len(p) for p in packets)}")