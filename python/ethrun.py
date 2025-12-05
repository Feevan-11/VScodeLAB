import mac_start_make
import asm_generate
import ETH_TEST
import hex_to_bin 
import mif_coe
import translator
import tablemd

if __name__ == "__main__":
    mac_start_make.main()
    ETH_TEST.main()
    asm_generate.ETH_TEST()
    translator.ETH_TEST()
    
    hex_to_bin.MAC()
    hex_to_bin.ETHSG()
    #hex_to_bin.ETHSG1()
    mif_coe.ETHSG()
    tablemd.main()