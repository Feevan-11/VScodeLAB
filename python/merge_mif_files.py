import os

def merge_and_replace(source_file, append_file):
    """
    Appends the contents of the append_file to the end of source_file and overwrites the original source_file
    :param source_file: appended target file name (will be overwritten)
    :param append_file: The name of the source file to append
    """
    try:
        # Read the original contents of the appended file (source_file).
        with open(source_file, 'r') as f:
            source_data = [line.strip() for line in f if line.strip()]
        
        # Read the contents of the appended file (append_file).
        with open(append_file, 'r') as f:
            append_data = [line.strip() for line in f if line.strip()]
        
        # Verify the binary format
        valid_chars = {'0', '1'}
        all_lines = source_data + append_data
        for line in all_lines:
            if not all(c in valid_chars for c in line):
                raise ValueError(f"Illegal binary data: {line}")
        
        # Overwrite to the original file
        with open(source_file, 'w') as f:
            f.write('\n'.join(all_lines))

        print(f"[{source_file}] The merge is complete，ADD {len(append_data)} line")
        print(f"all lines：{len(all_lines)} (old {len(source_data)} + new {len(append_data)})")
    
    except FileNotFoundError as e:
        print(f"The file does not exist：{e.filename}")
    except ValueError as e:
        print(f"Data validation failed：{str(e)}")
    except Exception as e:
        print(f"The operation failed：{str(e)}")

def merge__replace(source_files, output_file):
    """
    将多个源文件的内容按顺序合并到输出文件中
    :param source_files: 要合并的源文件列表（按顺序合并）
    :param output_file: 输出的目标文件名
    """
    try:
        all_lines = []
        total_files = len(source_files)
        
        # 逐个读取源文件并验证数据
        for i, filename in enumerate(source_files, 1):
            try:
                with open(filename, 'r') as f:
                    file_data = [line.strip() for line in f if line.strip()]
                
                # 验证二进制格式
                valid_chars = {'0', '1'}
                for line in file_data:
                    if not all(c in valid_chars for c in line):
                        raise ValueError(f"文件 '{filename}' 中包含非法二进制数据: {line}")
                
                all_lines.extend(file_data)
                print(f"[{filename}] 已加载，共 {len(file_data)} 行")
                
            except FileNotFoundError:
                print(f"文件不存在：{filename}")
                return
            except ValueError as e:
                print(f"数据验证失败：{str(e)}")
                return
        
        # 将合并后的内容写入输出文件
        with open(output_file, 'w') as f:
            f.write('\n'.join(all_lines))
        
        print(f"\n合并完成！输出文件：{output_file}")
        print(f"总共合并了 {total_files} 个文件")
        print(f"总行数：{len(all_lines)}")
        
        # 显示每个文件的贡献行数
        print("\n各文件贡献行数统计：")
        current_position = 0
        for i, filename in enumerate(source_files, 1):
            with open(filename, 'r') as f:
                file_line_count = len([line.strip() for line in f if line.strip()])
            print(f"  {i}. {filename}: {file_line_count} 行 (位置 {current_position + 1}-{current_position + file_line_count})")
            current_position += file_line_count
    
    except Exception as e:
        print(f"操作失败：{str(e)}")

def merge_all():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif_test")
    
    name0 = "DMA0_with_headers"
    name1 = "DMA1_with_headers"
    name2 = "MATRIX_A_with_headers"
    name3 = "MATRIX_B_with_headers"
    name4 = "SA_with_headers"
    name5 = "ETHDMA1_with_headers"
    name6 = "START_MAC"
    name7 = "ALL_MAC"
    mif_file0 = os.path.join(mif_dir, f"{name0}.mif")
    mif_file1 = os.path.join(mif_dir, f"{name1}.mif")
    mif_file2 = os.path.join(mif_dir, f"{name2}.mif")
    mif_file3 = os.path.join(mif_dir, f"{name3}.mif")
    mif_file4 = os.path.join(mif_dir, f"{name4}.mif")
    mif_file5 = os.path.join(mif_dir, f"{name5}.mif")
    mif_file6 = os.path.join(mif_dir, f"{name6}.mif")
    mif_file7 = os.path.join(mif_dir, f"{name7}.mif")

    print("The ALL_MAC is being processed...")
    files_to_merge = [mif_file0, mif_file1, mif_file2, mif_file3, mif_file4, mif_file5, mif_file6]
    output_filename = mif_file7
    
    merge__replace(files_to_merge, output_filename)

def SA():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif")
    mat_dir = os.path.join(script_dir, "mif")
    
    name0 = "ROM"
    name1 = "SA"
    mif_file0 = os.path.join(mif_dir, f"{name0}.mif")
    mif_file1 = os.path.join(mat_dir, f"{name1}.mif")

    print("The SA series is being processed...")
    merge_and_replace(mif_file0, mif_file1)

def SG():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif")
    mat_dir = os.path.join(script_dir, "mif")
    
    name0 = "ROM"
    name1 = "SG"
    mif_file0 = os.path.join(mif_dir, f"{name0}.mif")
    mif_file1 = os.path.join(mat_dir, f"{name1}.mif")

    print("The SA series is being processed...")
    merge_and_replace(mif_file0, mif_file1)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif")
    mat_dir = os.path.join(script_dir, "matrix")
    
    name0 = "GM0"
    name1 = "MATRIX_A"
    mif_file0 = os.path.join(mif_dir, f"{name0}.mif")
    mif_file1 = os.path.join(mif_dir, f"{name1}.mif")

    # first：GM0.mif + a_2.mif
    print("The GM0 series is being processed...")
    merge_and_replace(mif_file0, mif_file1)
    
    name2 = "GM1"
    name3 = "MATRIX_B"
    mif_file2 = os.path.join(mif_dir, f"{name2}.mif")
    mif_file3 = os.path.join(mif_dir, f"{name3}.mif")
    # The second group：GM11.mif + b_2.mif
    print("\nGM1 series is being processed...")
    merge_and_replace(mif_file2, mif_file3)

def SPARSE_main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif")
    sparse_dir = os.path.join(script_dir, "sparse")
    
    name0 = "GM0"
    name1 = "matrix_a_packets"
    mif_file0 = os.path.join(mif_dir, f"{name0}.mif")
    mif_file1 = os.path.join(sparse_dir, f"{name1}.mif")

    # first：GM0.mif + a_2.mif
    print("The GM0 series is being processed...")
    merge_and_replace(mif_file0, mif_file1)
    
    name2 = "GM1"
    name3 = "matrix_b_packets"
    mif_file2 = os.path.join(mif_dir, f"{name2}.mif")
    mif_file3 = os.path.join(sparse_dir, f"{name3}.mif")
    # The second group：GM11.mif + b_2.mif
    print("\nGM1 series is being processed...")
    merge_and_replace(mif_file2, mif_file3)

def ROM_TABLE():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif_test")
    sparse_dir = os.path.join(script_dir, "sparse")
    
    name0 = "MAIN_ROM"
    name1 = "routing_table"
    mif_file0 = os.path.join(mif_dir, f"{name0}.mif")
    mif_file1 = os.path.join(mif_dir, f"{name1}.mif")

    # first：GM0.mif + a_2.mif
    print("The GM0 series is being processed...")
    merge_and_replace(mif_file0, mif_file1)


if __name__ == "__main__":
    main()