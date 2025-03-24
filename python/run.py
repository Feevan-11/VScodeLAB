from sg_generate import main as sg_generate_main
from sg_add import main as sg_add_main
from asm_generate import main as asm_generate_main
from translator import main as translator_main
from matrix_generate import main as matrix_main
from matrix_add import main as matrix_add_main
from hex_to_bin import main as hex_to_bin_main
from merge_mif_files import main as merge_mif_files_main
from sg_5 import main as sg_generate5_main

if __name__ == "__main__":
    A_ROW = 16
    A_B = 16
    B_COL = 16
    random = False
    add = False
    if add:
        sg_add_main(A_ROW,B_COL)
    else: 
        sg_generate5_main(A_ROW,A_B,B_COL)   
    #print("\nSuccessfully generated SG\n") 
    print("\n") 
    asm_generate_main()  
    #print("\nSuccessfully generated ASM\n")   
    translator_main() 
    #print("\nSuccessfully translated\n")
    print("\n")  
    if add:
        matrix_add_main(random,A_ROW,B_COL)   
    else:    
        matrix_main(random,A_ROW,A_B,B_COL)
    #print("\nSuccessfully generated matrix\n") 
    hex_to_bin_main()
    #print("\nSuccessfully hex_to_bin\n") 
    merge_mif_files_main()
    #print("\nSuccessfully all\n") 