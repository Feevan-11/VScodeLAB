import  os
import  asm_generate
import  loop
import  translator
import  tablemd
import  mif_coe
import  hex_to_bin



def int_to_bin32(value):
    """
    Convert a 32-bit int to a binary string of length 32 (big-endian: bit31 on the left, bit0 on the right).
    """
    return format(value & 0xFFFFFFFF, '032b')

def link_descriptors_in_memory(descriptor_list, base_addr=0x00000000, desc_size=64):

    flattened = []  # Stores the final sequentially expanded 32-bit word

    for i in range(len(descriptor_list)):

        # Calculate the starting physical address of the next descriptor
        if i < len(descriptor_list) - 1:
            next_desc_addr = base_addr + (i + 1) * desc_size
        else:
            next_desc_addr = base_addr

        # Update Word0 for the current descriptor
        words = descriptor_list[i]
        words[0] = next_desc_addr

        # Flatten the updated 16 word into flattened
        flattened.extend(words)

    return flattened

def link_SAME(descriptor_list, base_addr=0x00000000, desc_size=64):

    flattened = []  # Stores the final sequentially expanded 32-bit word

    for i in range(len(descriptor_list)):

        next_desc_addr = base_addr 

        words = descriptor_list[i]
        words[0] = next_desc_addr
        flattened.extend(words)

    return flattened

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

def make_sg_dma_descriptor(
    next_desc_addr,
    buffer_addr,
    length_bytes
):
    
    word0 = 0  # bits[31:6]
    # Word1: 0
    word1 = 0
    # Word2: bufferaddr
    word2 = buffer_addr & 0xFFFFFFFF
    # Word3: 0
    word3 = 0
    # Word4: 0
    word4 = 0
    # Word5: 0
    word5 = 0
    # Word6: [25:0] = length_bytes, [31:26] = 000011
    word6 = (length_bytes & 0x0FFFFFFF)
    # Word7: 0 (status)
    word7 = 0
    word8 = 0 #APP0
    word9 = 0
    word10 = 0
    word11 = 0
    word12 = 0
    word13 = 0
    word14 = 0
    word15 = 0


    return [word0, word1, word2,  word3,  word4,  word5,  word6,  word7,
            word8, word9, word10, word11, word12, word13, word14, word15]


def generate_ethdma_descriptors_for_S2MM(
    data_in_base=0x40000000,
    MAC_LENTH = 64,
    SG_NUM = 100
):

    descriptors = []


    block_size_bytes =  0x0C000000 + MAC_LENTH
    addr = 0

    for j in range(SG_NUM):
      BUFFER_addr = data_in_base + addr
      next_desc_addr = 0
     
      desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
      addr = addr + MAC_LENTH
      descriptors.append(desc_words)

    return descriptors

def generate_ethdma_descriptors_for_MM2S(
    data_in_base=0x40000000,
    MAC_LENTH = 64,
    SG_NUM = 100
):

    descriptors = []


    block_size_bytes =  0x0C000000 + MAC_LENTH
    addr = 0

    for j in range(SG_NUM):
      BUFFER_addr = data_in_base + addr
      next_desc_addr = 0
     
      desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
      addr = addr + MAC_LENTH
      descriptors.append(desc_words)

    return descriptors


SGMEM_CDMA0_start    = 0xF4000000
SGMEM_CDMA1_start    = 0xF4200000

SGMEM_DMA0_BASE      = 0xF4400000
SGMEM_DMA1_BASE      = 0xF4600000
SGMEM_DMA2_BASE      = 0xF4800000
SGMEM_DMA3_BASE      = 0xF4A00000
SGMEM_DMA4_BASE      = 0xF4C00000
SGMEM_DMA5_BASE      = 0xF4E00000
SGMEM_DMA6_BASE      = 0xF5000000
SGMEM_DMA7_BASE      = 0xF5200000
SGMEM_ETHDMA0_BASE      = 0xF5400000
SGMEM_ETHDMA1_BASE      = 0xF5600000
SGMEM_ETHDMA2_BASE      = 0xF5800000
SGMEM_ETHDMA3_BASE      = 0xF5A00000
SGMEM_ETHDMA4_BASE      = 0xF5C00000




DMA0_config          = 0xFF000000
DMA1_config          = 0xFF000400
DMA2_config          = 0xFF000800
DMA3_config          = 0xFF000C00
DMA4_config          = 0xFF001000
DMA5_config          = 0xFF001400
DMA6_config          = 0xFF001800
DMA7_config          = 0xFF001C00

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

MPU_REG          = 0xFF005000
URAT             = 0xFF006000

MAC_START  = DDR0_START


DATA_START = MAC_START + 64


def main00(mac_lenth = 20,mac_onece = 110):
    MAC_LENTH  = mac_lenth * 64
    MAC_ONECE = mac_onece
    MAC_END    = DDR0_START + mac_lenth * (MAC_ONECE-1) * 64
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    MAIN_TXT_name = 'MAIN'
    txt_dir = os.path.join(script_dir,"txt")

    MAIN_TXT_file = os.path.join(txt_dir, f"{MAIN_TXT_name}.txt")

    descriptors_ethdma_S2MM = generate_ethdma_descriptors_for_S2MM(
        
        data_in_base=DDR0_START,
        MAC_LENTH = MAC_LENTH,
        SG_NUM = MAC_ONECE            #每次批处理的帧数
    )
    
    descriptors_ethdma_MM2S = generate_ethdma_descriptors_for_MM2S(
      
        data_in_base=DDR0_START,
        MAC_LENTH = MAC_LENTH,
        SG_NUM = MAC_ONECE
    )



    ETH3_S2MM_len = 64*len(descriptors_ethdma_S2MM)

    ETH_MM2S_len = 64*len(descriptors_ethdma_MM2S)

    ETH_LEN = max(ETH3_S2MM_len, ETH_MM2S_len)

    ethdma3_S2MM_sg_data = link_descriptors_in_memory(descriptors_ethdma_S2MM, base_addr=SGMEM_ETHDMA3_BASE, desc_size=64)
    ethdma_MM2S_sg_data =  link_SAME(descriptors_ethdma_MM2S, base_addr=0, desc_size=64)

    ethdma_name = 'eth_tile_sg'
    ethdma_file = os.path.join(txt_dir, f"{ethdma_name}.txt")
    ALLDATA= ethdma3_S2MM_sg_data + ethdma_MM2S_sg_data 
    

    write_txt_file(ALLDATA, ethdma_file)
    hex_to_bin.ETH_TILE_sg()
    

    with open(MAIN_TXT_file, 'w') as f0:

        f0.write("; --- SEGMENT 1 ---" +"\n")   
        f0.write("x1 0x"  + f"{(CDMA0_config        & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(CDMA1_config        & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001001          & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000          & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(SGMEM_CDMA0_start                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(SGMEM_ETHDMA3_BASE                              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(ETH_LEN                                         & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(SGMEM_CDMA0_start + ETH3_S2MM_len               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x9 0x"  + f"{(SGMEM_CDMA1_start                               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x10 0x"  + f"{(ethdma3_config                                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x11 0x"  + f"{(SGMEM_ETHDMA3_BASE                             & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x12 0x"  + f"{((SGMEM_ETHDMA3_BASE + ETH3_S2MM_len - 64)      & 0xFFFFFFFF):08x}"+"\n")

        f0.write("; --- SEGMENT 2 ---" +"\n")
        f0.write("x11 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x12 0x"   + f"{(0                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x13 0x"   + f"{(0xFF                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x14 0x"   + f"{(0xF4                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x15 0x"   + f"{(0xF0                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x16 0x"   + f"{(0xF1                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x17 0x"   + f"{(0xF2                   & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x18 0x"   + f"{(0xCCA41704             & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x19 0x"   + f"{(0x0                    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x20 0x"  + f"{(DDR0_START             & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x21 0x"  + f"{(DATA_START             & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x22 0x"  + f"{(MAC_LENTH              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x23 0x"  + f"{(MAC_END                & 0xFFFFFFFF):08x}"+"\n")


        
        f0.write("; --- SEGMENT 3 ---" +"\n")
        f0.write("x1 0x"  + f"{(CDMA0_config                    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma4_config                  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001001                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(SGMEM_CDMA1_start               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(SGMEM_ETHDMA4_BASE              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(0x40                            & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n") 

        f0.write("; --- SEGMENT 4 ---" +"\n")
        f0.write("x1 0x"  + f"{(CDMA0_config                    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma0_config                  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001001                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(SGMEM_CDMA1_start               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(SGMEM_ETHDMA0_BASE              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(0x40                            & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n") 

        f0.write("; --- SEGMENT 5 ---" +"\n")
        f0.write("x1 0x"  + f"{(CDMA0_config                    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma1_config                  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001001                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(SGMEM_CDMA1_start               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(SGMEM_ETHDMA1_BASE              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(0x40                            & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n") 

        f0.write("; --- SEGMENT 6 ---" +"\n")
        f0.write("x1 0x"  + f"{(CDMA0_config                    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma2_config                  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001001                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000                      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(SGMEM_CDMA1_start               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(SGMEM_ETHDMA2_BASE              & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(0x40                            & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(0                               & 0xFFFFFFFF):08x}"+"\n") 

        f0.write("; --- SEGMENT 7 ---" +"\n")
        f0.write("x1 0x"  + f"{(1     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(2     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(3     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(4     & 0xFFFFFFFF):08x}"+"\n")

        f0.write("; --- SEGMENT 8 ---" +"\n")
        f0.write("x1 0x"  + f"{(CDMA0_config    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001000      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(0               & 0xFFFFFFFF):08x}"+"\n")

        
def main(mac_lenth = 20,mac_onece = 110):
    main00(mac_lenth,mac_onece)
    asm_generate.main()
    translator.main()

    tablemd.main()

if __name__ == "__main__":
    main(mac_lenth = 20,mac_onece = 110)
    



      
