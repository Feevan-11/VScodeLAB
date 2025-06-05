import numpy as np
import os

def matrix_1_norm(A):
    return np.max(np.sum(np.abs(A), axis=0))

def matrix_inf_norm(A):
    return np.max(np.sum(np.abs(A), axis=1))

def matrix_to_mif(matrix, split_by, block_size, internal_order, HER=True):
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
        mif_content.append("DEPTH = {};".format(len(elements_list)//16))
        mif_content.append("WIDTH = 256;")
        mif_content.append("ADDRESS_RADIX = HEX;")
        mif_content.append("DATA_RADIX = HEX;")
        mif_content.append("CONTENT BEGIN")
    
    # 处理每个16元素的块
    for block_idx in range(len(elements_list) // 16):
        block = elements_list[block_idx*16 : (block_idx+1)*16]
        reversed_block = block[::-1]  # 小端序调整
        block_bytes = b''.join(reversed_block)
        hex_str = block_bytes.hex().upper()
        binary_str = format(int(hex_str, 16), '0256b')

        if HER:
            mif_content.append("  {}: {};".format(format(block_idx, '04X'), hex_str))
        else:
            mif_content.append(binary_str)
    if HER:
        mif_content.append("END;")
    
    return mif_content

def main(matrix_size=32):
    # 生成方阵A
    A = np.array([[2.0 if i == j else 0.0 for j in range(matrix_size)] 
                 for i in range(matrix_size)], dtype=np.float16)
    
    # 计算初始矩阵X0
    norm1 = matrix_1_norm(A.astype(np.float32))
    norm_inf = matrix_inf_norm(A.astype(np.float32))
    alpha = 1.0 / (norm1 * norm_inf)
    X0 = (alpha * A.T).astype(np.float16)
    
    # 牛顿迭代5次
    X = X0.copy()
    for _ in range(5):
        I = np.eye(matrix_size, dtype=np.float16)
        AX = A.astype(np.float32) @ X.astype(np.float32)
        X = X.astype(np.float32) @ (2*I - AX).astype(np.float32)
        X = X.astype(np.float16)

    I2 = 2*np.eye(matrix_size, dtype=np.float16)
    I = np.eye(16, dtype=np.float16)
    _I = np.array([[-1.0 if i == j else 0.0 for j in range(16)] 
                 for i in range(16)], dtype=np.float16)

    
    # 保存文件

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
    
    X0_MIF = matrix_to_mif(X0,'rows', 16, 'F', HER=False)
    I2_MIF = matrix_to_mif(I2,'rows', 16, 'F', HER=False)
    _I_MIF = matrix_to_mif(_I,'rows', 16, 'F', HER=False)

    A_MIF  = matrix_to_mif(A, 'cols', 16, 'C', HER=False)
    I_MIF  = matrix_to_mif(I, 'cols', 16, 'C', HER=False)

    a_2 = X0_MIF + I2_MIF + _I_MIF
    with open(bin_files[0], 'w') as f:
        f.write('\n'.join(a_2))

    b_2 = A_MIF + I_MIF 
    with open(bin_files[1], 'w') as f:
        f.write('\n'.join(b_2))

    X0_H = matrix_to_mif(X0,'rows', 16, 'F', HER=True)
    I2_H = matrix_to_mif(I2,'rows', 16, 'F', HER=True)
    _I_H = matrix_to_mif(_I,'rows', 16, 'F', HER=True)

    A_H  = matrix_to_mif(A, 'cols', 16, 'C', HER=True)
    I_H  = matrix_to_mif(I, 'cols', 16, 'C', HER=True)

    a_16 = X0_H + I2_H + _I_H
    with open(hex_files[0], 'w') as f:
        f.write('\n'.join(a_16))

    b_16 = A_H + I_H 
    with open(hex_files[1], 'w') as f:
        f.write('\n'.join(b_16))

    X5_MIF = matrix_to_mif(X,'rows', 16, 'F', HER=True)
    
    with open(os.path.join(matrix_dir, 'X5_result.mif'),'w') as f:
        f.write('\n'.join(X5_MIF))
    # 保存验证数据
    np.savetxt(os.path.join(matrix_dir, 'A_matrix.txt'), A,  fmt='%6.3f')
    np.savetxt(os.path.join(matrix_dir, 'X5_result.txt'), X, fmt='%6.3f')

if __name__ == "__main__":
    main(matrix_size=32)