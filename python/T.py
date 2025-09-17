import os
import merge_mif_files
def main():
        # script_dir = os.path.dirname(os.path.abspath(__file__))
    
        # name0 = "ROM"
    
        # mif_dir = os.path.join(script_dir,"mif")
    
        # rom_file0 = os.path.join(mif_dir, f"{name0}.mif")
    
        # with open(rom_file0, 'w') as f:
    
        #     f.write("")
        # print('111')
        # merge_mif_files.SA()
        # print('222')
      


    a = 0b000001
    bin_str = bin(a)[2:].zfill(6)
    print(f"参数a的二进制表示: {bin_str} (任务5←最高位 最低位→任务0)")
    
    # 任务1：检查最低位（第0位）
    if bin_str[5] == '1':
        print("执行任务0（最低位）")
        # 这里放置任务0的实际代码
    else:
        print("跳过任务0")
    
    # 任务2：检查第1位
    if bin_str[4] == '1':
        print("执行任务1")
        # 这里放置任务1的实际代码
    else:
        print("跳过任务1")
    
    # 任务3：检查第2位
    if bin_str[3] == '1':
        print("执行任务2")
        # 这里放置任务2的实际代码
    else:
        print("跳过任务2")
    
    # 任务4：检查第3位
    if bin_str[2] == '1':
        print("执行任务3")
        # 这里放置任务3的实际代码
    else:
        print("跳过任务3")
    
    # 任务5：检查第4位
    if bin_str[1] == '1':
        print("执行任务4")
        # 这里放置任务4的实际代码
    else:
        print("跳过任务4")
    
    # 任务6：检查最高位（第5位）
    if bin_str[0] == '1':
        print("执行任务5（最高位）")
        # 这里放置任务5的实际代码
    else:
        print("跳过任务5")


if __name__ == "__main__":
      main()