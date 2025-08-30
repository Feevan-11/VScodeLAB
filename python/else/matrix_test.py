import numpy as np
import os

# BF16 conversion functions without external dependencies
def to_bfloat16(array):
    """Convert float32 array to bfloat16 (as uint16)"""
    return array.view(np.uint32).astype(np.uint32) >> 16

def bfloat16_to_float32(array):
    """Convert bfloat16 (as uint16) back to float32"""
    return (array.astype(np.uint32) << 16).view(np.float32)

def matrix_to_mif(matrix, filename, split_by, block_size, internal_order, HER=True, dtype_str='fp16'):
    """生成支持多种数据格式的MIF文件"""
    elem_size = 2  # FP16/BF16默认值
    byte_order = '>'  # 大端序
    
    # 确定元素大小和转换类型
    if dtype_str == 'fp32':
        elem_size = 4
        byte_type = byte_order + 'f4'
    elif dtype_str == 'fp64':
        elem_size = 8
        byte_type = byte_order + 'f8'
    else:  # fp16/bf16
        byte_type = byte_order + 'u2' if dtype_str == 'bf16' else byte_order + 'f2'

    # 根据类型转换矩阵为字节
    if dtype_str == 'bf16':
        matrix = matrix.astype(byte_type)  # BF16使用uint16表示
    else:
        matrix = matrix.astype(byte_type)
        
    elements = []
    
    # 分块处理
    if split_by == 'rows':
        num_blocks = (matrix.shape[0] + block_size - 1) // block_size
        for i in range(num_blocks):
            start = i * block_size
            end = min(start + block_size, matrix.shape[0])
            block = matrix[start:end, :]
            flat_block = block.ravel(order=internal_order)
            elements.append(flat_block.tobytes())
            
    elif split_by == 'cols':
        num_blocks = (matrix.shape[1] + block_size - 1) // block_size
        for j in range(num_blocks):
            start = j * block_size
            end = min(start + block_size, matrix.shape[1])
            block = matrix[:, start:end]
            flat_block = block.ravel(order=internal_order)
            elements.append(flat_block.tobytes())
    
    # 合并所有块数据
    all_bytes = b''.join(elements)
    
    # 分割为元素大小的块
    elements_list = [all_bytes[i:i+elem_size] for i in range(0, len(all_bytes), elem_size)]
    
    # 填充到16元素的倍数
    pad_count = (16 - (len(elements_list) % 16)) % 16
    elements_list.extend([b'\x00' * elem_size] * pad_count)
    
    # 计算总块数
    total_blocks = len(elements_list) // 16
    
    # 生成MIF内容
    mif_content = []
    if HER:
        mif_content.append("DEPTH = {};".format(total_blocks))
        mif_content.append("WIDTH = {};".format(elem_size * 8 * 16))  # 每行16个元素
        mif_content.append("ADDRESS_RADIX = HEX;")
        mif_content.append("DATA_RADIX = HEX;")
        mif_content.append("CONTENT BEGIN")
    
    # 计算地址宽度
    if total_blocks == 0:
        addr_width = 4
    else:
        max_addr = total_blocks - 1
        addr_width = max(4, len(hex(max_addr)) - 2)  # 计算需要的十六进制宽度
    
    # 处理每个16元素的块
    for block_idx in range(total_blocks):
        block = elements_list[block_idx*16 : (block_idx+1)*16]
        reversed_block = block[::-1]  # 小端序调整
        block_bytes = b''.join(reversed_block)
        hex_str = block_bytes.hex().upper()  # 定义hex_str变量
        
        if HER:
            # 格式化地址
            addr_str = format(block_idx, f'0{addr_width}X')
            mif_content.append(f"{addr_str} : {hex_str};")
        else:
            binary_str = ''.join(format(byte, '08b') for byte in block_bytes)
            mif_content.append(binary_str)
    
    if HER:
        mif_content.append("END;")
    
    # 写入文件
    with open(filename, 'w') as f:
        f.write('\n'.join(mif_content))

def main(random=False, A_row=32, A_B=32, B_col=32, T=True, dtype=0):
    """Main function with data type support"""
    dtype_map = {
        0: ('fp16', np.float16),
        1: ('fp32', np.float32),
        2: ('fp64', np.float64),
        3: ('bf16', np.float32)  # Will convert to uint16 later
    }
    
    dtype_str, np_type = dtype_map[dtype]
    print(f"Using data type: {dtype_str}")
    
    # Generate matrices
    if random:
        A = np.random.uniform(-1, 1, (A_row, A_B)).astype(np_type)
        B = np.random.uniform(-1, 1, (A_B, B_col)).astype(np_type)
    else:
        # Create custom matrices
        A = np.array([[1.0] + [1.0]*(A_B-1) for _ in range(A_row)], dtype=np_type)
        if T:
            B = np.eye(A_B, dtype=np_type)
        else:
            B = np.array([[1.0] + [1.0]*(B_col-1) for _ in range(A_B)], dtype=np_type)

    # Handle bfloat16 conversion
    if dtype_str == 'bf16':
        A = to_bfloat16(A.astype(np.float32))
        B = to_bfloat16(B.astype(np.float32))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    matrix_dir = os.path.join(script_dir, "matrix")
    os.makedirs(matrix_dir, exist_ok=True)

    # Setup file paths
    hex_files = (
        os.path.join(matrix_dir, 'a_16.mif'),
        os.path.join(matrix_dir, 'b_16.mif')
    )
    bin_files = (
        os.path.join(matrix_dir, 'a_2.mif'),
        os.path.join(matrix_dir, 'b_2.mif')
    )

    # Generate MIF files
    if dtype == 0:
        b_size = 16
    elif dtype == 1:
        b_size = 8
    elif dtype == 2:
        b_size = 4
    elif dtype == 3:
        b_size = 16
    matrix_to_mif(A, hex_files[0], 'rows', b_size, 'F', HER=True, dtype_str=dtype_str)
    matrix_to_mif(B, hex_files[1], 'cols', b_size, 'C', HER=True, dtype_str=dtype_str)
    matrix_to_mif(A, bin_files[0], 'rows', b_size, 'F', HER=False, dtype_str=dtype_str)
    matrix_to_mif(B, bin_files[1], 'cols', b_size, 'C', HER=False, dtype_str=dtype_str)

    # Compute result matrix
    if dtype_str == 'bf16':
        A_f32 = bfloat16_to_float32(A)
        B_f32 = bfloat16_to_float32(B)
        C = np.matmul(A_f32, B_f32)
        # Convert final result back to bfloat16
        C_result = to_bfloat16(C)
    else:
        if dtype_str in ['fp16']:  # Use higher precision for accumulation
            C = np.matmul(A.astype(np.float32), B.astype(np.float32))
            C_result = C.astype(np_type)
        else:
            C = np.matmul(A, B)
            C_result = C

    # Save result matrices
    np.savetxt(os.path.join(matrix_dir, 'c_10.txt'), C, fmt='%.7g')
    
    # Convert to appropriate output bytes
    if dtype_str == 'fp16':
        c_bytes = C_result.astype('>f2').tobytes()
    elif dtype_str == 'fp32':
        c_bytes = C_result.astype('>f4').tobytes()
    elif dtype_str == 'fp64':
        c_bytes = C_result.astype('>f8').tobytes()
    elif dtype_str == 'bf16':
        c_bytes = C_result.astype('>u2').tobytes()
    
    # Convert to hex representations
    elem_size = 2 if dtype_str in ['fp16', 'bf16'] else 4 if dtype_str == 'fp32' else 8
    hex_list = []
    for i in range(0, len(c_bytes), elem_size):
        # For consistent big-endian representation
        hex_str = c_bytes[i:i+elem_size].hex().upper()
        hex_list.append(hex_str)
    
    # Write hex results
    with open(os.path.join(matrix_dir, f'c_{dtype_str.upper()}.txt'), 'w') as f:
        for i in range(0, len(hex_list), 16):
            line = ' '.join(hex_list[i:i+16])
            f.write(line + '\n')
            
    print("Operation completed successfully")

if __name__ == "__main__":
    # Example usage with different data types
    # main(dtype=0)  # fp16
    # main(dtype=1)  # fp32
    # main(dtype=2)  # fp64
    main(dtype=1)  # bf16