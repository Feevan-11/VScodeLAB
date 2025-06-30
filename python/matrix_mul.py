import numpy as np
import os

def matrix_to_mif(matrix, filename, split_by, block_size, internal_order, HER=True):
    """生成符合要求的MIF文件，支持分块存储"""
    matrix = matrix.astype('>f2')  # 大端序FP16
    elements = []
    
    # 分块处理
    if split_by == 'rows':
        num_blocks = (matrix.shape[0] + block_size - 1) // block_size
        for i in range(num_blocks):
            start = i * block_size
            end = min(start + block_size, matrix.shape[0])
            block = matrix[start:end, :]
            elements.append(block.ravel(order=internal_order).tobytes())
            
    elif split_by == 'cols':
        num_blocks = (matrix.shape[1] + block_size - 1) // block_size
        for j in range(num_blocks):
            start = j * block_size
            end = min(start + block_size, matrix.shape[1])
            block = matrix[:, start:end]
            elements.append(block.ravel(order=internal_order).tobytes())
    
    # 合并所有块数据
    all_bytes = b''.join(elements)
    
    # 转换为元素列表
    elements_list = [all_bytes[i:i+2] for i in range(0, len(all_bytes), 2)]
    
    # 补零到16的倍数
    pad_count = (16 - (len(elements_list) % 16)) % 16
    elements_list += [b'\x00\x00'] * pad_count
    
    # 生成MIF内容
    mif_content = []
    if HER:
        mif_content = [
            "DEPTH = {};".format(len(elements_list)//16),
            
        ]
    
    # 处理每个16元素的块
    for block_idx in range(len(elements_list) // 16):
        block = elements_list[block_idx*16 : (block_idx+1)*16]
        reversed_block = block[::-1]  # 小端序调整
        block_bytes = b''.join(reversed_block)
        hex_str = block_bytes.hex().upper()
        binary_str = format(int(hex_str, 16), '0256b')
        
        if HER:
            mif_content.append("{} : {};".format(format(block_idx, '04X'), hex_str))
        else:
            mif_content.append(binary_str)
    
    if HER:
        mif_content.append("END;")
    
    # 写入文件
    with open(filename, 'w') as f:
        f.write('\n'.join(mif_content))

def main(random = False, A_row = 32, A__B = 16, B_col = 32,T = True, type = 0 ):

    # 配置参数
    random_mode = random  # True=随机矩阵，False=自定义矩阵

    #    自定义矩阵 (random_mode=False时生效)

    Arow = A_row
    A_B = A__B
    Bcol = B_col
    if type ==0:
        fp=np.float16
    elif type ==1:
        fp=np.float32
    elif type ==2:
        fp=np.float64
    elif type ==3:
        fp=np.float16
    A_custom = np.array([[2.0] + [1.0]*(A_B-1) for _ in range(Arow)], dtype=fp)
    if T:
        B_custom = np.eye(A__B, dtype=fp)
    else:
        B_custom = np.array([[1.0] + [1.0]*(Bcol-1) for _ in range(A_B)], dtype=fp)
    

    # 生成矩阵
    if random_mode:
       A = np.random.uniform(-1, 1, (Arow, A_B)).astype(np.float16)
       B = np.random.uniform(-1, 1, (A_B, Bcol)).astype(np.float16)
    else:
        A = A_custom
        B = B_custom

    script_dir = os.path.dirname(os.path.abspath(__file__))
    matrix_dir = os.path.join(script_dir, "matrix")
    os.makedirs(matrix_dir, exist_ok=True)

    # 生成文件路径
    hex_files = (
        os.path.join(matrix_dir, 'a_16.mif'),
        os.path.join(matrix_dir, 'b_16.mif')
    )
    bin_files = (
        os.path.join(matrix_dir, 'a_2.mif'),
        os.path.join(matrix_dir, 'b_2.mif')
    )

    # 生成矩阵文件
    matrix_to_mif(A, hex_files[0], 'rows', 16, 'F', HER=True)
    matrix_to_mif(B, hex_files[1], 'cols', 16, 'C', HER=True)
    matrix_to_mif(A, bin_files[0], 'rows', 16, 'F', HER=False)
    matrix_to_mif(B, bin_files[1], 'cols', 16, 'C', HER=False)

    # 计算并保存结果矩阵
    C = np.matmul(A.astype(np.float32), B.astype(np.float32)).astype(np.float16)
    
    # 保存十进制结果
    np.savetxt(os.path.join(matrix_dir, 'c_10.txt'), C, fmt='%.7g')
    
    # 将结果转换为小端序字节流
    c_bytes = C.astype('<f2').tobytes()
    # 生成十六进制字符串列表（每2字节反转后转大写）
    hex_list = []
    for i in range(0, len(c_bytes), 2):
        # 反转字节顺序得到正确的十六进制表示
        reversed_bytes = c_bytes[i:i+2][::-1]
        hex_str = reversed_bytes.hex().upper()
        hex_list.append(hex_str)
    with open(os.path.join(matrix_dir, 'c_FP16.txt'), 'w') as f:
        for i in range(0, len(hex_list), 16):
            line = ' '.join(hex_list[i:i+16])
            f.write(line + '\n')

if __name__ == "__main__":
    main(random = False, A_row = 32, A__B = 32, B_col = 32)