import os
from pathlib import Path

def create_folder_structure():
    # 定义主文件夹名称列表
    main_folders = [
        "F-1-001", "F-1-002", "F-1-003", "F-1-004", "F-1-005", "F-1-006", "F-1-007", "F-1-008", "F-1-009",
        "F-1-0010", "F-1-0011", "F-1-0012", "F-1-013", "F-1-014", "F-1-015", "F-1-016", "F-2-001", "F-2-002",
        "F-2-003", "F-2-004", "F-2-005", "F-2-006", "P-3-001", "P-3-002", "P-4-001", "P-4-002", "P-4-003",
        "P-4-004", "P-4-005", "F-5-001", "F-5-002", "F-5-003", "F-5-004", "F-5-005", "F-5-006", "F-5-007",
        "F-5-008", "F-5-009", "F-5-010", "F-5-011", "F-5-012", "F-5-013", "F-5-014", "F-5-015", "F-5-016",
        "F-5-017", "F-5-018", "F-5-019", "F-6-001", "F-6-002", "F-6-003", "F-6-004", "F-6-005", "F-6-006",
        "F-6-007", "F-6-008", "F-6-009", "F-6-010", "F-6-011", "F-6-012", "F-6-013", "F-6-014", "F-7-001",
        "F-7-002", "F-7-003", "F-7-004", "F-7-005", "F-7-006", "F-8-001", "F-8-002", "F-8-003", "F-8-004",
        "F-9-001", "F-9-002", "F-9-003", "F-10-001", "F-10-002", "F-10-003", "P-10-004", "P-10-005", "P-10-006",
        "F-11-001", "F-11-002", "P-11-003", "P-11-004", "F-12-001", "P-12-002", "P-12-003", "P-12-004", "F-13-001",
        "F-13-002", "F-13-003", "F-14-001", "F-14-002", "F-15-001"
    ]
    
    # 定义子文件夹结构
    subfolders = {
        'BIT': ['tile_impl.bit', 'impl_tile.ltx'],
        'SIM': ['ROM.mif', 'GM0.mif', 'GM1.mif'],
        'MATRIX': ['A.csv', 'B.csv'],
        'MAC': ['MAC.txt'],
        'TEST_RESULT': ['误差.txt']
    }
    
    # 创建主文件夹和子结构
    for main_folder in main_folders:
        try:
            # 创建主文件夹[1,6](@ref)
            main_path = Path(main_folder)
            main_path.mkdir(parents=True, exist_ok=True)
            print(f"创建主文件夹: {main_folder}")
            
            # 创建子文件夹和文件
            for subfolder, files in subfolders.items():
                subfolder_path = main_path / subfolder
                subfolder_path.mkdir(exist_ok=True)
                print(f"  创建子文件夹: {subfolder}")
                
                # 在子文件夹中创建文件
                for file in files:
                    file_path = subfolder_path / file
                    file_path.touch()  # 创建空文件
                    print(f"    创建文件: {file}")
                    
        except Exception as e:
            print(f"错误: 创建 {main_folder} 时出现问题 - {e}")
    
    print("\n文件夹结构创建完成！")

def create_folder_structure_with_os():
    """
    使用os模块的替代版本[1,8](@ref)
    """
    import os
    
    # 定义主文件夹名称列表（同上）
    main_folders = [
        "F-1-001", "F-1-002", "F-1-003", "F-1-004", "F-1-005", "F-1-006", "F-1-007", "F-1-008", "F-1-009",
        "F-1-0010", "F-1-0011", "F-1-0012", "F-1-013", "F-1-014", "F-1-015", "F-1-016", "F-2-001", "F-2-002",
        "F-2-003", "F-2-004", "F-2-005", "F-2-006", "P-3-001", "P-3-002", "P-4-001", "P-4-002", "P-4-003",
        "P-4-004", "P-4-005", "F-5-001", "F-5-002", "F-5-003", "F-5-004", "F-5-005", "F-5-006", "F-5-007",
        "F-5-008", "F-5-009", "F-5-010", "F-5-011", "F-5-012", "F-5-013", "F-5-014", "F-5-015", "F-5-016",
        "F-5-017", "F-5-018", "F-5-019", "F-6-001", "F-6-002", "F-6-003", "F-6-004", "F-6-005", "F-6-006",
        "F-6-007", "F-6-008", "F-6-009", "F-6-010", "F-6-011", "F-6-012", "F-6-013", "F-6-014", "F-7-001",
        "F-7-002", "F-7-003", "F-7-004", "F-7-005", "F-7-006", "F-8-001", "F-8-002", "F-8-003", "F-8-004",
        "F-9-001", "F-9-002", "F-9-003", "F-10-001", "F-10-002", "F-10-003", "P-10-004", "P-10-005", "P-10-006",
        "F-11-001", "F-11-002", "P-11-003", "P-11-004", "F-12-001", "P-12-002", "P-12-003", "P-12-004", "F-13-001",
        "F-13-002", "F-13-003", "F-14-001", "F-14-002", "F-15-001"
    ]
    
    # 定义子文件夹结构
    subfolders = {
        'BIT': ['tile_impl.bit', 'impl_tile.ltx'],
        'SIM': ['ROM.mif', 'GM0.mif', 'GM1.mif'],
        'MATRIX': ['A.csv', 'B.csv'],
        'TEST_RESULT': ['误差.txt']
    }
    
    for main_folder in main_folders:
        try:
            # 创建主文件夹[1,7](@ref)
            os.makedirs(main_folder, exist_ok=True)
            print(f"创建主文件夹: {main_folder}")
            
            # 创建子文件夹和文件
            for subfolder, files in subfolders.items():
                subfolder_path = os.path.join(main_folder, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                print(f"  创建子文件夹: {subfolder}")
                
                # 在子文件夹中创建文件
                for file in files:
                    file_path = os.path.join(subfolder_path, file)
                    with open(file_path, 'w') as f:
                        pass  # 创建空文件
                    print(f"    创建文件: {file}")
                    
        except Exception as e:
            print(f"错误: 创建 {main_folder} 时出现问题 - {e}")
    
    print("\n文件夹结构创建完成！")

if __name__ == "__main__":
    # 使用pathlib版本（推荐）
    create_folder_structure()
    
    # 如果想要使用os模块版本，取消注释下行
    # create_folder_structure_with_os()