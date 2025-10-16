from sg_generate import main as sg_generate_main
from asm_generate import main as asm_generate_main
from translator import main as translator_main
from merge import main as merge_main
from matrix import main as matrix_main
from btoh import main as btoh_main
from btoh import MAC as MAC_main
from tablemd import main as ta_main
from merge_mif_files import main as merge_mif_files_main

if __name__ == "__main__":
    A_ROW = 16
    A_B = 16
    B_COL = 16
    random = False
    #A_ROW,A_B,B_COL
    sg_generate_main(A_ROW,A_B,B_COL)    
    asm_generate_main()    
    translator_main()  
    print("a1") 
    #merge_main() 
    print("a")
    matrix_main(random,A_ROW,A_B,B_COL)
    print("aa")
    btoh_main()
    print("aaa")
    merge_mif_files_main()
    ta_main()
    MAC_main()