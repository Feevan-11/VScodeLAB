import os

def merge_and_replace(source_file, append_file):
    """
    将 append_file 的内容追加到 source_file 末尾，并覆盖原 source_file
    :param source_file: 被追加的目标文件名（会被覆盖）
    :param append_file: 要追加的源文件名
    """
    try:
        # 读取被追加文件（source_file）的原始内容
        with open(source_file, 'r') as f:
            source_data = [line.strip() for line in f if line.strip()]
        
        # 读取追加文件（append_file）的内容
        with open(append_file, 'r') as f:
            append_data = [line.strip() for line in f if line.strip()]
        
        # 验证二进制格式
        valid_chars = {'0', '1'}
        all_lines = source_data + append_data
        for line in all_lines:
            if not all(c in valid_chars for c in line):
                raise ValueError(f"非法二进制数据: {line}")
        
        # 覆盖写入原文件
        with open(source_file, 'w') as f:
            f.write('\n'.join(all_lines))
        
        # 输出统计信息
        print(f"[{source_file}] 合并完成，追加 {len(append_data)} 行")
        print(f"总行数：{len(all_lines)} (原 {len(source_data)} + 新 {len(append_data)})")
    
    except FileNotFoundError as e:
        print(f"文件不存在：{e.filename}")
    except ValueError as e:
        print(f"数据验证失败：{str(e)}")
    except Exception as e:
        print(f"操作失败：{str(e)}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif")
    mat_dir = os.path.join(script_dir, "matrix")
    
    name0 = "GM0"
    name1 = "a_2"
    mif_file0 = os.path.join(mif_dir, f"{name0}.mif")
    mif_file1 = os.path.join(mat_dir, f"{name1}.mif")

    # 第一组：GM0.mif + a_2.mif
    print("正在处理 GM0 系列...")
    merge_and_replace(mif_file0, mif_file1)
    
    name2 = "GM11"
    name3 = "b_2"
    mif_file2 = os.path.join(mif_dir, f"{name2}.mif")
    mif_file3 = os.path.join(mat_dir, f"{name3}.mif")
    # 第二组：GM11.mif + b_2.mif
    print("\n正在处理 GM11 系列...")
    merge_and_replace(mif_file2, mif_file3)

if __name__ == "__main__":
    main()