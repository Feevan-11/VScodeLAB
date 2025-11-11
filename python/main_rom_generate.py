import  os
import  asm_generate
import  loop
import  translator
import  tablemd
import  mif_coe



def int_to_bin32(value):
    """
    Convert a 32-bit int to a binary string of length 32 (big-endian: bit31 on the left, bit0 on the right).
    """
    return format(value & 0xFFFFFFFF, '032b')




def write_txt_file(words, filename):
    """
    Write words (each element is a 32-bit int) to the .txt file, with 32-bit binary per line, without commas or semicolons.
    """
    with open(filename, 'w') as f:
        for w in words:
            bin_str = int_to_bin32(w)
            hex_string = hex(int(bin_str, 2))
            f.write(hex_string+ "\n")

def write_txt_file_A(words, filename):
    """
    Write words (each element is a 32-bit int) to the .txt file, with 32-bit binary per line, without commas or semicolons.
    """
    with open(filename, 'a') as f:
        for w in words:
            bin_str = int_to_bin32(w)
            hex_string = hex(int(bin_str, 2))
            f.write(hex_string+ "\n")

SGMEM_CDMA0_start    = 0xF4000000
SGMEM_CDMA1_start    = 0xF4200000
SGMEM_DMA0_BASE      = 0xF4400000
SGMEM_DMA1_BASE      = 0xF4800000
SGMEM_DMA2_BASE      = 0xF4C00000
SGMEM_DMA3_BASE      = 0xF5000000
SGMEM_DMA4_BASE      = 0xF5400000
SGMEM_DMA5_BASE      = 0xF5800000
SGMEM_DMA6_BASE      = 0xF5C00000
SGMEM_DMA7_BASE      = 0xF6000000
SGMEM_DMA8_BASE      = 0xF6400000
SGMEM_DMA9_BASE      = 0xF6800000
SGMEM_DMA10_BASE     = 0xF6C00000
SGMEM_DMA11_BASE     = 0xF7000000
SGMEM_ETHDMA0_BASE      = 0xF7400000
SGMEM_ETHDMA1_BASE      = 0xF7600000
SGMEM_ETHDMA2_BASE      = 0xF7800000
SGMEM_ETHDMA3_BASE      = 0xF7A00000
SGMEM_ETHDMA4_BASE      = 0xF7C00000


DMA0_config          = 0xFF000000
DMA1_config          = 0xFF000400
DMA2_config          = 0xFF000800
DMA3_config          = 0xFF000C00
DMA4_config          = 0xFF001000
DMA5_config          = 0xFF001400
DMA6_config          = 0xFF001800
DMA7_config          = 0xFF001C00
DMA8_config          = 0xFF002000
DMA9_config          = 0xFF002400
DMA10_config         = 0xFF002800
DMA11_config         = 0xFF002C00
ethdma0_config       = 0xFF003000
ethdma1_config       = 0xFF003400
ethdma2_config       = 0xFF003800
ethdma3_config       = 0xFF003C00
ethdma4_config       = 0xFF004000
CDMA0_config         = 0xFF004400
CDMA1_config         = 0xFF004440

DDR0_START       = 0x40000000
DDR1_START       = 0x80000000
Data_Mem0        = 0xC0000000
Data_Mem1        = 0xC2000000
Data_Mem2        = 0xC4000000
Data_Mem3        = 0xC6000000
Data_Mem4        = 0xC8000000
Data_Mem5        = 0xCA000000
Data_Mem6        = 0xCC000000
Data_Mem7        = 0xCE000000
Data_Mem8        = 0xD0000000
Data_Mem9        = 0xD2000000
Data_Mem10       = 0xD4000000
Data_Mem11       = 0xD6000000
MPU_REG          = 0xFF005000
URAT             = 0xFF006000

MAC_START  = DDR0_START
MAC_LENTH  = 640
MAC_END    = DDR0_START + (MAC_LENTH * 9) +64
DATA_START = MAC_START + 64


def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))

    MAIN_TXT_name = 'MAIN'
    txt_dir = os.path.join(script_dir,"txt")

    MAIN_TXT_file = os.path.join(txt_dir, f"{MAIN_TXT_name}.txt")

    with open(MAIN_TXT_file, 'w') as f0:

        f0.write("; --- SEGMENT 1 ---" +"\n")   
        f0.write("x1 0x"  + f"{(ethdma0_config          & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma1_config          & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00000000              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00000000              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(0                       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(0                       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(0                       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(0                       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x9 0x"  + f"{(0                       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x10 0x" + f"{(0                       & 0xFFFFFFFF):08x}"+"\n")

        f0.write("; --- SEGMENT 2 ---" +"\n")
        f0.write("x1 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x10 0x"  + f"{(0xFF                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x11 0x"  + f"{(0xF1                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x12 0x"  + f"{(0xF2                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x13 0x"  + f"{(0xF3                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x14 0x"  + f"{(0xF4                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x15 0x"  + f"{(0xFFFFFFFF             & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x20 0x"  + f"{(DDR0_START             & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x21 0x"  + f"{(DATA_START             & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x22 0x"  + f"{(MAC_LENTH              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x23 0x"  + f"{(MAC_END                & 0xFFFFFFFF):08x}"+"\n")
        
        f0.write("; --- SEGMENT 3 ---" +"\n")
        f0.write("x1 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma1_config                  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001008                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{((SGMEM_ETHDMA1_BASE + 64)       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{((SGMEM_ETHDMA1_BASE + 64)       & 0xFFFFFFFF):08x}"+"\n") #MM2S

        f0.write("; --- SEGMENT 4 ---" +"\n")
        f0.write("x1 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma2_config                  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001008                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{((SGMEM_ETHDMA2_BASE + 64)       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{((SGMEM_ETHDMA2_BASE + 64)       & 0xFFFFFFFF):08x}"+"\n") #MM2S

        f0.write("; --- SEGMENT 5 ---" +"\n")
        f0.write("x1 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma3_config                  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001008                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{((SGMEM_ETHDMA3_BASE + 64)       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{((SGMEM_ETHDMA3_BASE + 64)       & 0xFFFFFFFF):08x}"+"\n") #MM2S

        f0.write("; --- SEGMENT 6 ---" +"\n")
        f0.write("x1 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma4_config                  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001008                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{((SGMEM_ETHDMA4_BASE + 64)       & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{((SGMEM_ETHDMA4_BASE + 64)       & 0xFFFFFFFF):08x}"+"\n") #MM2S

        f0.write("; --- SEGMENT 7 ---" +"\n")
        f0.write("x9  0x"  + f"{(0     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x16 0x"  + f"{(1     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x17 0x"  + f"{(2     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x18 0x"  + f"{(3     & 0xFFFFFFFF):08x}"+"\n")

        f0.write("; --- SEGMENT 8 ---" +"\n")
        f0.write("x1 0x"  + f"{(CDMA0_config    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001000      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")

        


if __name__ == "__main__":
    main()
    asm_generate.main()
    translator.main()
    mif_coe.main()
    tablemd.main()



      
