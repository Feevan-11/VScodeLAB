from sg_generate import main as sg_generate_main
from asm_generate import main as asm_generate_main
from translator import main as translator_main
from merge import main as merge_main
from matrix import main as amatrix_main
from btoh import main as btoh_main
from merge_mif_files import main as merge_mif_files_main

if __name__ == "__main__":
    sg_generate_main()    
    asm_generate_main()    
    translator_main()   
    merge_main() 
    amatrix_main()
    btoh_main()
    merge_mif_files_main()