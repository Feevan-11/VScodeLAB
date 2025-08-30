from sg_add import main as sg_add_main
from asm_generate import main as asm_generate_main
from translator import main as translator_main
from matrix_mul import main as matrix_mul_main
from matrix_add import main as matrix_add_main
from hex_to_bin import main as hex_to_bin_main
from merge_mif_files import main as merge_mif_files_main
from SG_mul import main as sg_mul_main
from tablemd import main as tablemd_main
from loop import main as loop_main


if __name__ == "__main__":
    A_ROW = 64
    A_B = 64
    B_COL = 64
    descriptors = 0x00008000
    random = False
    block_width = 16
    element_size = 2
    APP0 = 3

    element_type = 0 # FP16 0, FP32 1, FP64 2, BF16 3, 

    if(element_type == 0):
        element_size = 2
        block_width = 16
        APP0 = 3
    elif(element_type == 1): 
        element_size = 4
        block_width = 8
        APP0 = 1
    elif(element_type == 2): 
        element_size = 8
        block_width = 4
        APP0 = 0
    elif(element_type == 3): 
        element_size = 2
        block_width = 16
        APP0 = 2

    mood = 2 #1+,2*

    if(mood == 1):
        sg_add_main(A_ROW,B_COL,descriptors)
    elif(mood == 2): 
        sg_mul_main(A_ROW,A_B,B_COL,descriptors,block_width = block_width, element_size = element_size, APP0 = APP0)  


    print("\n") 
    asm_generate_main(GM1 = mood)  
    loop_main()
 
    translator_main() 

    print("\n")  
    if(mood == 1):
        matrix_add_main(random,A_ROW,B_COL)   
    elif(mood == 2):    
        matrix_mul_main(random,A_ROW,A_B,B_COL,T=False,type=element_type)

    hex_to_bin_main()

    merge_mif_files_main()

    tablemd_main()