import SA_X_MAIN
import asm_generate
import main_rom_generate
import main_rom_gen_vcs
import merge_mif_files
import macT
import tablemd
import mif_coe

def main():
    # 支持的数据类型: 0:"fp16", 1:"fp32", 2:"fp64", 3:"bf16"
    #[A_ROW,A*B,B_COL,阵列大小,数据字节数,A数据类型,B数据类型]

    martix_List = [[32,8,32,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0]]
    MPU_ID = '1000'
    mac_da = 0x0000ff  
    flag = 0xCCA41704
    mac_lenth= 8
    mac_NUMBER = 9
    VCS = 0

    if VCS == 0:
        main_rom_generate.main(mac_lenth+1,mac_NUMBER)
    if VCS == 1:
        main_rom_gen_vcs.main(mac_lenth+1,mac_NUMBER)

    SA_X_MAIN.main(martix_List , MPU_ID , mac_da , flag, mac_lenth)

    macT.main(mac_da)

    mac_num = merge_mif_files.merge_all(mac_lenth+1)

    if (mac_NUMBER == mac_num):
        print("\n帧数正确\n")
    else:
        print("\n需调整帧数\n")

    merge_mif_files.ROM_TABLE()

    if VCS == 0:
        mif_coe.main()



if __name__ == "__main__":
    main()