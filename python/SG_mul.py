import os
import config

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
    length_bytes,
    APP0
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
    word8 = APP0 #APP0
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


def generate_cdma0_descriptors_for_matrix_A_IN(
    A_rows=64,
    A_cols=128,
    block_width=16,
    Global_0_base=0x00010000,
    Shared_Men0_base=0x80000000,
    element_size=2
):
    """
    Generate a list of SG descriptors for matrix A (8 words per descriptor),
    Suppose A is stored in rows, A_rows x A_cols in size, and block_width rows (entire columns) are moved at a time.
    The destination address is switched back and forth between dest0/dest1.
    Return value: descriptors_A, where descriptors_A is [ [word0,word1,...], [word0,word1,...], ... ]
    """
    descriptors = []
    # There are (A_rows / block_width) sub-blocks in total (not taking into account the divisible remainder)
    Anum_blocks = A_rows // block_width

    # Each subblock: block_width rows, A_cols elements per row, each element = 4 bytes = > block_size_bytes
    block_size_bytes = block_width * A_cols * element_size

    for i in range(Anum_blocks):
       
        # SA：BASE + i* (block_width*A_cols*4)
        src_addr = Global_0_base + i * block_size_bytes
        #print(f'{src_addr:08x}')
        # DA 0x80000000 / 0x90000000 
        dst_addr = Shared_Men0_base + i * block_size_bytes
        # Set next_desc_addr to 0 first, and then the main tone function will handle the links uniformly
        next_desc_addr = 0
        #if (i != 0):
        desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
        descriptors.append(desc_words)

    return descriptors

def generate_cdma1_descriptors_for_matrix_B_IN(
    B_rows=128,
    B_cols=64,
    block_width=16,
    Global_1_base=0x40001000,
    Shared_Men1_base=0x90000000,
    element_size=2
):

    descriptors = []
    Bnum_blocks = B_cols // block_width

    block_size_bytes = block_width * B_rows * element_size

    for i in range(Bnum_blocks):
       
        src_addr = Global_1_base + i * block_size_bytes
        dst_addr = Shared_Men1_base + i * block_size_bytes
        next_desc_addr = 0
        desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
        descriptors.append(desc_words)

    return descriptors

def generate_cdma0_descriptors_for_matrix_A_OUT(
    A_rows=64,
    A_cols=128,
    B_cols=64,
    block_width=16,
    Global_0_base=0x24000000,
    Shared_Men0_base=0x84000000,
    Shared_Men2_base=0x94000000,
    element_size=4
):

    descriptors = []

    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    block_size_bytes = block_width * block_width * element_size
    src_addr_add = 0

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
          A = i*Bnum_blocks + j

          dst_addr = Global_0_base + A * block_size_bytes
          src_addr = Shared_Men0_base if (A % 2 == 0) else Shared_Men2_base
          src_addr = src_addr + src_addr_add
          next_desc_addr = 0
          
          desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
          descriptors.append(desc_words)
          if(A % 2 == 1):
                src_addr_add = src_addr_add + 512

    return descriptors

def generate_cdma1_descriptors_for_matrix_B_OUT(
    A_rows=64,
    B_rows=128,
    B_cols=64,
    block_width=16,
    Global_1_base=0x68000000,
    Shared_Men1_base=0x8c000000,
    Shared_Men3_base=0x9c000000,
    element_size=4
):
    
    descriptors = []
    Bnum_blocks = B_cols // block_width
    Anum_blocks = A_rows // block_width

    block_size_bytes = B_rows * block_width * element_size
    src_addr_add = 0

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
            B = i*Bnum_blocks + j
            dst_addr = Global_1_base + B * block_size_bytes

            src_addr = Shared_Men1_base if (B % 2 == 0) else Shared_Men3_base
            src_addr = src_addr + src_addr_add
            next_desc_addr = 0
            desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
            descriptors.append(desc_words)
            if (B % 2 == 1):
                src_addr_add = src_addr_add + 512

    return descriptors


def generate_dma0_descriptors_for_MM2S(
    A_rows=64,
    A_B=128,
    B_cols=64,
    block_width=16,
    Shared_Men0_base=0x80000000,
    element_size=2,
    APP0 =0
):
    
    descriptors = []
    # There are (A_rows / block_width) sub-blocks in total (excluding the divisible remainder)
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    # Each subblock: block_width rows, A_cols elements per row, each element = 4 bytes = > block_size_bytes
    block_size_bytes = block_width * A_B * element_size + 0x0C000000
    block_size = block_width * A_B * element_size

    for i in range(Anum_blocks):
        BUFFER_addr = Shared_Men0_base + (i * block_size)
        for j in range(Bnum_blocks):
          next_desc_addr = 0
          '''
          if(i*Bnum_blocks + j == 0):
          #if((i*Bnum_blocks + j)%16 == 0):
              block_size_bytes = block_width * A_B * element_size + 0x08000000
          #elif((i*Bnum_blocks + j)%16 == 15):  
          elif(i*Bnum_blocks + j == Anum_blocks *Bnum_blocks - 1):
              block_size_bytes = block_width * A_B * element_size + 0x04000000
          else:
              block_size_bytes = block_width * A_B * element_size
          '''
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes , APP0)
          descriptors.append(desc_words)

    return descriptors

def generate_dma1_descriptors_for_MM2S(
    A_rows=64,
    A_B=128,
    B_cols=64,
    block_width=16,
    Shared_Men1_base=0x88000000,
    element_size=2,
    APP0 = 0
):
    
    descriptors = []
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    block_size_bytes = block_width * A_B * element_size + 0x0C000000
    block_size = block_width * A_B * element_size

    for i in range(Anum_blocks):
        
        for j in range(Bnum_blocks):
          BUFFER_addr = Shared_Men1_base + (j * block_size) 
          next_desc_addr = 0
          '''
          if(i*Bnum_blocks + j == 0):
          #if((i*Bnum_blocks + j)%16 == 0):
              block_size_bytes = block_width * A_B * element_size + 0x08000000
          #elif((i*Bnum_blocks + j)%16 == 15):  
          elif(i*Bnum_blocks + j == Anum_blocks *Bnum_blocks - 1):
              block_size_bytes = block_width * A_B * element_size + 0x04000000
          else:
              block_size_bytes = block_width * A_B * element_size
          '''
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes, APP0)
          descriptors.append(desc_words)

    return descriptors

def generate_dma0_descriptors_for_S2MM(
    A_rows=64,
    B_cols=64,
    block_width=16,
    Shared_Men2_base=0x90000000,
    element_size=2,
    APP0 = 0
):

    descriptors = []
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    block_size_bytes = block_width * block_width * element_size + 0x0C000000
    addr = 0

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
          BUFFER_addr = Shared_Men2_base + addr
          next_desc_addr = 0
          '''
          if((i*Bnum_blocks + j)%16 == 0):
              block_size_bytes = block_width * block_width * element_size + 0x08000000
          #elif((i*Bnum_blocks + j)%16 == 15):  
          elif(i*Bnum_blocks + j == Anum_blocks *Bnum_blocks - 1):
              block_size_bytes = block_width * block_width * element_size + 0x04000000
          else:
              block_size_bytes = block_width * block_width * element_size
          '''    
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes, APP0)
          addr = addr + 512
          descriptors.append(desc_words)

    return descriptors

def generate_dma1_descriptors_for_S2MM(
    A_rows=64,
    B_cols=64,
    block_width=16,
    Shared_Men3_base=0x98000000,
    element_size=2,
    APP0 = 0
):

    descriptors = []
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    block_size_bytes = block_width * block_width * element_size + 0x0C000000
    addr = 0

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
          A = i*Bnum_blocks + j
          BUFFER_addr = Shared_Men3_base + addr
          next_desc_addr = 0
          '''
          if((i*Bnum_blocks + j)%16 == 0):
              block_size_bytes = block_width * block_width * element_size + 0x08000000
          #elif((i*Bnum_blocks + j)%16 == 15):  
          elif(i*Bnum_blocks + j == Anum_blocks *Bnum_blocks - 1):
              block_size_bytes = block_width * block_width * element_size + 0x04000000
          else:
              block_size_bytes = block_width * block_width * element_size
          '''
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes, APP0)
          addr = addr + 512
          descriptors.append(desc_words)

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

def op_DMA(A__ROWS=16,A__COLS=16,B__ROWS=16,B__COLS=16, block_width = 16, element_size = 2, APP0 = 0,
       data0_in = 0x80000000,data1_in = 0x80400000,data0_out = 0x90000000,data1_out = 0x90400000,
       DMA0_REG_base= 0xC0000000,DMA1_REG_base= 0xC0000400):

    A_ROWS = A__ROWS
    A_COLS = A__COLS
    B_ROWS = B__ROWS
    B_COLS = B__COLS

    global ALL
    global sg_start
    global GM1_setid

    descriptors_DMA0_S2MM = generate_dma0_descriptors_for_S2MM(
        A_rows=A_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Shared_Men2_base=data0_out,
        element_size=element_size,
        APP0 = APP0
    )
    descriptors_DMA1_S2MM = generate_dma1_descriptors_for_S2MM(
        A_rows=A_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Shared_Men3_base=data1_out,
        element_size=element_size,
        APP0 = APP0
    )
    descriptors_DMA0_MM2S = generate_dma0_descriptors_for_MM2S(
        A_rows=A_ROWS,
        A_B = B_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Shared_Men0_base=data0_in,
        element_size=element_size,
        APP0 = APP0
    )
    descriptors_DMA1_MM2S = generate_dma1_descriptors_for_MM2S(
        A_rows=A_ROWS,
        A_B = B_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Shared_Men1_base=data1_in,
        element_size=element_size,
        APP0 = APP0
    )
    
    dma0_S2MM =  sg_start
    print(f'{sg_start:08x}')
    dma0_MM2S =  dma0_S2MM + len(descriptors_DMA0_S2MM) * 64
    dma1_S2MM =  dma0_MM2S + len(descriptors_DMA0_MM2S) * 64
    dma1_MM2S =  dma1_S2MM + len(descriptors_DMA1_S2MM) * 64

    dma0_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA0_MM2S, base_addr=dma0_MM2S, desc_size=64)
    dma1_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA1_MM2S, base_addr=dma1_MM2S, desc_size=64)
    dma0_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA0_S2MM, base_addr=dma0_S2MM, desc_size=64)
    dma1_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA1_S2MM, base_addr=dma1_S2MM, desc_size=64)

    ALL = ALL + dma0_S2MM_sg_data + dma0_MM2S_sg_data + dma1_S2MM_sg_data + dma1_MM2S_sg_data

    script_dir = os.path.dirname(os.path.abspath(__file__))

    dma0_MM2S_name = 'dma0_MM2S_sg'
    dma1_MM2S_name = 'dma1_MM2S_sg'
    dma0_S2MM_name = 'dma0_S2MM_sg'
    dma1_S2MM_name = 'dma1_S2MM_sg'

    txt_dir = os.path.join(script_dir,"txt")

    dma0_MM2S_file = os.path.join(txt_dir, f"{dma0_MM2S_name}.txt")
    dma1_MM2S_file = os.path.join(txt_dir, f"{dma1_MM2S_name}.txt")
    dma0_S2MM_file = os.path.join(txt_dir, f"{dma0_S2MM_name}.txt")
    dma1_S2MM_file = os.path.join(txt_dir, f"{dma1_S2MM_name}.txt")

    global DMA_ID 
    if DMA_ID == 1:
        write_txt_file(dma0_MM2S_sg_data, dma0_MM2S_file)
        write_txt_file(dma1_MM2S_sg_data, dma1_MM2S_file)
        write_txt_file(dma0_S2MM_sg_data, dma0_S2MM_file)
        write_txt_file(dma1_S2MM_sg_data, dma1_S2MM_file)
    else:
        write_txt_file_A(dma0_MM2S_sg_data, dma0_MM2S_file)
        write_txt_file_A(dma1_MM2S_sg_data, dma1_MM2S_file)
        write_txt_file_A(dma0_S2MM_sg_data, dma0_S2MM_file)
        write_txt_file_A(dma1_S2MM_sg_data, dma1_S2MM_file)
    if GM1_setid == 1:
        mood = 'w'
    else:
        mood = 'a'
    DMA_ID = DMA_ID + 1
    print(" DMA0_MM2S descriptors count:", len(descriptors_DMA0_MM2S))
    print(" DMA1_MM2S descriptors count:", len(descriptors_DMA1_MM2S))
    print(" DMA0_S2MM descriptors count:", len(descriptors_DMA0_S2MM))
    print(" DMA1_S2MM descriptors count:", len(descriptors_DMA1_S2MM))

    DMA0_S2MM_len = 64*len(descriptors_DMA0_S2MM)
    DMA0_MM2S_len = 64*len(descriptors_DMA0_MM2S)
    DMA1_S2MM_len = 64*len(descriptors_DMA1_S2MM)
    DMA1_MM2S_len = 64*len(descriptors_DMA1_MM2S)
    DMA0_len = 64*(len(descriptors_DMA0_MM2S)+len(descriptors_DMA0_S2MM))
    DMA1_len = 64*(len(descriptors_DMA1_MM2S)+len(descriptors_DMA1_S2MM))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    name1 = "GM1"
    txt_dir = os.path.join(script_dir,"txt")

    GM1_file1 = os.path.join(txt_dir, f"{name1}.txt")

    GM1_LOOP_file1 = os.path.join(txt_dir, f"{name1}LOOP.txt")
    

    with open(GM1_LOOP_file1, mood) as f1_L:
        f1_L.write(f"; --- SEGMENT {GM1_setid} ---" +"\n") #CDMA
        #CDMA_X1 = cdma(A__ROWS,A__COLS)
        f1_L.write("x1 0x" + f"{(0 & 0xFFFFFFFF):08x}"+"\n")


    with open(GM1_file1, mood) as f1:
        DMA0_S2MM_START =  sg_start
        DMA0_MM2S_START =  DMA0_S2MM_START + DMA0_S2MM_len
        DMA1_S2MM_START =  DMA0_MM2S_START + DMA0_MM2S_len
        DMA1_MM2S_START =  DMA1_S2MM_START + DMA1_S2MM_len
        f1.write(f"; --- SEGMENT {GM1_setid} ---" +"\n")
        f1.write("x1 0x" + f"{(DMA0_REG_base & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(DMA1_REG_base & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(DMA0_S2MM_START & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(DMA1_S2MM_START & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x1001 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{(DMA0_MM2S_START & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{(DMA1_MM2S_START & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x9 0x" +  f"{((DMA0_MM2S_START-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x10 0x" + f"{((DMA1_MM2S_START-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x11 0x" + f"{((DMA0_MM2S_START+DMA0_MM2S_len-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x12 0x" + f"{((DMA1_MM2S_START+DMA1_MM2S_len-64) & 0xFFFFFFFF):08x}"+"\n")

    sg_start =   sg_start + DMA0_len + DMA1_len 

def op_CDMA(A_ROWS=16,A_COLS=16,B_ROWS=16,B_COLS=16, block_width = 16, element_size = 2,Global0_base = 0x00010000,
            Global1_base = 0x40001000,CDMA0_reg_base= 0xC0000800,CDMA1_reg_base= 0xC0000840,DATA0 = 0x80000000,DATA1 = 0x88000000):

    global ALL
    global sg_start
    global GM1_setid

    descriptors_A_IN = generate_cdma0_descriptors_for_matrix_A_IN(
        A_rows=A_ROWS,
        A_cols=A_COLS,
        block_width=block_width,
        Global_0_base=Global0_base,
        Shared_Men0_base=DATA0,
        element_size=element_size
    )
    descriptors_B_IN = generate_cdma1_descriptors_for_matrix_B_IN(
        B_rows=B_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Global_1_base=Global1_base,
        Shared_Men1_base=DATA1,
        element_size=element_size
    )

    descriptors_A = descriptors_A_IN
    descriptors_B = descriptors_B_IN

    cdma0_base = sg_start
    cdma1_base = cdma0_base + len(descriptors_A) * 64
    CDMA0_len  = 64*len(descriptors_A)
    CDMA1_len  = 64*len(descriptors_B)

    cdma0_sg_data = link_descriptors_in_memory(descriptors_A, base_addr=cdma0_base, desc_size=64)
    cdma1_sg_data = link_descriptors_in_memory(descriptors_B, base_addr=cdma1_base, desc_size=64)

    ALL = ALL + cdma0_sg_data + cdma1_sg_data 

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cdma0_name = 'cdma0_sg'
    cdma1_name = 'cdma1_sg'

    txt_dir = os.path.join(script_dir,"txt")

    cdma0_file = os.path.join(txt_dir, f"{cdma0_name}.txt")
    cdma1_file = os.path.join(txt_dir, f"{cdma1_name}.txt")


    if GM1_setid == 1:
        write_txt_file(cdma0_sg_data, cdma0_file)
        write_txt_file(cdma1_sg_data, cdma1_file)
        mood = 'w'   
    else:
        write_txt_file_A(cdma0_sg_data, cdma0_file)
        write_txt_file_A(cdma1_sg_data, cdma1_file)  
        mood = 'a'

    print(" CDMA0 descriptors count:", len(descriptors_A))
    print(" CDMA1 descriptors count:", len(descriptors_B))

    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name1 = "GM1"
    txt_dir = os.path.join(script_dir,"txt")

    GM1_file1 = os.path.join(txt_dir, f"{name1}.txt")

    GM1_LOOP_file1 = os.path.join(txt_dir, f"{name1}LOOP.txt")

    with open(GM1_file1, mood) as f1:
        CDMA0_START = sg_start
        CDMA1_START = CDMA0_START + CDMA0_len
        f1.write(f"; --- SEGMENT {GM1_setid} ---" +"\n")
        f1.write("x1 0x" + f"{(CDMA0_reg_base                & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(CDMA1_reg_base                & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0x00001008                    & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0x00001000                    & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(CDMA0_START                   & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(CDMA1_START                   & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((CDMA1_START-64)              & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((CDMA1_START + CDMA1_len -64) & 0xFFFFFFFF):08x}"+"\n")

    def cdma(row,col):
        cd_x1 = ((row*col*2)/60)/300 
        cd_x1 = int(cd_x1)
        return cd_x1
    
    with open(GM1_LOOP_file1, mood) as f1_L:
        f1_L.write(f"; --- SEGMENT {GM1_setid} ---" +"\n") #CDMA
        CDMA_X1 = cdma(A_ROWS,A_COLS)
        f1_L.write("x1 0x" + f"{(CDMA_X1 & 0xFFFFFFFF):08x}"+"\n")

    sg_start =   sg_start + CDMA0_len + CDMA1_len 

sg_start     = 0xA0000000
GM1_setid    = 1
ALL          = []
DMA_ID       = 1

def main(AROWS = 32,AB =32,BCOLS = 32,START = 0x00000100, block_width = 16, element_size = 2, APP0 = 0):
    A_ROWS = AROWS
    A_B = AB
    B_COLS = BCOLS
    A_DATA_START = START
    global ALL
    global sg_start
    
    print("Number of SG descriptors: ",int(A_DATA_START/64))
    
    global GM1_setid
    
    
    #GM1_setid = GM1_setid + 1


    op_DMA(A__ROWS = A_ROWS,A__COLS = A_B,B__ROWS = A_B,B__COLS = B_COLS,
       block_width = block_width, element_size = element_size, APP0 = APP0)
    

    sg_lenth = int(sg_start-int(0xA0000000))
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name0 = "ROM"
    txt_dir = os.path.join(script_dir,"txt")
    ROM_file0 = os.path.join(txt_dir, f"{name0}.txt")
    ROM_LOOP_file0 = os.path.join(txt_dir, f"{name0}LOOP.txt")

    all_file = os.path.join(txt_dir, f"allsg.txt")

    allSGdescriptors = int(A_DATA_START/64)
    if(allSGdescriptors >= int(sg_lenth/64)):
        print("There is no need to add space to the SG descriptor")
    else:
        print("Need to add space to the SG descriptor")

    #print(f'{sg_start:08x}')
    descriptorss = []
    alllen = int(int(A_DATA_START/64) - int(sg_lenth/64))
    #print(int(A_DATA_START/64))
    #print(int(sg_lenth/64))
    for i in range(alllen):
        A = 0
        word = make_sg_dma_descriptor(A,A,A,A)
        descriptorss.append(word)
    deadata = flat(descriptorss)
    AL = ALL + deadata
    write_txt_file(AL , all_file)

    def descriptors(len):
        ds_x1 = (len/45) 
        ds_x1 = int(ds_x1)
        return ds_x1
    
    
    with open(ROM_file0, 'w') as f0:
        f0.write("; --- SEGMENT 1 ---" +"\n")
        f0.write("x1 0x" + f"{(0xFF004400  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x" + f"{(0xFF004440  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x" + f"{(0x00001000  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x" + f"{(0x00001000  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x" + f"{(0x00000000  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x" + f"{(0xA0000000  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x" + f"{(0x40000000  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x" + f"{(0xB0001000  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x9 0x" + f"{(sg_lenth    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x10 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")


    with open(ROM_LOOP_file0, 'w') as f0_L:
        f0_L.write("; --- SEGMENT 1 ---" +"\n")
        ds_x1 = descriptors(sg_lenth)
        f0_L.write("x1 0x" + f"{(ds_x1+10 & 0xFFFFFFFF):08x}"+"\n")

if __name__ == "__main__":
    main(AROWS = 16,AB =16,BCOLS = 16, block_width = 16, element_size = 2, APP0 = 0 )



      
