from sg_add import main as sg_add_main
from asm_generate import main as asm_generate_main
from translator import main as translator_main
from matrix_mul import main as matrix_mul_main
from matrix_add import main as matrix_add_main
from hex_to_bin import main as hex_to_bin_main
from merge_mif_files import main as merge_mif_files_main
from SG_mul_all import main as sg_mul_main
from tablemd import main as tablemd_main
from loop import main as loop_main
import matrix_multiple_precision


if __name__ == "__main__":
    A_ROW = 32
    A_B = 512
    B_COL = 32
    descriptors = 0x10000
    random = False
    block_width = 32
    element_size = 2
    APP0 = 0    
    element_type = 0 # FP16 0, FP64 1 
    num = 2
    A_TYPE = 0          # FP16 0
    B_TYPE = 1          # BF16 1
    OUTPUT_TYPE = 0     # FP32 2
    mpu_select = 0      # 0 相同精度 ； 3 多精度

    MPU_WORD = ((mpu_select & 0x03) << 6) | ((OUTPUT_TYPE & 0x03) << 4) | ((B_TYPE & 0x03) << 2) | (A_TYPE & 0x03)
    print(f"MPU_WORD 二进制: {MPU_WORD:08b}")
    

    if(element_type == 0):
        element_size = 2
        block_width = 32
        APP0 = 0

    elif(element_type == 1): 
        element_size = 8
        block_width = 4
        APP0 = 0

    mood = 2 
    
    if(mood == 1):
        sg_add_main(A_ROW,B_COL,descriptors)
    elif(mood == 2):
        sg_mul_main(A_ROW,A_B,B_COL,descriptors,block_width = block_width, element_size = element_size, 
                    APP0 = mpu_select,MPU_ID='1100',MPU_WORD = MPU_WORD,num =num)  
    if(mood == 1):
        matrix_add_main(random,A_ROW,B_COL)   
    elif(mood == 2):
        if (mpu_select == 3):
            matrix_multiple_precision.main(random,A_ROW,A_B,B_COL,A_type = A_TYPE,B_type = B_TYPE,OUTPUT_TYPE = OUTPUT_TYPE)
        elif(mpu_select == 0):
            matrix_mul_main(random,A_ROW,A_B,B_COL,type = element_type)

    hex_to_bin_main()

    merge_mif_files_main()

    tablemd_main()