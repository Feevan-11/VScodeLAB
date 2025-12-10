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
    # 支持的数据类型: 0:"fp16", 1:"fp32", 2:"fp64", 3:"bf16"
    #[A_ROW,A*B,B_COL,阵列大小,数据字节数,A数据类型,B数据类型]

    martix_List = [[288,288,288,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0]]
    MPU_ID = '1000'
    mac_da = 0x0000ff  
    flag = 0xCCA41704
    mac_lenth= 19
    mac_onece = 352 #352
    VCS = 0

    if VCS == 0:
        main_rom_generate.main(mac_lenth+1,mac_onece)
    if VCS == 1:
        main_rom_gen_vcs.main(mac_lenth+1,mac_onece)

    SA_X_MAIN.main(martix_List , MPU_ID , mac_da , flag, mac_lenth)

    mac_start_make.main(mac_da,mac_lenth)

    mac_num = merge_mif_files.merge_all(mac_lenth+1)

    mac_add = mac_onece - mac_num % mac_onece

    mac_start_make.make_null(mac_da,mac_lenth,mac_add)


    merge_mif_files.add_null()


    mif_coe.main()
    tablemd.main()
    


if __name__ == "__main__":
    main()