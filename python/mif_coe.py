import sys
import os

def convert_mif_to_coe(input_file,out_file):
    # 检查输入文件后缀
    if not input_file.endswith('.mif'):
        raise ValueError("输入文件必须是.mif格式")
    
    # 生成输出文件名
    output_file = out_file
    
    # 读取输入文件
    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"错误：未找到文件 {input_file}")
        return
    
    # 验证每行是否只包含0和1
    for idx, line in enumerate(lines, 1):
        if not set(line).issubset({'0', '1'}):
            raise ValueError(f"第{idx}行包含非法字符: {line}")
    
    # 处理数据行（添加逗号和分号）
    if not lines:
        raise ValueError("输入文件内容为空")
    processed = [line + ',' for line in lines]
    processed[-1] = processed[-1][:-1] + ';'  # 最后一行替换为分号
    
    # 写入COE文件（包含头部）
    try:
        with open(output_file, 'w') as f:
            f.write("memory_initialization_radix=2;\n")
            f.write("memory_initialization_vector=\n")
            f.write('\n'.join(processed))
    except IOError:
        print(f"错误：无法写入文件 {output_file}")
        return
    
    print(f"转换完成: {input_file} -> {output_file}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif_test")
    coe_dir = os.path.join(script_dir, "coe_test")

    names = ["MAIN_ROM","ALL_MAC","ETH_TILE_SG"]
    for name in names:
        mif_file = os.path.join(mif_dir, f"{name}.mif")
        coe_file = os.path.join(coe_dir, f"{name}.coe")
        convert_mif_to_coe(mif_file,coe_file)

def test():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif")
    coe_dir = os.path.join(script_dir, "coe")

    names = ["test","test_sg","test_data"]
    for name in names:
        mif_file = os.path.join(mif_dir, f"{name}.mif")
        coe_file = os.path.join(coe_dir, f"{name}.coe")
        convert_mif_to_coe(mif_file,coe_file)
def tile_test():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif_test")
    coe_dir = os.path.join(script_dir, "coe_test")

    names = ["test","test_sg","test_data"]
    for name in names:
        mif_file = os.path.join(mif_dir, f"{name}.mif")
        coe_file = os.path.join(coe_dir, f"{name}.coe")
        convert_mif_to_coe(mif_file,coe_file)
if __name__ == "__main__":
    main()