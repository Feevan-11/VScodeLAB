def generate_mif(binary_list, width, output_file):
    """
    将二进制列表输出为 MIF 文件格式。

    参数:
    - binary_list: 二进制数据列表，每个元素是一个二进制字符串（如 "10101010"）。
    - width: 数据位宽，例如 8 表示每个存储单元 8 位。
    - output_file: 输出的 MIF 文件路径。
    """
    depth = len(binary_list)  # 存储器深度
    with open(output_file, 'w') as mif:
        # 写入 MIF 文件头
        mif.write(f"-- Memory Initialization File\n")
        mif.write(f"WIDTH={width};\n")
        mif.write(f"DEPTH={depth};\n\n")
        mif.write("ADDRESS_RADIX=DEC;\n")  # 地址表示为十进制
        mif.write("DATA_RADIX=BIN;\n\n")  # 数据表示为二进制
        mif.write("CONTENT BEGIN\n")

        # 写入每个地址和对应数据
        for addr, value in enumerate(binary_list):
            mif.write(f"    {addr} : {value};\n")

        # 结束文件
        mif.write("END;\n")

    print(f"MIF 文件已成功生成：{output_file}")


# 示例二进制列表
binary_list = [
    "00000000", "00000001", "00000010", "00000011",
    "00000100", "00000101", "00000110", "00000111",
    "11111111", "10101010", "01010101", "11001100"
]

# 生成 MIF 文件
output_file = "memory.mif"
generate_mif(binary_list, width=8, output_file=output_file)
