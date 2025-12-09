#import translator
#import tablemd
#import asm_generate
#import mif_coe
#import test_sg
#import hex_to_bin
#
#
##test_sg.main()
##asm_generate.TEST()
##translator.TEST()
##hex_to_bin.test()
##mif_coe.test()
##tablemd.main_t()
#
#A_TYPE = 0          # FP16 0 
#B_TYPE = 0          # BF16 1
#OUTPUT_TYPE = 0     # FP32 2
#mpu_select = 1
#
## 将4个变量拼接成8位二进制数
#MPU_WORD = ((mpu_select & 0x03) << 6) | ((OUTPUT_TYPE & 0x03) << 4) | ((B_TYPE & 0x03) << 2) | (A_TYPE & 0x03)
#
#print(f"MPU_WORD 二进制: {MPU_WORD:08b}")
#print(f"MPU_WORD 十六进制: 0x{MPU_WORD:02X}")
#print(f"MPU_WORD 十进制: {MPU_WORD}")

import SA_X_MAIN
import asm_generate
import main_rom_generate
import main_rom_gen_vcs
import merge_mif_files
import mac_start_make
import hex_to_bin
import mif_coe
import tablemd

def main():


    mac_da = 0x0000f0  
    flag = 0xCCA41704
    mac_lenth= 19
    mac_onece = 9


    mac_start_make.make_XN(mac_da,mac_lenth,mac_onece)

    


if __name__ == "__main__":
    main()