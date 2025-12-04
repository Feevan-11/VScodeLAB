import os

def make_sg_cdma_descriptor(
    next_desc_addr,
    src_addr,
    dst_addr,
    length_bytes
):
    """
    Construct an AXI CDMA SG descriptor (8 x 32-bit) and return a list of length 8, each element is int (32-bit).
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
    # Word2: SRCADDR
    word2 = src_addr & 0xFFFFFFFF
    # Word3: 0
    word3 = 0
    # Word4: DSTADDR
    word4 = dst_addr & 0xFFFFFFFF
    # Word5: 0
    word5 = 0
    # Word6: [25:0] = length_bytes, [31:26] = 0
    word6 = (length_bytes & 0x03FFFFFF)
    # Word7: 0 (status)
    word7 = 0
    word8 = 0
    word9 = 0
    word10 = 0
    word11 = 0
    word12 = 0
    word13 = 0
    word14 = 0
    word15 = 0


    return [word0, word1, word2,  word3,  word4,  word5,  word6,  word7,
            word8, word9, word10, word11, word12, word13, word14, word15]

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
    word8 = 0
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

def generate_dma0_descriptors_for_MM2S(    
    base_addr=0x00000000 
):

    descriptors = []

    block_size_bytes = 0x0C000000 + 64*8
    addr = 64*8
    BUFFER_addr = base_addr 

    for i in range(2):       
        next_desc_addr = 0
        desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
        descriptors.append(desc_words)
        BUFFER_addr = BUFFER_addr + addr
    
    return descriptors

def generate_dma1_descriptors_for_MM2S(    
    base_addr=0x00000000 
):

    descriptors = []

    block_size_bytes = 0x0C000000 + 64*8
    addr = 64*8
    BUFFER_addr = base_addr 

    for i in range(2):       
        next_desc_addr = 0
        desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
        descriptors.append(desc_words)
        BUFFER_addr = BUFFER_addr + addr
    
    return descriptors


def generate_dma0_descriptors_for_S2MM(    
        base_addr=0x00000000 
):

    descriptors = []

    block_size_bytes = 0x0C000000 + 64*8
    addr = 64*8
    BUFFER_addr = base_addr 

    for i in range(2):       
        next_desc_addr = 0
        desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
        descriptors.append(desc_words)
        BUFFER_addr = BUFFER_addr + addr

    return descriptors

def generate_dma1_descriptors_for_S2MM(
    base_addr=0x00000000 
):

    descriptors = []

    block_size_bytes = 0x0C000000 + 64*8
    addr = 64*8
    BUFFER_addr = base_addr 

    for i in range(2):       
        next_desc_addr = 0
        desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
        descriptors.append(desc_words)
        BUFFER_addr = BUFFER_addr + addr

    return descriptors

def link_descriptors_in_memory(descriptor_list, base_addr=0x00000000, desc_size=64):
    """
    Given a set of descriptors (each of which is 16 words), we imagine that they are sequentially stored in memory, starting with base_addr,
    Each descriptor is 64 bytes in size (16 words × 4 bytes). This function is updated sequentially
    Word0 for each descriptor so that it points to the next descriptor address (except for the last one = 0).
    Finally, a string of 32-bit words in the form of "flattened" is returned (in descriptive order).
    """

    flattened = []  # Stores the final sequentially expanded 32-bit word

    for i in range(len(descriptor_list)):

        # Calculate the starting physical address of the next descriptor
        if i < len(descriptor_list) - 1:
            next_desc_addr = base_addr + (i + 1) * desc_size
        else:
            next_desc_addr = base_addr

        # Update Word0 for the current descriptor
        words = descriptor_list[i]
        # Word0 = bits[31:6] = next_desc_addr >> 6
        #w0_rest = (next_desc_addr<<6) & 0xFFFFFFC0
        words[0] = next_desc_addr

        # Flatten the updated 16 word into flattened
        flattened.extend(words)

    return flattened

def flat(descriptor_list):
    flattened = []  # Stores the final sequentially expanded 32-bit word

    for i in range(len(descriptor_list)):
        words = descriptor_list[i]
        flattened.extend(words)

    return flattened

def op(A__ROWS=16,A__COLS=16,B__ROWS=16,B__COLS=16):

    A_ROWS = A__ROWS
    A_COLS = A__COLS
    B_ROWS = B__ROWS
    B_COLS = B__COLS

    descriptors_DMA0_S2MM = generate_dma0_descriptors_for_S2MM(
        base_addr=0x00001200

    )
    descriptors_DMA1_S2MM = generate_dma1_descriptors_for_S2MM(
        base_addr=0x00001200

    )
    descriptors_DMA0_MM2S = generate_dma0_descriptors_for_MM2S(
        base_addr=0x00000000

    )
    descriptors_DMA1_MM2S = generate_dma1_descriptors_for_MM2S(
        base_addr=0x00000000
    )

    # 2) Create an In-Memory Linear Placement layout for each of the two descriptor lists, and point Word0 to the next descriptor
    # Here we assume that the descriptor for CDMA0 starts at 0x00000000 and the descriptor for CDMA1 starts with 0x00100000 (example)

    dma0_S2MM =  0x00000000
    dma1_S2MM =  0x00000000
    ADD0 =  len(descriptors_DMA0_S2MM) * 64
    ADD1 =  len(descriptors_DMA1_S2MM) * 64
    dma0_MM2S =  dma0_S2MM + ADD0
    dma1_MM2S =  dma1_S2MM + ADD1

    dma0_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA0_MM2S, base_addr=dma0_MM2S, desc_size=64)
    dma1_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA1_MM2S, base_addr=dma1_MM2S, desc_size=64)
    dma0_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA0_S2MM, base_addr=dma0_S2MM, desc_size=64)
    dma1_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA1_S2MM, base_addr=dma1_S2MM, desc_size=64)

    dma0_data =   dma0_S2MM_sg_data + dma0_MM2S_sg_data
    dma1_data =   dma1_S2MM_sg_data + dma1_MM2S_sg_data 

    script_dir = os.path.dirname(os.path.abspath(__file__))

    dma0_MM2S_name = 'dma0_test_sg'
    dma1_MM2S_name = 'dma1_test_sg'


    txt_dir = os.path.join(script_dir,"txt")


    dma0_MM2S_file = os.path.join(txt_dir, f"{dma0_MM2S_name}.txt")
    dma1_MM2S_file = os.path.join(txt_dir, f"{dma1_MM2S_name}.txt")

    all_file = os.path.join(txt_dir, f"allsg.txt")

    write_txt_file(dma0_data, dma0_MM2S_file)
    write_txt_file(dma1_data, dma1_MM2S_file)

    

    print(" DMA0_MM2S descriptors count:", len(descriptors_DMA0_MM2S))
    print(" DMA1_MM2S descriptors count:", len(descriptors_DMA1_MM2S))
    print(" DMA0_S2MM descriptors count:", len(descriptors_DMA0_S2MM))
    print(" DMA1_S2MM descriptors count:", len(descriptors_DMA1_S2MM))


    DMA0_S2MM_len = 64*len(descriptors_DMA0_S2MM)
    DMA0_MM2S_len = 64*len(descriptors_DMA0_MM2S)

    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    name1 = "test"
    txt_dir = os.path.join(script_dir,"txt")

    GM1_file1 = os.path.join(txt_dir, f"{name1}.txt")



    with open(GM1_file1, 'w') as f1:
        f1.write("; --- SEGMENT 1 ---" +"\n")
        f1.write("x1 0x" + f"{(0xFF006000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0x00000074 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0x00000065 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0x00000073 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x00000074 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00000020 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{(0x00000073 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{(0x00000075 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x9 0x" + f"{(0x00000063 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x10 0x" + f"{(0x00000063 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x11 0x" + f"{(0x00000065 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x12 0x" + f"{(0x00000065 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x13 0x" + f"{(0x00000064 & 0xFFFFFFFF):08x}"+"\n")



def main(AROWS = 32,BCOLS = 32):
    A_ROWS = AROWS
    B_COLS = BCOLS
    op(A__ROWS = A_ROWS,A__COLS = BCOLS,B__ROWS = AROWS,B__COLS = B_COLS)

if __name__ == "__main__":
    main(AROWS = 32,BCOLS = 32)
