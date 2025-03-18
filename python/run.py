from sg_generate import main as sg_generate_main
from asm_generate import main as asm_generate_main
from translator import main as translator_main
from matrix_generate import main as matrix_main
from hex_to_bin import main as hex_to_bin_main
from merge_mif_files import main as merge_mif_files_main

if __name__ == "__main__":
    A_ROW = 192
    A_B = 8
    B_COL = 192
    random = False
    sg_generate_main(A_ROW,A_B,B_COL)   
    #print("\nSuccessfully generated SG\n") 
    print("\n") 
    asm_generate_main()  
    #print("\nSuccessfully generated ASM\n")   
    translator_main() 
    #print("\nSuccessfully translated\n")
    print("\n")     
    matrix_main(random,A_ROW,A_B,B_COL)
    #print("\nSuccessfully generated matrix\n") 
    hex_to_bin_main()
    #print("\nSuccessfully hex_to_bin\n") 
    merge_mif_files_main()
    #print("\nSuccessfully all\n") 