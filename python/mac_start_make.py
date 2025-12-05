import  os
from typing import List, Tuple, Optional



def u32(x: int) -> int:
    """限制为32-bit无符号"""
    return x & 0xFFFFFFFF

def make_mac_head(mac_flag: int, mac_da: int, stye: int, data_da: int, data_bbt: int) :
    """生成 16×32bit 的 MAC 头部（前 5 项有效，其余补 0）。"""
    words = [0] * 16
    words[0] = u32(mac_flag)
    words[1] = u32(mac_da)
    words[2] = u32(stye)
    words[3] = u32(data_da)
    words[4] = u32(data_bbt)
    return words

def header_words_to_bin_line(words: List[int]) -> str:
    """
    将16个32-bit word 组装为一行512位二进制字符串：
    规则：word15 在左，word0 在右（即 word15 是最高位段，word0 是最低位段）
    """
    if len(words) != 16:
        raise ValueError("头部words长度必须为16。")
    panull_macs = []
    for i in range(15, -1, -1):
        panull_macs.append(f"{u32(words[i]):032b}")
    return "".join(panull_macs)



def main(mac_da,mac_len):


    script_dir = os.path.dirname(os.path.abspath(__file__))

    name0 = "routing_table"
    name1 = "STAnull_mac_MAC"

    mif_dir = os.path.join(script_dir,"mif_test")

    null_file = os.path.join(mif_dir, f"{name0}.mif")
    stanull_mac_file1 = os.path.join(mif_dir, f"{name1}.mif")

    mac_da = mac_da  
    flag = 0xCCA41704

    null_mac = make_mac_head(0xFF, 0xFF, 0xFF, 0xFF, 0xFF)
    stanull_mac = make_mac_head(flag, mac_da, 2, 0x88b5, 0)

    null_mac_BIN = header_words_to_bin_line(null_mac)
    header_bin_line = header_words_to_bin_line(stanull_mac)

    with open(null_file, 'w') as f:
        f.write(null_mac_BIN)


    with open(stanull_mac_file1, 'w') as f:
        f.write(header_bin_line + '\n')
        for _ in range(mac_len):  
            f.write('01' * 256 + '\n')

def make_null(mac_da,mac_len,mac_add):


    script_dir = os.path.dirname(os.path.abspath(__file__))

    name0 = "null_mac"

    mif_dir = os.path.join(script_dir,"mif_test")

    null_file = os.path.join(mif_dir, f"{name0}.mif")


    mac_da = mac_da  
    flag = 0xCCA41704

    null_mac = make_mac_head(flag, mac_da, 3, 0x88b5, 0)

    null_mac_BIN = header_words_to_bin_line(null_mac)

    with open(null_file, 'w') as f:
        print('共添加帧数：',mac_add)
        for _ in range(mac_add):  
            f.write(null_mac_BIN + '\n')
            for _ in range(mac_len):  
                f.write('01' * 256 + '\n')    

if __name__ == "__main__":
    main(mac_da = 0xCCA41704,mac_len = 19)



      
