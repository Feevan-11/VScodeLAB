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
    name1 = "a_2"
    mif_file0 = os.path.join(mif_dir, f"{name0}.mif")
    mif_file1 = os.path.join(mat_dir, f"{name1}.mif")

    # first：GM0.mif + a_2.mif
    print("The GM0 series is being processed...")
    merge_and_replace(mif_file0, mif_file1)
    
    name2 = "GM1"
    name3 = "b_2"
    mif_file2 = os.path.join(mif_dir, f"{name2}.mif")
    mif_file3 = os.path.join(mat_dir, f"{name3}.mif")
    # The second group：GM11.mif + b_2.mif
    print("\nGM1 series is being processed...")
    merge_and_replace(mif_file2, mif_file3)

if __name__ == "__main__":
    main()