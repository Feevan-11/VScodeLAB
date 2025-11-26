import  os
import  config
import  asm_generate
import  loop
import  translator
import  merge_mif_files



def make_sg_dma_descriptor(
    next_desc_addr,
    buffer_addr,
    length_bytes
):
    """
    Construct an AXI DMA SG descriptor (8 x 32-bit) and return a list of length 8, each element is int (32-bit).
    Field Layout:
      Word0 (0x00): [5:0]=0, [31:6] = next_desc_addr >> 6
      Word1 (0x04): 0
      Word2 (0x08): src_addr
      Word3 (0x0C): 0
      Word4 (0x10): dst_addr
      Word5 (0x14): 0
      Word6 (0x18): [25:0] = length_bytes, [31:26]=0
      Word7 (0x1C): 0  (status word initialize as 0)
    """
    # Word0: NEXTDESC (Align addresses in 64 bytes => bits[31:6] = next_desc_addr >> 6)
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
    Shared_Men3_base=0x98000000,
    MAC_LENTH = 64
):

    descriptors = []


    block_size_bytes =  0x0C000000 + MAC_LENTH
    addr = 0

    for j in range(1):
      BUFFER_addr = Shared_Men3_base + addr
      next_desc_addr = 0
     
      desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
      addr = addr + MAC_LENTH
      descriptors.append(desc_words)

    return descriptors

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

def link(descriptor_list, base_addr=0x00000000, desc_size=64):

    flattened = []  # Stores the final sequentially expanded 32-bit word

    for i in range(len(descriptor_list)):

        next_desc_addr = base_addr

        words = descriptor_list[i]
        words[0] = next_desc_addr

        # Flatten the updated 16 word into flattened
        flattened.extend(words)

    return flattened

#def flat(descriptor_list):
#    flattened = []  # Stores the final sequentially expanded 32-bit word
#
#    for i in range(len(descriptor_list)):
#        words = descriptor_list[i]
#        flattened.extend(words)
#
#    return flattened

SG_MEM0 = 0xFF000000

ethdma0_CONFIG_BASE    = 0xFF003C00
SGMEM_ethdma0_BASE     = 0xF5A00000

ethdma1_CONFIG_BASE    = 0xFF003400
SGMEM_ethdma1_BASE     = 0xF5600000

cdma0_CONFIG_BASE    = 0xFF004400
cdma1_CONFIG_BASE    = 0xFF004440


DDR0_START       = 0x40000000
DDR1_START       = 0x80000000

def main():



    descriptors_ethdma_S2MM = generate_ethdma_descriptors_for_S2MM(
        data_in_base=0x40000000,
        MAC_LENTH = 64,
        SG_NUM = 100
    )

    descriptors_ethdma1_S2MM = generate_ethdma_descriptors_for_S2MM(
        data_in_base=0x40000000,
        MAC_LENTH = 64,
        SG_NUM = 100
    )

    descriptors_ethdma_MM2S = generate_ethdma_descriptors_for_MM2S(
        data_in_base=DDR1_START,
        MAC_LENTH = 64,
        SG_NUM = 100
    )

    descriptors_ethdma0_MM2S = generate_ethdma_descriptors_for_MM2S(
        data_in_base=DDR1_START,
        MAC_LENTH = 64,
        SG_NUM = 100
    )

    
    
    ETH0_S2MM_len = 64*len(descriptors_ethdma_S2MM)

    ETH1_MM2S_len = 64*len(descriptors_ethdma_MM2S)

    ethdma0_S2MM_sg_data = link_descriptors_in_memory(descriptors_ethdma_S2MM, base_addr=SGMEM_ethdma0_BASE, desc_size=64)
    ethdma1_MM2S_sg_data = link_descriptors_in_memory(descriptors_ethdma_MM2S, base_addr=SGMEM_ethdma1_BASE + ETH0_S2MM_len, desc_size=64)

    ethdma1_S2MM_sg_data = link_descriptors_in_memory(descriptors_ethdma1_S2MM, base_addr=ETH0_S2MM_len + ETH1_MM2S_len+SGMEM_ethdma1_BASE, desc_size=64)
    ethdma0_MM2S_sg_data = link_descriptors_in_memory(descriptors_ethdma0_MM2S, base_addr=ETH0_S2MM_len + ETH1_MM2S_len+SGMEM_ethdma0_BASE + ETH0_S2MM_len, desc_size=64)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    ethdma0_S2MM_name = 'ethdma0_S2MM_sg'
    ethdma1_MM2S_name = 'ethdma1_MM2S_sg'
    ethdma_TXT_name = 'ETH_TEST'
    txt_dir = os.path.join(script_dir,"txt")

    ethdma0_S2MM_file = os.path.join(txt_dir, f"{ethdma0_S2MM_name}.txt")
    ethdma1_MM2S_file = os.path.join(txt_dir, f"{ethdma1_MM2S_name}.txt")
    ethdma_TXT_file = os.path.join(txt_dir, f"{ethdma_TXT_name}.txt")

    with open(ethdma_TXT_file, 'w') as f0:

        f0.write("; --- SEGMENT 1 ---" +"\n")
        f0.write("x1 0x"  + f"{(0xFF004400     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(0xFF004440     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001000         & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000         & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(0x40000000    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(SGMEM_ethdma0_BASE  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(256          & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(0x40000100     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x9 0x"  + f"{(SGMEM_ethdma1_BASE  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x10 0x" + f"{(256          & 0xFFFFFFFF):08x}"+"\n")
        f0.write("; --- SEGMENT 2 ---" +"\n")
        f0.write("x1 0x"  + f"{(ethdma0_CONFIG_BASE     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(ethdma1_CONFIG_BASE     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001001    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(SGMEM_ethdma0_BASE         & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{((SGMEM_ethdma0_BASE + ETH0_S2MM_len - 64)    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{((SGMEM_ethdma1_BASE + ETH0_S2MM_len)     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{((SGMEM_ethdma1_BASE + ETH0_S2MM_len + ETH1_MM2S_len - 64)      & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x15 0x"  + f"{( ETH0_S2MM_len + ETH1_MM2S_len+ SGMEM_ethdma1_BASE         & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x16 0x"  + f"{((ETH0_S2MM_len + ETH1_MM2S_len+ SGMEM_ethdma1_BASE + ETH0_S2MM_len - 64)    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x17 0x"  + f"{((ETH0_S2MM_len + ETH1_MM2S_len+ SGMEM_ethdma0_BASE + ETH0_S2MM_len)     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x18 0x"  + f"{((ETH0_S2MM_len + ETH1_MM2S_len+ SGMEM_ethdma0_BASE + ETH0_S2MM_len + ETH1_MM2S_len - 64)      & 0xFFFFFFFF):08x}"+"\n")
        
       #f0.write("; --- SEGMENT 3 ---" +"\n")
       #f0.write("x1 0x"  + f"{(0     & 0xFFFFFFFF):08x}"+"\n")
       #f0.write("x2 0x"  + f"{(0     & 0xFFFFFFFF):08x}"+"\n")
       #f0.write("x3 0x"  + f"{(0     & 0xFFFFFFFF):08x}"+"\n")
       #f0.write("x4 0x"  + f"{(0     & 0xFFFFFFFF):08x}"+"\n")
       #f0.write("x5 0x"  + f"{(0     & 0xFFFFFFFF):08x}"+"\n")
       #f0.write("x6 0x"  + f"{(0     & 0xFFFFFFFF):08x}"+"\n")
       #f0.write("x7 0x"  + f"{(0x00000000     & 0xFFFFFFFF):08x}"+"\n")
       #f0.write("x8 0x"  + f"{((SGMEM_ethdma0_BASE + ETH0_S2MM_len - 64)     & 0xFFFFFFFF):08x}"+"\n")
    all_da = ethdma0_S2MM_sg_data + ethdma1_MM2S_sg_data + ethdma1_S2MM_sg_data + ethdma0_MM2S_sg_data
    all_da = all_da + all_da
    write_txt_file(all_da, ethdma0_S2MM_file)
    write_txt_file(ethdma1_MM2S_sg_data, ethdma1_MM2S_file)


if __name__ == "__main__":
    main()



      
