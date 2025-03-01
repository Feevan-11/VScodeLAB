import numpy as np
import os

# 配置参数
random_mode = True  # True=随机矩阵，False=自定义矩阵
#HER = False          # True=输出16进制，False=输出2进制
M, K, N = 64, 64, 64   # 矩阵维度 A(MxK) B(KxN)

# 自定义矩阵 (random_mode=False时生效)
A_custom = np.array([[1.0, 2.0, 3.0],
                    [4.0, 5.0, 6.0]], dtype=np.float16)
B_custom = np.array([[7.0, 8.0],
                    [9.0, 10.0],
                    [11.0, 12.0]], dtype=np.float16)

# 生成矩阵
if random_mode:
    A = np.random.uniform(-1, 1, (M, K)).astype(np.float16)
    B = np.random.uniform(-1, 1, (K, N)).astype(np.float16)
else:
    A = A_custom
    B = B_custom



def matrix_to_mif(matrix, filename, order='C',HER =True):
    """生成符合要求的MIF文件"""
    # 处理存储顺序并转换大端序
    matrix = matrix.astype('>f2')  # 大端序FP16
    if order == 'F':
        matrix = matrix.T         # 列优先存储
    
    # 将矩阵数据转为字节列表
    byte_list = matrix.tobytes()
    elements = [byte_list[i:i+2] for i in range(0, len(byte_list), 2)]
    
    # 补零到16的倍数个元素
    pad_count = (16 - (len(elements) % 16)) % 16
    elements += [b'\x00\x00'] * pad_count
    
    # 生成MIF文件头
    if HER:
        mif_content = [
        f"DEPTH = {len(elements)//16};",
        ]
    else:
        mif_content = []

    
    # 按16元素分块处理
    for block_idx in range(len(elements)//16):
        # 获取当前块并逆序元素顺序
        block = elements[block_idx*16 : (block_idx+1)*16]
        reversed_block = block[::-1]  # 小端序排列
        
        # 拼接字节数据并转换为HEX
        block_bytes = b''.join(reversed_block)
        hex_str = block_bytes.hex().upper()
        binary_str = format(int(hex_str, 16), '0{}b'.format(len(hex_str)*4))
        
        if HER:
            mif_content.append(f"{block_idx:04X} : {hex_str};")
        else:
            mif_content.append(f"{binary_str};")
        
        
    
    #mif_content.append("END;")
    
    # 写入文件
    with open(filename, 'w') as f:
        f.write('\n'.join(mif_content))

def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    script_dir = os.path.join(script_dir,"matrix")
    # 创建目标文件夹（如果不存在）
    os.makedirs(script_dir, exist_ok=True)       # 自动创建目录，已存在时不报错

    hex_file_a = os.path.join(script_dir, 'a_16.mif')
    hex_file_b = os.path.join(script_dir, 'b_16.mif')
    bin_file_a = os.path.join(script_dir, 'a_2.mif')
    bin_file_b = os.path.join(script_dir, 'b_2.mif')


    # 生成矩阵文件
    matrix_to_mif(A, hex_file_a, 'C', HER = True)  # 行优先存储
    matrix_to_mif(B, hex_file_b, 'F', HER = True)  # 列优先存储
    matrix_to_mif(A, bin_file_a, 'C', HER = False)  # 行优先存储
    matrix_to_mif(B, bin_file_b, 'F', HER = False)  # 列优先存储

    # 矩阵乘法并输出小端序结果
    C = np.matmul(A.astype(np.float32), B.astype(np.float32)).astype(np.float16)
    C_bytes = C.astype('<f2').tobytes()  # 小端序转换

    CC = np.matmul(A.astype(np.float32), B.astype(np.float32)).astype(np.float16)

    # 写入十进制文本文件

    out_c = os.path.join(script_dir,'c_10.txt') 
    out_cc = os.path.join(script_dir,'c_FP16.txt')
                         
    with open(out_c, 'w') as f:
        for row in CC:
        # 使用通用格式输出，自动省略小数点后的零
            line = ' '.join(f"{num:.7g}" for num in row)
            f.write(line + '\n')

    with open(out_cc, 'w') as f:
        # 按两个字节分割数据
        for i in range(0, len(C_bytes), 2):
            hex_str = C_bytes[i:i+2].hex().upper()
            f.write(f"{hex_str}\n")

if __name__ == "__main__":
    main()