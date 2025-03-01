import os

def process_mif(input_filename, output_filename):
    # 读取输入文件并预处理
    try:
        with open(input_filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"错误：文件 {input_filename} 不存在")
        return

    # 验证每行格式
    valid_lines = []
    for idx, line in enumerate(lines, 1):
        if len(line) != 128:
            print(f"第 {idx} 行长度错误：应为128位，实际为{len(line)}位")
            return
        if not all(c in {'0', '1'} for c in line):
            print(f"第 {idx} 行包含非法字符")
            return
        valid_lines.append(line)

    # 组合二进制数据
    combined = []
    for i in range(0, len(valid_lines), 2):
        if i+1 < len(valid_lines):
            # 第二行放左边，第一行放右边
            combined.append(valid_lines[i+1] + valid_lines[i])

    # 写入输出文件
    with open(output_filename, 'w') as f:
        f.write('\n'.join(combined))
    
    print(f"转换完成！共处理 {len(valid_lines)} 行，生成 {len(combined)} 行256位数据")

if __name__ == "__main__":

    script_dir = os.path.dirname(os.path.abspath(__file__))

    input_file = "DMNGM1"    # 输入文件名
    output_file = "DMNGM11"  # 输出文件名

    mif_dir = os.path.join(script_dir,"mif")

    input_filename = os.path.join(mif_dir, f"{input_file}.mif")
    output_filename = os.path.join(mif_dir, f"{output_file}.mif")
    
    process_mif(input_filename, output_filename)