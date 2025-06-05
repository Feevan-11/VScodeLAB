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


def generate_cdma0_descriptors_for_matrix_A_IN(
    A_B=64,
    block_width=16,
    Global_0_base=0x00010000,
    Shared_Men0_base=0x80000000,
    Shared_Men2_base=0x90000200,
    element_size=2
):
    """
    Generate a list of SG descriptors for matrix A (8 words per descriptor),
    Suppose A is stored in rows, A_rows x A_cols in size, and block_width rows (entire columns) are moved at a time.
    The destination address is switched back and forth between dest0/dest1.
    Return value: descriptors_A, where descriptors_A is [ [word0,word1,...], [word0,word1,...], ... ]
    """
    descriptors = []
    
    Anum_blocks = A_B // block_width

    block_size_bytes = block_width * A_B * element_size
    j = 0

    for i in range(2*Anum_blocks):
        if(i < (Anum_blocks)):
            src_addr = Global_0_base + i * block_size_bytes
            dst_addr = Shared_Men0_base + i * block_size_bytes
            next_desc_addr = 0
            desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
            descriptors.append(desc_words)
        else:
            src_addr = Global_0_base + i * block_size_bytes
            dst_addr = Shared_Men2_base + j * block_size_bytes
            next_desc_addr = 0
            desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
            descriptors.append(desc_words)
            j += 1
        if(i == (2*Anum_blocks-1)):
            src_addr += block_size_bytes
            dst_addr = 0x90000000
            block_size_bytes = 512
            desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
            descriptors.append(desc_words)
    return descriptors

def generate_cdma1_descriptors_for_matrix_B_IN(
    A_B=64,
    block_width=16,
    Global_1_base=0x40001000,
    Shared_Men1_base=0x88000000,
    Shared_Men3_base=0x98000000,
    element_size=2
):

    descriptors = []
    Bnum_blocks = A_B // block_width

    block_size_bytes = block_width * A_B * element_size

    for i in range(Bnum_blocks):
       
        src_addr = Global_1_base + i * block_size_bytes
        dst_addr = Shared_Men1_base + i * block_size_bytes
        next_desc_addr = 0
        desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
        descriptors.append(desc_words)
        if(i == (Bnum_blocks-1)):
            src_addr += block_size_bytes
            dst_addr = Shared_Men3_base
            block_size_bytes = 512
            desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
            descriptors.append(desc_words)

    return descriptors


def generate_dma0_descriptors_for_MM2S(
    A_B=64,
    block_width=16,
    Shared_Men0_base=0x80000000,
    element_size=2,
    row = True
):
    
    descriptors = []
    Anum_blocks = A_B // block_width
    Bnum_blocks = A_B // block_width

    # Each subblock: block_width rows, A_cols elements per row, each element = 4 bytes = > block_size_bytes
    block_size_bytes = block_width * A_B * element_size + 0x0C000000
    block_size = block_width * A_B * element_size
    if(row):
      for i in range(Anum_blocks):
        BUFFER_addr = Shared_Men0_base + (i * block_size)
        for j in range(Bnum_blocks):
          next_desc_addr = 0
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words)
    else:
      for i in range(Anum_blocks):
        
        for j in range(Bnum_blocks):
          BUFFER_addr = Shared_Men0_base + (j * block_size)
          next_desc_addr = 0
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words)
    return descriptors

def generate_dma1_descriptors_for_MM2S(
    A_B=64,
    block_width=16,
    Shared_Men1_base=0x88000000,
    element_size=2,
    row = True
):
    
    descriptors = []
    Anum_blocks = A_B // block_width
    Bnum_blocks = A_B // block_width

    # Each subblock: block_width rows, A_cols elements per row, each element = 4 bytes = > block_size_bytes
    block_size_bytes = block_width * A_B * element_size + 0x0C000000
    block_size = block_width * A_B * element_size
    if(row):
      
      for i in range(Anum_blocks):
        for j in range(Bnum_blocks):
          BUFFER_addr = Shared_Men1_base + (j * block_size)
          next_desc_addr = 0
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words)
    else:
      for i in range(Anum_blocks):
        BUFFER_addr = Shared_Men1_base + (i * block_size)
        for j in range(Bnum_blocks):
          next_desc_addr = 0
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words)
    return descriptors

def generate_dma0_ADD_for_MM2S(
    A_B=64,
    block_width=16,
    Shared_Men2_base=0x90000200,
    element_size=2,
    row = True
):
    
    descriptors = []
    # There are (rows / block_width) sub-blocks in total (excluding the divisible remainder)
    ROW_blocks = A_B // block_width
    COL_blocks = A_B // block_width

    # Each subblock: block_width rows, cols elements per row, each element = 4 bytes = > block_size_bytes
    block_size = block_width * block_width * element_size

    for i in range(ROW_blocks):
        
        for j in range(COL_blocks):
          
          A = i*COL_blocks + j
          BUFFER_addr = Shared_Men2_base + (A * block_size)
          eye_addr = 0x90000000
          next_desc_addr = 0

          block_size_bytes = block_width * block_width * element_size + 0x08000000
          desc_words0 = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words0)  

          block_size_bytes = block_width * block_width * element_size + 0x04000000
          desc_words1 = make_sg_dma_descriptor(next_desc_addr, eye_addr, block_size_bytes)
          descriptors.append(desc_words1)

    return descriptors

def generate_dma1_ADD_for_MM2S(
    A_B=64,
    block_width=16,
    Shared_Men3_base=0x98000200,
    element_size=2,
    row = True
):
    
    descriptors = []
    ROW_blocks = A_B // block_width
    COL_blocks = A_B // block_width

    block_size = block_width * block_width * element_size

    for i in range(ROW_blocks):
        
        for j in range(COL_blocks):
          
          A = i*COL_blocks + j
          BUFFER_addr = Shared_Men3_base + (A * block_size)
          eye_addr = 0x98000000
          next_desc_addr = 0
          
          block_size_bytes = block_width * block_width * element_size + 0x08000000
          desc_words0 = make_sg_dma_descriptor(next_desc_addr, eye_addr, block_size_bytes)
          descriptors.append(desc_words0)  

          block_size_bytes = block_width * block_width * element_size + 0x04000000
          desc_words1 = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words1)

    return descriptors


def generate_dma0_descriptors_for_S2MM(
    A_B=64,
    block_width=16,
    Shared_Men2_base=0x90000000,
    element_size=2
):

    descriptors = []
    Anum_blocks = A_B // block_width

    block_size_bytes = block_width * block_width * element_size + 0x0C000000
    addr = 0
    BUFFER_addr = Shared_Men2_base

    for _ in range(Anum_blocks):
        for _ in range(Anum_blocks):          
          next_desc_addr = 0
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words)
          BUFFER_addr =  BUFFER_addr + 512

    return descriptors


def generate_dma1_descriptors_for_S2MM(
    A_B=64,
    block_width=16,
    Shared_Men3_base=0x98000000,
    element_size=2
):

    descriptors = []
    Anum_blocks = A_B // block_width

    block_size_bytes = block_width * block_width * element_size + 0x0C000000
    addr = 0
    BUFFER_addr = Shared_Men3_base

    for _ in range(Anum_blocks):
        for _ in range(Anum_blocks):          
          next_desc_addr = 0
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words)
          BUFFER_addr =  BUFFER_addr + 512

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

def op(A_B=16,A_DATA_START = 0x00010000):

    A__B = A_B
    # 1) Generate a list of descriptors corresponding to A and B
    descriptors_A_IN = generate_cdma0_descriptors_for_matrix_A_IN(
        A_B=A__B,
        block_width=16,
        Global_0_base=A_DATA_START,
        Shared_Men0_base=0x80000000,
        Shared_Men2_base=0x90000200,
        element_size=2
    )
    descriptors_B_IN = generate_cdma1_descriptors_for_matrix_B_IN(
        A_B=A__B,
        block_width=16,
        Global_1_base=0x40001000,
        Shared_Men1_base=0x88000000,
        Shared_Men3_base=0x98000000,
        element_size=2
    )

    descriptors_A = descriptors_A_IN
    descriptors_B = descriptors_B_IN

    descriptors_DMA0_B_S2MM = generate_dma0_descriptors_for_S2MM(
        A_B=A__B,
        block_width=16,
        Shared_Men2_base=0x90080000,
        element_size=2
    )
    descriptors_DMA1_B_S2MM = generate_dma1_descriptors_for_S2MM(
        A_B=A__B,
        block_width=16,
        Shared_Men3_base=0x98000200,
        element_size=2
    )
    descriptors_DMA0_B_MM2S = generate_dma0_descriptors_for_MM2S(
        A_B=A__B,
        block_width=16,
        Shared_Men0_base=0x80000000,
        element_size=2,
        row = False
    )
    descriptors_DMA1_B_MM2S = generate_dma1_descriptors_for_MM2S(
        A_B=A__B,
        block_width=16,
        Shared_Men1_base=0x88000000,
        element_size=2,
        row = False
    )

    descriptors_DMA0_C_S2MM = generate_dma0_descriptors_for_S2MM(
        A_B=A__B,
        block_width=16,
        Shared_Men2_base=0x90080000,
        element_size=2
    )
    descriptors_DMA1_C_S2MM = generate_dma1_descriptors_for_S2MM(
        A_B=A__B,
        block_width=16,
        Shared_Men3_base=0x98000200 + (A__B*A__B*2),
        element_size=2
    )
    descriptors_DMA0_C_MM2S = generate_dma0_ADD_for_MM2S(
        A_B=A__B,
        block_width=16,
        Shared_Men2_base=0x90000200,
        element_size=2,
        row = True
    )
    descriptors_DMA1_C_MM2S = generate_dma1_ADD_for_MM2S(
        A_B=A__B,
        block_width=16,
        Shared_Men3_base=0x98000200,
        element_size=2,
        row = True
    )

    descriptors_DMA0_X_S2MM = generate_dma0_descriptors_for_S2MM(
        A_B=A__B,
        block_width=16,
        Shared_Men2_base=0x80000000,
        element_size=2
    )
    descriptors_DMA1_X_S2MM = generate_dma1_descriptors_for_S2MM(
        A_B=A__B,
        block_width=16,
        Shared_Men3_base=0x88080000,
        element_size=2
    )
    descriptors_DMA0_X_MM2S = generate_dma0_descriptors_for_MM2S(
        A_B=A__B,
        block_width=16,
        Shared_Men0_base=0x80000000,
        element_size=2,
        row = True
    )
    descriptors_DMA1_X_MM2S = generate_dma1_descriptors_for_MM2S(
        A_B=A__B,
        block_width=16,
        Shared_Men1_base=0x98000200 + A__B*A__B*2,
        element_size=2,
        row = True
    )


    descriptors_DMA0_S2MM = descriptors_DMA0_B_S2MM + descriptors_DMA0_C_S2MM + descriptors_DMA0_X_S2MM
    descriptors_DMA1_S2MM = descriptors_DMA1_B_S2MM + descriptors_DMA1_C_S2MM + descriptors_DMA1_X_S2MM

    descriptors_DMA0_MM2S = descriptors_DMA0_B_MM2S + descriptors_DMA0_C_MM2S + descriptors_DMA0_X_MM2S
    descriptors_DMA1_MM2S = descriptors_DMA1_B_MM2S + descriptors_DMA1_C_MM2S + descriptors_DMA1_X_MM2S

    cdma0_base = 0xA8000000
    cdma1_base = 0xAC000000
    dma0_S2MM =  0xA0000000
    dma1_S2MM =  0xA4000000
    ADD0 =  len(descriptors_DMA0_S2MM) * 64
    ADD1 =  len(descriptors_DMA1_S2MM) * 64
    dma0_MM2S =  dma0_S2MM + ADD0
    dma1_MM2S =  dma1_S2MM + ADD1

    cdma0_sg_data = link_descriptors_in_memory(descriptors_A, base_addr=cdma0_base, desc_size=64)
    cdma1_sg_data = link_descriptors_in_memory(descriptors_B, base_addr=cdma1_base, desc_size=64)
    dma0_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA0_MM2S, base_addr=dma0_MM2S, desc_size=64)
    dma1_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA1_MM2S, base_addr=dma1_MM2S, desc_size=64)
    dma0_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA0_S2MM, base_addr=dma0_S2MM, desc_size=64)
    dma1_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA1_S2MM, base_addr=dma1_S2MM, desc_size=64)

    ALL = cdma0_sg_data + cdma1_sg_data + dma0_S2MM_sg_data + dma0_MM2S_sg_data + dma1_S2MM_sg_data + dma1_MM2S_sg_data

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cdma0_name = 'cdma0_sg'
    cdma1_name = 'cdma1_sg'
    dma0_MM2S_name = 'dma0_MM2S_sg'
    dma1_MM2S_name = 'dma1_MM2S_sg'
    dma0_S2MM_name = 'dma0_S2MM_sg'
    dma1_S2MM_name = 'dma1_S2MM_sg'

    txt_dir = os.path.join(script_dir,"txt")

    cdma0_file = os.path.join(txt_dir, f"{cdma0_name}.txt")
    cdma1_file = os.path.join(txt_dir, f"{cdma1_name}.txt")
    dma0_MM2S_file = os.path.join(txt_dir, f"{dma0_MM2S_name}.txt")
    dma1_MM2S_file = os.path.join(txt_dir, f"{dma1_MM2S_name}.txt")
    dma0_S2MM_file = os.path.join(txt_dir, f"{dma0_S2MM_name}.txt")
    dma1_S2MM_file = os.path.join(txt_dir, f"{dma1_S2MM_name}.txt")
    all_file = os.path.join(txt_dir, f"allsg.txt")

    write_txt_file(cdma0_sg_data, cdma0_file)
    write_txt_file(cdma1_sg_data, cdma1_file)
    write_txt_file(dma0_MM2S_sg_data, dma0_MM2S_file)
    write_txt_file(dma1_MM2S_sg_data, dma1_MM2S_file)
    write_txt_file(dma0_S2MM_sg_data, dma0_S2MM_file)
    write_txt_file(dma1_S2MM_sg_data, dma1_S2MM_file)
    

    print(" CDMA0 descriptors count:", len(descriptors_A))
    print(" CDMA1 descriptors count:", len(descriptors_B))
    print(" DMA0_MM2S descriptors count:", len(descriptors_DMA0_MM2S))
    print(" DMA1_MM2S descriptors count:", len(descriptors_DMA1_MM2S))
    print(" DMA0_S2MM descriptors count:", len(descriptors_DMA0_S2MM))
    print(" DMA1_S2MM descriptors count:", len(descriptors_DMA1_S2MM))
    allSG = len(descriptors_A) + len(descriptors_B) + len(descriptors_DMA0_MM2S) + len(descriptors_DMA1_MM2S) 
    + len(descriptors_DMA0_S2MM)+ len(descriptors_DMA1_S2MM)
    allSGdescriptors = int(A_DATA_START/64)
    if(allSGdescriptors >= allSG):
        print("There is no need to add space to the SG descriptor")
    else:
        print("Need to add space to the SG descriptor")

    STAR = 0
    CDMA0_len = 64*len(descriptors_A)
    CDMA1_len = 64*len(descriptors_B)
    DMA0_S2MM_len = 64*len(descriptors_DMA0_S2MM)
    DMA1_S2MM_len = 64*len(descriptors_DMA1_S2MM)
    DMA0_MM2S_len = 64*len(descriptors_DMA0_MM2S)
    DMA1_MM2S_len = 64*len(descriptors_DMA1_MM2S)
    DMA0_len = 64*(len(descriptors_DMA0_MM2S)+len(descriptors_DMA0_S2MM))
    DMA1_len = 64*(len(descriptors_DMA1_MM2S)+len(descriptors_DMA1_S2MM))

    descriptorss = []
    alllen = int(int(A_DATA_START/64) - (CDMA0_len + CDMA1_len + DMA0_len + DMA1_len)/64)
    for i in range(alllen):
        A = 0
        word = make_sg_dma_descriptor(A,A,A)
        descriptorss.append(word)
    deadata = flat(descriptorss)
    AL = ALL + deadata
    write_txt_file(AL , all_file)

    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name0 = "ROM"
    name1 = "GM1"
    txt_dir = os.path.join(script_dir,"txt")

    ROM_file0 = os.path.join(txt_dir, f"{name0}.txt")
    GM1_file1 = os.path.join(txt_dir, f"{name1}.txt")

    ROM_LOOP_file0 = os.path.join(txt_dir, f"{name0}LOOP.txt")
    GM1_LOOP_file1 = os.path.join(txt_dir, f"{name1}LOOP.txt")

    def descriptors(len):
        ds_x1 = (len/45)/300 
        ds_x1 = int(ds_x1)
        return ds_x1
    def cdma(row,col):
        cd_x1 = ((row*col*2)/28)/300 
        cd_x1 = int(cd_x1)
        return cd_x1
    def sa_m(row):
        sa_x1 = (2*(16*row)*(row/16)*(row/16)/63)/300 
        sa_x1 = int(sa_x1)
        return sa_x1
    
    def sa_a(row):
        sa_a_x1 = ((16*32)*(row/16)*(row/16)/14)/300 
        sa_a_x1 = int(sa_a_x1)
        return sa_a_x1

    with open(ROM_file0, 'w') as f0:
        f0.write("; --- SEGMENT 1 ---" +"\n")
        f0.write("x5 0x" + f"{(0x00000000 & 0xFFFFFFFF):08x}"+"\n")  #SA
        f0.write("x6 0x" + f"{(0xA8000000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x" + f"{(0x40000000 & 0xFFFFFFFF):08x}"+"\n")  #SA
        f0.write("x8 0x" + f"{(0xB0001000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x9 0x" + f"{(CDMA0_len & 0xFFFFFFFF):08x}"+"\n")   #BBT
        f0.write("x10 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x11 0x" + f"{(CDMA0_len & 0xFFFFFFFF):08x}"+"\n")  #SA
        f0.write("x12 0x" + f"{(0xAC000000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x13 0x" + f"{(CDMA1_len & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x14 0x" + f"{((CDMA0_len+CDMA1_len) & 0xFFFFFFFF):08x}"+"\n")  #SA
        f0.write("x15 0x" + f"{(0xA0000000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x16 0x" + f"{(DMA0_len & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x17 0x" + f"{((CDMA0_len+CDMA1_len+DMA0_len) & 0xFFFFFFFF):08x}"+"\n")  #SA
        f0.write("x18 0x" + f"{(0xA4000000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("; --- SEGMENT 2 ---" +"\n")
        f0.write("x0 0x" + f"{(0x0 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("; --- SEGMENT 3 ---" +"\n")
        f0.write("x0 0x" + f"{(0x0 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("; --- SEGMENT 4 ---" +"\n")
        f0.write("x0 0x" + f"{(0x0 & 0xFFFFFFFF):08x}"+"\n")

    cdma0_ds_x1 = int(CDMA0_len/45 + 10)
    cdma1_ds_x1 = int(CDMA1_len/45 + 10)
    cdma0_gm1_ds_x1 = int(CDMA0_len/(45*90))
    cdma1_gm1_ds_x1 = int(CDMA1_len/(45*90))
    dma0_ds_x1 = descriptors(DMA0_len)
    dma1_ds_x1 = descriptors(DMA1_len)

    with open(ROM_LOOP_file0, 'w') as f0_L:
        f0_L.write("; --- SEGMENT 1 ---" +"\n")
        f0_L.write("x1 0x" + f"{(cdma0_ds_x1 & 0xFFFFFFFF):08x}"+"\n")  #CDMA0

        f0_L.write("; --- SEGMENT 2 ---" +"\n")
        f0_L.write("x1 0x" + f"{(cdma1_ds_x1 & 0xFFFFFFFF):08x}"+"\n")  #CDMA1

        f0_L.write("; --- SEGMENT 3 ---" +"\n")
        f0_L.write("x1 0x" + f"{(dma0_ds_x1 & 0xFFFFFFFF):08x}"+"\n")  #DMA0

        f0_L.write("; --- SEGMENT 4 ---" +"\n")
        f0_L.write("x1 0x" + f"{(dma1_ds_x1 & 0xFFFFFFFF):08x}"+"\n")  #DMA1

    DMA0_B_S2MM_len = 64*len(descriptors_DMA0_B_S2MM)
    DMA1_B_S2MM_len = 64*len(descriptors_DMA1_B_S2MM)
    DMA0_C_S2MM_len = 64*len(descriptors_DMA0_C_S2MM)
    DMA1_C_S2MM_len = 64*len(descriptors_DMA1_C_S2MM)
    DMA0_X_S2MM_len = 64*len(descriptors_DMA0_X_S2MM)
    DMA1_X_S2MM_len = 64*len(descriptors_DMA1_X_S2MM)
    DMA0_B_MM2S_len = 64*len(descriptors_DMA0_B_MM2S)
    DMA1_B_MM2S_len = 64*len(descriptors_DMA1_B_MM2S)
    DMA0_C_MM2S_len = 64*len(descriptors_DMA0_C_MM2S)
    DMA1_C_MM2S_len = 64*len(descriptors_DMA1_C_MM2S)
    DMA0_X_MM2S_len = 64*len(descriptors_DMA0_X_MM2S)
    DMA1_X_MM2S_len = 64*len(descriptors_DMA1_X_MM2S)

    with open(GM1_LOOP_file1, 'w') as f1_L:
        f1_L.write("; --- SEGMENT 1 ---" +"\n") #CDMA
        CDMA_X1 = cdma(A_B,A_B)
        f1_L.write("x1 0x" + f"{(CDMA_X1 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 2 ---" +"\n") 
        f1_L.write("x1 0x" + f"{(0 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 3 ---" +"\n") #DMA_B
        B_X1 = sa_m(A_B)
        f1_L.write("x1 0x" + f"{(B_X1 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 4 ---" +"\n")
        f1_L.write("x1 0x" + f"{(0 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 5 ---" +"\n") #DMA_C
        C_X1 = sa_a(A_B)
        f1_L.write("x1 0x" + f"{(C_X1 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 6 ---" +"\n")
        f1_L.write("x1 0x" + f"{(0 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 7 ---" +"\n") #DMA_X
        X_X1 = sa_m(A_B)
        f1_L.write("x1 0x" + f"{(X_X1 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 8 ---" +"\n") #descriptors
        f1_L.write("x1 0x" + f"{(cdma0_gm1_ds_x1 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 9 ---" +"\n") #descriptors
        f1_L.write("x1 0x" + f"{(cdma1_gm1_ds_x1 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 10 ---" +"\n") #descriptors
        f1_L.write("x1 0x" + f"{(dma0_ds_x1 & 0xFFFFFFFF):08x}"+"\n")

        f1_L.write("; --- SEGMENT 11 ---" +"\n") #descriptors
        f1_L.write("x1 0x" + f"{(dma1_ds_x1 & 0xFFFFFFFF):08x}"+"\n")

    with open(GM1_file1, 'w') as f1:
        #CDMA 0 1
        f1.write("; --- SEGMENT 1 ---" +"\n")
        f1.write("x1 0x" + f"{(0xC0000800 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0xC0000840 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0x00001008 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0xA8000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0xAC000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((0xA8000000+CDMA0_len-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((0xAC000000+CDMA1_len-64) & 0xFFFFFFFF):08x}"+"\n")

        #DMA_S2MM_B
        f1.write("; --- SEGMENT 2 ---" +"\n")
        f1.write("x1 0x" + f"{(0xC0000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0xC0000400 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0xA0000000 & 0xFFFFFFFF):08x}"+"\n") #Head
        f1.write("x4 0x" + f"{(0xA4000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x1001 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((0xA0000000+ DMA0_B_S2MM_len-64) & 0xFFFFFFFF):08x}"+"\n") #Tail
        f1.write("x8 0x" + f"{((0xA4000000+ DMA1_B_S2MM_len-64) & 0xFFFFFFFF):08x}"+"\n")

        #DMA_MM2S_B
        f1.write("; --- SEGMENT 3 ---" +"\n")
        f1.write("x1 0x" + f"{(0xC0000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0xC0000400 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0xA0000000+DMA0_S2MM_len & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0xA4000000+DMA1_S2MM_len & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x1001 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((0xA0000000+DMA0_B_MM2S_len+DMA0_S2MM_len-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((0xA4000000+DMA1_B_MM2S_len+DMA1_S2MM_len-64) & 0xFFFFFFFF):08x}"+"\n")

        #DMA_S2MM_C
        f1.write("; --- SEGMENT 4 ---" +"\n")
        f1.write("x1 0x" + f"{(0xC0000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0xC0000400 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{((0xA0000000+ DMA0_B_S2MM_len) & 0xFFFFFFFF):08x}"+"\n") #Head
        f1.write("x4 0x" + f"{((0xA4000000+ DMA1_B_S2MM_len) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x1001 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((0xA0000000+ DMA0_B_S2MM_len + DMA0_C_S2MM_len -64) & 0xFFFFFFFF):08x}"+"\n") #Tail
        f1.write("x8 0x" + f"{((0xA4000000+ DMA1_B_S2MM_len + DMA1_C_S2MM_len -64) & 0xFFFFFFFF):08x}"+"\n")

        #DMA_MM2S_C
        f1.write("; --- SEGMENT 5 ---" +"\n")
        f1.write("x1 0x" + f"{(0xC0000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0xC0000400 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0xA0000000+DMA0_S2MM_len+DMA0_B_MM2S_len & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0xA4000000+DMA1_S2MM_len+DMA1_B_MM2S_len & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x1001 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((0xA0000000+DMA0_B_MM2S_len+DMA0_S2MM_len+DMA0_C_MM2S_len-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((0xA4000000+DMA1_B_MM2S_len+DMA1_S2MM_len+DMA1_C_MM2S_len-64) & 0xFFFFFFFF):08x}"+"\n")

        #DMA_S2MM_X
        f1.write("; --- SEGMENT 6 ---" +"\n")
        f1.write("x1 0x" + f"{(0xC0000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0xC0000400 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{((0xA0000000+ DMA0_B_S2MM_len + DMA0_C_S2MM_len) & 0xFFFFFFFF):08x}"+"\n") #Head
        f1.write("x4 0x" + f"{((0xA4000000+ DMA1_B_S2MM_len + DMA1_C_S2MM_len) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x1001 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((0xA0000000+ DMA0_S2MM_len -64) & 0xFFFFFFFF):08x}"+"\n") #Tail
        f1.write("x8 0x" + f"{((0xA4000000+ DMA1_S2MM_len -64) & 0xFFFFFFFF):08x}"+"\n")

        #DMA_MM2S_X
        f1.write("; --- SEGMENT 7 ---" +"\n")
        f1.write("x1 0x" + f"{(0xC0000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0xC0000400 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0xA0000000+DMA0_S2MM_len+DMA0_B_MM2S_len+DMA1_C_MM2S_len & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0xA4000000+DMA1_S2MM_len+DMA1_B_MM2S_len+DMA1_C_MM2S_len & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x1001 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((0xA0000000+DMA0_MM2S_len + DMA0_S2MM_len-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((0xA4000000+DMA1_MM2S_len +  DMA1_S2MM_len-64) & 0xFFFFFFFF):08x}"+"\n")

        f1.write("; --- SEGMENT 8 ---" +"\n")
        f1.write("x1 0x" + f"{(0xC0000800 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0x00000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0xA8000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(CDMA0_len  & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{(CDMA0_len  & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((0xAC000000) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x9 0x" + f"{(CDMA1_len & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x10 0x" + f"{((CDMA0_len+CDMA1_len) & 0xFFFFFFFF):08x}"+"\n")  #SA
        f1.write("x11 0x" + f"{(0xA0000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x12 0x" + f"{(DMA0_len & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x13 0x" + f"{((CDMA0_len+CDMA1_len+DMA0_len) & 0xFFFFFFFF):08x}"+"\n")  #SA
        f1.write("x14 0x" + f"{(0xA4000000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x15 0x" + f"{(DMA1_len & 0xFFFFFFFF):08x}"+"\n")

        f1.write("; --- SEGMENT 9 ---" +"\n")
        f1.write("x0 0x" + f"{(0 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("; --- SEGMENT 10 ---" +"\n")
        f1.write("x0 0x" + f"{(0 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("; --- SEGMENT 11 ---" +"\n")
        f1.write("x0 0x" + f"{(0 & 0xFFFFFFFF):08x}"+"\n")
def main(matrix_size=32, START = 0x00001000):
    A_B = matrix_size
    A_DATA_START = START
    print("Number of SG descriptors: ",int(A_DATA_START/64))
    op(A_B = A_B,A_DATA_START = A_DATA_START)

if __name__ == "__main__":
    main(matrix_size=32)
