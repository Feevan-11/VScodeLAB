import SA_X_MAIN
import asm_generate
import main_rom_generate
import merge_mif_files
import macT
import tablemd
import mif_coe

def main():
    # 支持的数据类型: 0:"fp16", 1:"fp32", 2:"fp64", 3:"bf16"
    #[A_ROW,A*B,B_COL,阵列大小,数据字节数,A数据类型,B数据类型]

    martix_List = [[256,256,256,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0]]
    MPU_ID = '1000'
    mac_da = 0xF0001280  
    flag = 0xCCA41704
    mac_lenth= 499
    mac_NUMBER = 14

    main_rom_generate.main(mac_lenth+1,mac_NUMBER)
    print('1')
    SA_X_MAIN.main(martix_List , MPU_ID , mac_da , flag, mac_lenth)

    macT.main()

    merge_mif_files.merge_all()
    merge_mif_files.ROM_TABLE()
    mif_coe





if __name__ == "__main__":
    main()