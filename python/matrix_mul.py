import numpy as np
import os
import struct


def matrix_to_mif(matrix, filename, split_by, block_size, internal_order, HER=True):
    """生成符合要求的MIF文件，支持多种数据类型"""
    # 确定数据类型和字节大小
    dtype_map = {
        np.float16: ('>f2', 2),
        np.float32: ('>f4', 4),
        np.float64: ('>f8', 8),
        np.uint16: ('>u2', 2)  # 保留原BF16路径，但当前主流程不会用到
    }

    if matrix.dtype == np.float16:
        dtype_str, element_size = dtype_map[np.float16]
        matrix = matrix.astype(dtype_str)
    elif matrix.dtype == np.float32:
        dtype_str, element_size = dtype_map[np.float32]
        matrix = matrix.astype(dtype_str)
    elif matrix.dtype == np.float64:
        dtype_str, element_size = dtype_map[np.float64]
        matrix = matrix.astype(dtype_str)
    elif matrix.dtype == np.uint16:  # BF16（目前不会用到）
        dtype_str, element_size = dtype_map[np.uint16]
        # 确保是大端序
        matrix = matrix.astype('>u2')
    else:
        # 默认使用FP16
        dtype_str, element_size = dtype_map[np.float16]
        matrix = matrix.astype(dtype_str)

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
    elements_list = [all_bytes[i:i + element_size] for i in range(0, len(all_bytes), element_size)]

    # 计算每行元素数量（512位/元素大小）
    elements_per_line = 512 // (element_size * 8)

    # 补零到elements_per_line的倍数
    pad_count = (elements_per_line - (len(elements_list) % elements_per_line)) % elements_per_line
    elements_list += [b'\x00' * element_size] * pad_count

    # 生成MIF内容
    mif_content = []
    if HER:
        mif_content = [
            f"DEPTH = {len(elements_list) // elements_per_line};",
        ]

    # 处理每个块（512位）
    for block_idx in range(len(elements_list) // elements_per_line):
        block = elements_list[block_idx * elements_per_line: (block_idx + 1) * elements_per_line]

        # 将块分成两个子块
        subblock_size = elements_per_line // 2
        subblock1 = block[subblock_size:elements_per_line]  # 高地址部分
        subblock2 = block[0:subblock_size]                  # 低地址部分

        # 分别反转每个子块
        reversed_subblock1 = subblock1[::-1]
        reversed_subblock2 = subblock2[::-1]

        # 合并子块：高地址在左，低地址在右
        combined_block = reversed_subblock1 + reversed_subblock2
        block_bytes = b''.join(combined_block)
        hex_str = block_bytes.hex().upper()

        if HER:
            mif_content.append(f"{format(block_idx, '04X')} : {hex_str};")
        else:
            # 对于二进制模式，转换为512位二进制字符串
            binary_str = format(int(hex_str, 16), '0512b')
            mif_content.append(binary_str)

    if HER:
        mif_content.append("END;")

    # 写入文件
    with open(filename, 'w') as f:
        f.write('\n'.join(mif_content))


def main(random=False, A_row=32, A__B=32, B_col=32, type=0, COUNT=0):
    """
    当前版本约定：
      - 只支持两种数据类型：fp16 和 fp64
      - A 和 B 的数据类型必须一致，由 type 决定
      - type: 0 -> fp16, 1 -> fp64
      - fp16 按 32 进行分块；fp64 按 4 进行分块
    B_type 参数保留，仅为兼容，实际不再使用。
    """
    # 配置参数
    random_mode = random  # True=随机矩阵，False=自定义矩阵

    # 根据 type 确定数据类型（只支持 fp16 和 fp64）
    if type == 0:
        A_datatype = "fp16"
    elif type == 1:
        A_datatype = "fp64"
    else:
        raise ValueError("type 只能是 0(fp16) 或 1(fp64)")

    # A 和 B 的数据类型必须一致
    B_datatype = A_datatype

    # 根据数据类型选择对应的numpy类型和块大小
    # fp16 -> block_size = 32
    # fp64 -> block_size = 4
    dtype_map = {
        "fp16": (np.float16, 32),
        "fp64": (np.float64, 4),
    }

    A_np_type, A_block_size = dtype_map[A_datatype]
    B_np_type, B_block_size = dtype_map[B_datatype]

    print(f"Using data type: {A_datatype}, A_block_size: {A_block_size}")
    print(f"Using data type: {B_datatype}, B_block_size: {B_block_size}")

    # 自定义矩阵（全 1）
    A_custom = np.array([[1.0] * A__B for _ in range(A_row)], dtype=A_np_type)
    B_custom = np.array([[1.0] * B_col for _ in range(A__B)], dtype=B_np_type)

    # 生成矩阵
    if random_mode:
        A = np.random.uniform(-1, 1, (A_row, A__B)).astype(A_np_type)
        B = np.random.uniform(-1, 1, (A__B, B_col)).astype(B_np_type)
    else:
        A = A_custom
        B = B_custom

    script_dir = os.path.dirname(os.path.abspath(__file__))
    matrix_dir = os.path.join(script_dir, "matrix")
    mif_dir = os.path.join(script_dir, "mif")
    os.makedirs(matrix_dir, exist_ok=True)
    os.makedirs(mif_dir, exist_ok=True)

    # 生成文件路径
    hex_files = (
        os.path.join(matrix_dir, f'a_16.mif'),
        os.path.join(matrix_dir, f'b_16.mif')
    )
    bin_files = (
        os.path.join(mif_dir, 'MATRIX_A.mif'),
        os.path.join(mif_dir, 'MATRIX_B.mif')
    )

    # 生成矩阵文件（不再区分 bf16 等）
    matrix_to_mif(A, hex_files[0], 'rows', A_block_size, 'F', HER=True)
    matrix_to_mif(A, bin_files[0], 'rows', A_block_size, 'F', HER=False)

    matrix_to_mif(B, hex_files[1], 'cols', B_block_size, 'C', HER=True)
    matrix_to_mif(B, bin_files[1], 'cols', B_block_size, 'C', HER=False)

    # 计算结果矩阵 C（统一用 float64 做计算）
    C = np.matmul(A.astype(np.float64), B.astype(np.float64))

    # 保存十进制结果
    np.savetxt(os.path.join(matrix_dir, f'c_{COUNT}.txt'), C, fmt='%.7g')

    # 根据数据类型保存结果（仅 fp16 / fp64）
    if A_datatype == "fp16":
        C_result = C.astype(np.float16)
        c_bytes = C_result.astype('<f2').tobytes()
        suffix = "FP16"
        element_size = 2
    elif A_datatype == "fp64":
        C_result = C.astype(np.float64)
        c_bytes = C_result.astype('<f8').tobytes()
        suffix = "FP64"
        element_size = 8
    else:
        raise ValueError("只支持 fp16 和 fp64 两种结果类型")

    # 生成十六进制字符串列表
    hex_list = []
    for i in range(0, len(c_bytes), element_size):
        # 反转字节顺序得到正确的十六进制表示
        element_bytes = c_bytes[i:i + element_size]
        reversed_bytes = element_bytes[::-1]
        hex_str = reversed_bytes.hex().upper()
        hex_list.append(hex_str)

    with open(os.path.join(matrix_dir, f'c_{suffix}.txt'), 'w') as f:
        for i in range(0, len(hex_list), 16):
            line = ' '.join(hex_list[i:i + 16])
            f.write(line + '\n')


if __name__ == "__main__":
    # 支持的数据类型: 0 -> "fp16", 1 -> "fp64"
    # 例如：fp16
    # main(random=False, A_row=32, A__B=32, B_col=32, type=0, COUNT=0)
    # 例如：fp64
    # main(random=False, A_row=32, A__B=32, B_col=32, type=1, COUNT=0)
    main(random=False, A_row=32, A__B=32, B_col=32, type=0, COUNT=0)
