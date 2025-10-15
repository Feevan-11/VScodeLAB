import macT
import asm_generate
import ethsg
import hex_to_bin 
import mif_coe
import translator
import tablemd

if __name__ == "__main__":
    macT.main()
    ethsg.main()
    asm_generate.check()
    translator.check()
    
    hex_to_bin.MAC()
    hex_to_bin.ETHSG()
    hex_to_bin.ETHSG1()
    mif_coe.ETHSG()
    tablemd.main()