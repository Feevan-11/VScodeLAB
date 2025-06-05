from sg_generate import main as sg_generate_main
from sg_add import main as sg_add_main
from sg import main as sg_main
from asm_generate import main as asm_generate_main
from translator import main as translator_main
from matrix_generate import main as matrix_main
from matrix_add import main as matrix_add_main
from matrix import main as matrix
from hex_to_bin import main as hex_to_bin_main
from merge_mif_files import main as merge_mif_files_main
from SG_one import main as sg_one_main
from tablemd import main as tablemd_main
from loop import main as loop_main


if __name__ == "__main__":
    A_ROW = 128
    A_B = 128
    B_COL = 128
    descriptors = 0x00008000
    random = False
    block_width = 16
    element_size = 2
    APP0 = 0

    mood = 2 #1+,2*,3ni,4T

    if(mood == 1):
        sg_add_main(A_ROW,B_COL,descriptors)
    elif(mood == 2): 
        sg_one_main(A_ROW,A_B,B_COL,descriptors,block_width = block_width, element_size = element_size, APP0 = APP0)
    elif(mood == 3):
        sg_main(A_ROW,descriptors)    
    elif(mood == 4):
        sg_generate_main(A_ROW,A_B,A_B,descriptors)

    print("\n") 
    asm_generate_main(GM1 = mood)  
    loop_main()
 
    translator_main() 

    print("\n")  
    if(mood == 1):
        matrix_add_main(random,A_ROW,B_COL)   
    elif(mood == 2):    
        matrix_main(random,A_ROW,A_B,B_COL,T=False)
    elif(mood == 3):    
        matrix(A_ROW)
    elif(mood == 4):    
        matrix_main(random,A_ROW,A_B,B_COL,T=True)

    hex_to_bin_main()

    merge_mif_files_main()

    tablemd_main()