import MAC
import asm_generate
import main_txt
import hex_to_bin 
import mif_coe
import translator
import tablemd

if __name__ == "__main__":
    MAC.main()
    main_txt.main()
    asm_generate.main()
    translator.main()
    hex_to_bin.MAC()

    mif_coe.main()

    tablemd.main()