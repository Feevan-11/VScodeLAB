import  os
import  asm_generate
#import  loop
import  translator
import  merge_mif_files
import  MAC
import  hex_to_bin
import  matrix_mul
import  mac_start_make


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
          addr = addr + block_width*block_width*element_size
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
          
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes, APP0)
          addr = addr + block_width*block_width*element_size
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

WRITE_BACK = 0x20000

def generate_ethdma_descriptors_for_MM2S(
    HEAD_in_base=0x40000000,
    data_in_base=0x40000000,
    MAC_LENTH = 64,
    SG_NUM = 100
):

    descriptors = []

    block_size_bytes0=  0x08000000 + 64
    block_size_bytes =  0x04000000 + MAC_LENTH
    addr = 0
    addr0 = HEAD_in_base 

    for j in range(SG_NUM):
      addr0 = addr0 + 64*j
      BUFFER_addr = data_in_base + addr
      next_desc_addr = 0
      desc_words0 = make_sg_dma_descriptor(next_desc_addr, addr0, block_size_bytes0,0)
      descriptors.append(desc_words0)
      
      desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes,0)
      descriptors.append(desc_words)
      addr = addr + MAC_LENTH

    return descriptors

def generate_ethdma_XN_for_MM2S(
    data_in_head = 0x40000000,
    data_in_base=  0x40000000,
    MAC_LENTH = 64,
    xn_NUM = 100
):

    descriptors = []

    block_size_bytes0=  0x08000000 + 64
    block_size_bytes =  0x04000000 + MAC_LENTH
    addr = 0
    addr0 = data_in_head

    for j in range(xn_NUM):
      BUFFER_addr = data_in_base + addr
      next_desc_addr = 0
      desc_words0 = make_sg_dma_descriptor(next_desc_addr, addr0, block_size_bytes0,0)
      descriptors.append(desc_words0)
      
      desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes,0)
      descriptors.append(desc_words)
      addr = addr + MAC_LENTH

    return descriptors

def op_SA(A__ROWS=16,B__ROWS=16,B__COLS=16, block_width = 32, element_size = 2,A_TYPE = 0,B_TYPE = 0, MPU_ID = 0,
          mac_da = 0xF0000000 , flag = 0xCCA41704, mac_lenth= 99):

    if MPU_ID == 0:
        data0_in      = Data_Mem0
        data1_in      = Data_Mem1
        data0_out     = Data_Mem0 + WRITE_BACK
        data1_out     = Data_Mem1 + WRITE_BACK
        DMA0_REG_base = DMA0_config
        DMA1_REG_base = DMA1_config
        DMA0_SG       = SGMEM_DMA0_BASE
        DMA1_SG       = SGMEM_DMA1_BASE
    elif MPU_ID == 1:
        data0_in      = Data_Mem2
        data1_in      = Data_Mem3
        data0_out     = Data_Mem2 + WRITE_BACK
        data1_out     = Data_Mem3 + WRITE_BACK
        DMA0_REG_base = DMA2_config
        DMA1_REG_base = DMA3_config
        DMA0_SG       = SGMEM_DMA2_BASE
        DMA1_SG       = SGMEM_DMA3_BASE
    elif MPU_ID == 2:
        data0_in      = Data_Mem4
        data1_in      = Data_Mem5
        data0_out     = Data_Mem4 + WRITE_BACK
        data1_out     = Data_Mem5 + WRITE_BACK
        DMA0_REG_base = DMA4_config
        DMA1_REG_base = DMA5_config
        DMA0_SG       = SGMEM_DMA4_BASE
        DMA1_SG       = SGMEM_DMA5_BASE
    elif MPU_ID == 3:
        data0_in      = Data_Mem6
        data1_in      = Data_Mem7
        data0_out     = Data_Mem6 + WRITE_BACK
        data1_out     = Data_Mem7 + WRITE_BACK
        DMA0_REG_base = DMA6_config
        DMA1_REG_base = DMA7_config
        DMA0_SG       = SGMEM_DMA6_BASE
        DMA1_SG       = SGMEM_DMA7_BASE

    else:
        print(f"ERRO")

    A_ROWS = A__ROWS
    B_ROWS = B__ROWS
    B_COLS = B__COLS


    #global SA_setid

    descriptors_DMA0_S2MM = generate_dma0_descriptors_for_S2MM(
        A_rows=A_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Shared_Men2_base=data0_out,
        element_size=element_size,
        APP0 = 0
    )
    descriptors_DMA1_S2MM = generate_dma1_descriptors_for_S2MM(
        A_rows=A_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Shared_Men3_base=data1_out,
        element_size=element_size,
        APP0 = 0
    )
    descriptors_DMA0_MM2S = generate_dma0_descriptors_for_MM2S(
        A_rows=A_ROWS,
        A_B = B_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Shared_Men0_base=data0_in,
        element_size=element_size,
        APP0 = 0
    )
    descriptors_DMA1_MM2S = generate_dma1_descriptors_for_MM2S(
        A_rows=A_ROWS,
        A_B = B_ROWS,
        B_cols=B_COLS,
        block_width=block_width,
        Shared_Men1_base=data1_in,
        element_size=element_size,
        APP0 = 0
    )
    M_NUM = int((A_ROWS/block_width) * (B_COLS/block_width))*2
    descriptors_ethdma_DATA_MM2S = generate_ethdma_descriptors_for_MM2S(
        HEAD_in_base=DDR1_START,
        data_in_base=data0_in,
        MAC_LENTH = block_width*block_width,
        SG_NUM = M_NUM
    )
    descriptors_ethdma_XN_MM2S = generate_ethdma_XN_for_MM2S(
        data_in_head=DDR1_XN_HEAD,
        data_in_base=DDR1_XN_DATA,
        MAC_LENTH = mac_lenth*64,
        xn_NUM = XN_NUM
    )
    

    ETH4_DATA_MM2S_len = 64*len(descriptors_ethdma_DATA_MM2S)
    #ETH43_DATA_len = 64*len(descriptors_ETHDMA1_S2MM)
    ETH4_XN_MM2S_len = 64*len(descriptors_ethdma_XN_MM2S)

    SGMEM_DMA0_start =  DMA0_SG            
    SGMEM_DMA0_start_MM2S =  SGMEM_DMA0_start + len(descriptors_DMA0_S2MM) * 64
    SGMEM_DMA1_start =  DMA1_SG
    SGMEM_DMA1_start_MM2S =  SGMEM_DMA1_start + len(descriptors_DMA1_S2MM) * 64

    dma0_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA0_MM2S, base_addr=SGMEM_DMA0_start_MM2S, desc_size=64)
    dma1_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA1_MM2S, base_addr=SGMEM_DMA1_start_MM2S, desc_size=64)
    dma0_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA0_S2MM, base_addr=SGMEM_DMA0_start, desc_size=64)
    dma1_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA1_S2MM, base_addr=SGMEM_DMA1_start, desc_size=64)
    ethdma4_sg_DATA_data0 = link_descriptors_in_memory(descriptors_ethdma_DATA_MM2S, base_addr=SGMEM_ETHDMA4_BASE, desc_size=64)
    ethdma4_sg_XN_data = link_descriptors_in_memory(descriptors_ethdma_XN_MM2S, base_addr=SGMEM_ETHDMA4_BASE+ETH4_DATA_MM2S_len, desc_size=64)
    #ethdma3_sg_DATA_data = link_descriptors_in_memory(descriptors_ETHDMA1_S2MM, base_addr=SGMEM_ETHDMA3_BASE, desc_size=64)
    
    dma0_sg_data = dma0_S2MM_sg_data + dma0_MM2S_sg_data
    dma1_sg_data = dma1_S2MM_sg_data + dma1_MM2S_sg_data

    script_dir = os.path.dirname(os.path.abspath(__file__))
    dma0_name = 'dma0_sg'
    dma1_name = 'dma1_sg'

    ethdma4_name = 'ethdma4_sg'
    ethdma3_name = 'ethdma3_sg'

    
    txt_dir = os.path.join(script_dir,"txt")
    dma0_file = os.path.join(txt_dir, f"{dma0_name}.txt")
    dma1_file = os.path.join(txt_dir, f"{dma1_name}.txt")
    ethdma4_file = os.path.join(txt_dir, f"{ethdma4_name}.txt")
    #ethdma3_file = os.path.join(txt_dir, f"{ethdma3_name}.txt")

    ethdma4_sg_DATA_data = ethdma4_sg_DATA_data0 

    write_txt_file(dma0_sg_data, dma0_file)
    write_txt_file(dma1_sg_data, dma1_file)
    write_txt_file(ethdma4_sg_DATA_data+ethdma4_sg_XN_data, ethdma4_file)
    #write_txt_file(ethdma3_sg_DATA_data, ethdma3_file)
    
 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    txt_dir = os.path.join(script_dir,"txt")
    
    name1 = "SA"   
    SA_file1 = os.path.join(txt_dir, f"{name1}.txt")

    DMA0_S2MM_len = 64*len(descriptors_DMA0_S2MM)
    DMA0_MM2S_len = 64*len(descriptors_DMA0_MM2S)
    DMA1_S2MM_len = 64*len(descriptors_DMA1_S2MM)
    DMA1_MM2S_len = 64*len(descriptors_DMA1_MM2S)


    DMA0_MM2S_START = DMA0_SG + DMA0_S2MM_len
    DMA1_MM2S_START = DMA1_SG + DMA1_S2MM_len

    with open(SA_file1, 'w') as f1:
        f1.write(f"; --- SEGMENT 1 ---" +"\n")
        f1.write("x1 0x" + f"{(DMA0_REG_base   & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(DMA1_REG_base   & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(DMA0_SG & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(DMA1_SG & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(0x1001 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{(DMA0_MM2S_START -64 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{(DMA1_MM2S_START -64 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x9 0x" +  f"{((DMA0_MM2S_START) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x10 0x" + f"{((DMA1_MM2S_START) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x11 0x" + f"{((DMA0_MM2S_START+DMA0_MM2S_len-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x12 0x" + f"{((DMA1_MM2S_START+DMA1_MM2S_len-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write(f"; --- SEGMENT 2 ---" +"\n")
        f1.write("x1 0x"  + f"{(0x0          & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x"  + f"{(ethdma4_config          & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x"  + f"{(0x00001001              & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x"  + f"{(0x00001000              & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x"  + f"{(SGMEM_ETHDMA3_BASE      & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x"  + f"{(SGMEM_ETHDMA3_BASE      & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x"  + f"{(SGMEM_ETHDMA4_BASE  + ETH4_DATA_MM2S_len    & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x"  + f"{((SGMEM_ETHDMA4_BASE + ETH4_DATA_MM2S_len + ETH4_XN_MM2S_len - 64)      & 0xFFFFFFFF):08x}"+"\n")
        f1.write(f"; --- SEGMENT 3 ---" +"\n")
        f1.write("x1 0x"  + f"{(0x0         & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x"  + f"{(ethdma4_config          & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x"  + f"{(0x00001001              & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x"  + f"{(0x00001000              & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x"  + f"{(SGMEM_ETHDMA0_BASE         & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x"  + f"{(SGMEM_ETHDMA0_BASE      & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x"  + f"{(SGMEM_ETHDMA4_BASE      & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x"  + f"{((SGMEM_ETHDMA4_BASE  + ETH4_DATA_MM2S_len - 64)      & 0xFFFFFFFF):08x}"+"\n")


    

    asm_generate.main_SA_ID()
    
    translator.SA_ID() 
    mac_start_make.make_XN_head(mac_da,XN_FLAG-1)
    mac_start_make.make_Array(mac_da,M_NUM)
    mac_start_make.make_XN(mac_da,mac_lenth,XN_NUM)
    hex_to_bin.dmasg()
    matrix_mul.main(False ,A__ROWS,B__ROWS,B__COLS, A_TYPE , MPU_ID)
    
    global ROM_START

    
    MAC.main_auto(flag,mac_da,1,"DMA0",mac_lenth,DMA0_SG)
    MAC.main_auto(flag,mac_da,1,"DMA1",mac_lenth,DMA1_SG)
    MAC.main_auto(flag,mac_da,1,'MATRIX_A',mac_lenth,data0_in)
    MAC.main_auto(flag,mac_da,1,'MATRIX_B',mac_lenth,data1_in)
    MAC.main_auto(flag,mac_da,1,"SA",mac_lenth,ROM_START)
    MAC.main_auto(flag,mac_da,1,"ETHDMA4",mac_lenth,SGMEM_ETHDMA1_BASE)
    MAC.main_auto(flag,mac_da,1,"Array_mac",mac_lenth,DDR1_START)
    MAC.main_auto(flag,mac_da,1,"XN_head_mac",mac_lenth,DDR1_XN_HEAD)
    MAC.main_auto(flag,mac_da,1,"XN_mac",mac_lenth,DDR1_XN_DATA)
    
    #merge_mif_files.SA()

    ROM_START = ROM_START + 64*10
    

SGMEM_CDMA0_BASE      = 0xF4000000
SGMEM_CDMA1_BASE      = 0xF4200000
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

CDMA0_config     = 0xFF004400
CDMA1_config     = 0xFF004440
DMA0_config      = 0xFF000000
DMA1_config      = 0xFF000400
DMA2_config      = 0xFF000800
DMA3_config      = 0xFF000C00
DMA4_config      = 0xFF001000
DMA5_config      = 0xFF001400
DMA6_config      = 0xFF001800
DMA7_config      = 0xFF001C00
ethdma0_config       = 0xFF003000
ethdma1_config       = 0xFF003400
ethdma2_config       = 0xFF003800
ethdma3_config       = 0xFF003C00
ethdma4_config       = 0xFF004000
XN_FLAG = 257


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
DDR1_XN_DATA     = 0x80004000
DDR1_XN_HEAD     = 0x80002000

ROM_START   = 0xF0001500
XN_NUM      = 10

def main(matrix_List= [[16,16,16,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0]], MPU_ID = '1000',
         mac_da = 0xF0000000 , flag = 0xCCA41704 , mac_lenth= 99):


    bin_str = MPU_ID

    script_dir = os.path.dirname(os.path.abspath(__file__))
    MIF_DIR = os.path.join(script_dir, "mif")
    TXT_DIR = os.path.join(script_dir, "txt")
    mif_file = os.path.join(MIF_DIR, ".mif")

    headers_txt_path = os.path.join(TXT_DIR, "headers.txt")
    with open(headers_txt_path, "w", encoding="utf-8") as f:
        f.write("")

    segments_txt_path = os.path.join(TXT_DIR, "segments.txt")
    with open(segments_txt_path, "w", encoding="utf-8") as f:
        f.write("")

    
    if bin_str[0] == '1':
        op_SA(A__ROWS=matrix_List[0][0],B__ROWS=matrix_List[0][1],B__COLS=matrix_List[0][2], block_width = matrix_List[0][3], 
              element_size = matrix_List[0][4],A_TYPE = matrix_List[0][5],B_TYPE = matrix_List[0][6],
                MPU_ID = 0,mac_da = mac_da , flag = flag, mac_lenth= mac_lenth)
    
    if bin_str[1] == '1':
        op_SA(A__ROWS=matrix_List[1][0],B__ROWS=matrix_List[1][1],B__COLS=matrix_List[1][2], block_width = matrix_List[1][3], 
                element_size = matrix_List[1][4],A_TYPE = matrix_List[1][5],B_TYPE = matrix_List[1][6],
                MPU_ID = 1,mac_da = mac_da ,flag = flag, mac_lenth= mac_lenth)
  
    if bin_str[2] == '1':
        op_SA(A__ROWS=matrix_List[2][0],B__ROWS=matrix_List[2][1],B__COLS=matrix_List[2][2], block_width = matrix_List[2][3], 
              element_size = matrix_List[2][4],A_TYPE = matrix_List[2][5],B_TYPE = matrix_List[2][6], 
              MPU_ID = 2,mac_da = mac_da ,flag = flag, mac_lenth= mac_lenth)
    
    if bin_str[3] == '1':
        op_SA(A__ROWS=matrix_List[3][0],B__ROWS=matrix_List[3][1],B__COLS=matrix_List[3][2], block_width = matrix_List[3][3], 
              element_size = matrix_List[3][4],A_TYPE = matrix_List[3][5],B_TYPE = matrix_List[3][6], 
              MPU_ID = 3,mac_da = mac_da ,flag = flag, mac_lenth= mac_lenth)
    

if __name__ == "__main__":
    main(matrix_List = [[16,16,16,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0],[16,16,16,32,2,0,0]] , MPU_ID = '1000',
         mac_da = 0x80000000 , flag = 0xCCA41704, mac_lenth= 99)



      
