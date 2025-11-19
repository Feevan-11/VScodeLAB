import  os
import  config
import  asm_generate
#import  loop
import  translator
import  merge_mif_files

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
    list1,
    Global_base=0x00010000,
    Shared_Men_base=0x80000000
):
    src_addr = Global_base
    dst_addr = Shared_Men_base
    descriptors = []    
    Anum_blocks = len(list1)
    block_size_bytes = 1

    for i in range(Anum_blocks):
       
        block_size_bytes = list1[i] * 64
        
        next_desc_addr = 0

        desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
        descriptors.append(desc_words)

        src_addr = src_addr +  block_size_bytes

        dst_addr = dst_addr +  block_size_bytes

    return descriptors


def generate_cdma1_descriptors_for_matrix_B_IN(
    list1,
    Global_base=0x00010000,
    Shared_Men_base=0x80000000
):
    src_addr = Global_base
    dst_addr = Shared_Men_base
    descriptors = []    
    Bnum_blocks = len(list1)
    block_size_bytes = 1

    for i in range(Bnum_blocks):
       
        block_size_bytes = list1[i] * 64
        
        next_desc_addr = 0

        desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
        descriptors.append(desc_words)

        src_addr = src_addr +  block_size_bytes

        dst_addr = dst_addr +  block_size_bytes

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
    
    list1,
    Shared_Men_base=0x80000000
):
    
    descriptors = []
    
    Anum_blocks = len(list1)
    Bnum_blocks = len(list1)
    BUFFER_addr = Shared_Men_base

    
    for i in range(Anum_blocks):        
        block_size_bytes =  list1[i]*64 + 0x0C000000
        block_size =        list1[i]*64 
        for j in range(Bnum_blocks):
          next_desc_addr = 0
          
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes , 0)
          descriptors.append(desc_words)

        BUFFER_addr = BUFFER_addr + block_size
    return descriptors

def generate_dma1_descriptors_for_MM2S(
    list1,
    Shared_Men_base=0x80000000
):
    
    descriptors = []
    
    Anum_blocks = len(list1)
    Bnum_blocks = len(list1)
    BUFFER_addr = Shared_Men_base

    
    for i in range(Anum_blocks):        
        
        for j in range(Bnum_blocks):
          next_desc_addr = 0
          block_size_bytes =  list1[j]*64 + 0x0C000000
          block_size =        list1[j]*64 
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes , 0)
          descriptors.append(desc_words)

        BUFFER_addr = BUFFER_addr + block_size
    return descriptors

def generate_dma0_descriptors_for_S2MM(
    list1,
    Shared_Men_base=0x90000000
):

    descriptors = []
    Anum_blocks = len(list1)
    Bnum_blocks = len(list1)

    
    BUFFER_addr = Shared_Men_base

    for i in range(Anum_blocks):
        block_size_bytes = list1[i]*64*2  + 0x0C000000
        block_size       = list1[i]*64*2
        for j in range(Bnum_blocks):
          
          next_desc_addr = 0
          
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes,0)
          BUFFER_addr = BUFFER_addr + block_size
          descriptors.append(desc_words)

    return descriptors

def generate_dma1_descriptors_for_S2MM(
    list1,
    Shared_Men_base=0x90000000
):

    descriptors = []
    Anum_blocks = len(list1)
    Bnum_blocks = len(list1)

    
    BUFFER_addr = Shared_Men_base

    for i in range(Anum_blocks):
        block_size_bytes = list1[i]*64*2  + 0x0C000000
        block_size       = list1[i]*64*2
        for j in range(Bnum_blocks):
          
          next_desc_addr = 0
          
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes,0)
          BUFFER_addr = BUFFER_addr + block_size
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

def read_integer_lists_and_lengths(file_path):
    """
    从指定文件中读取两行整数（每行整数由空格分隔），返回两个整数列表及其长度

    参数:
        file_path (str): 文件路径

    返回:
        tuple: 包含 (list1, list2, length1, length2) 的元组
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 确保文件至少有两行内容
        if len(lines) < 2:
            raise ValueError("文件行数不足，需要至少两行数据")
        
        # 处理第一行：转换为整数列表
        list1_str = lines[0].strip()
        list1 = [int(x) for x in list1_str.split()] if list1_str else []
        
        # 处理第二行：转换为整数列表
        list2_str = lines[1].strip()
        list2 = [int(x) for x in list2_str.split()] if list2_str else []
        
        # 计算两个列表的长度
        length1 = len(list1)
        length2 = len(list2)
        
        print(f"列表1包含 {length1} 个整数: {list1}")
        print(f"列表2包含 {length2} 个整数: {list2}")
        
        return list1, list2, length1, length2
        
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 未找到")
        return [], [], 0, 0
    except ValueError as e:
        print(f"数据格式错误: 请确保文件中只包含有效的整数。错误详情: {e}")
        return [], [], 0, 0
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return [], [], 0, 0



    


def op_SA(DDR0_START = 0x0, DDR1_START = 0x0, CDMA0_reg_base= 0x0, CDMA1_reg_base= 0x0,  MPU_ID = 0):

    out = 0x10000
    if MPU_ID == 0:
        data0_in      = Data_Mem0
        data1_in      = Data_Mem1
        data0_out     = Data_Mem0 + out
        data1_out     = Data_Mem1 + out
        DMA0_REG_base = DMA0_config
        DMA1_REG_base = DMA1_config
        DMA0_SG       = SGMEM_DMA0_BASE
        DMA1_SG       = SGMEM_DMA1_BASE
    elif MPU_ID == 1:
        data0_in      = Data_Mem2
        data1_in      = Data_Mem3
        data0_out     = Data_Mem2 + out
        data1_out     = Data_Mem3 + out
        DMA0_REG_base = DMA2_config
        DMA1_REG_base = DMA3_config
        DMA0_SG       = SGMEM_DMA2_BASE
        DMA1_SG       = SGMEM_DMA3_BASE
    elif MPU_ID == 2:
        data0_in      = Data_Mem4
        data1_in      = Data_Mem5
        data0_out     = Data_Mem4 + out
        data1_out     = Data_Mem5 + out
        DMA0_REG_base = DMA4_config
        DMA1_REG_base = DMA5_config
        DMA0_SG       = SGMEM_DMA4_BASE
        DMA1_SG       = SGMEM_DMA5_BASE
    elif MPU_ID == 3:
        data0_in      = Data_Mem6
        data1_in      = Data_Mem7
        data0_out     = Data_Mem6 + out
        data1_out     = Data_Mem7 + out
        DMA0_REG_base = DMA6_config
        DMA1_REG_base = DMA7_config
        DMA0_SG       = SGMEM_DMA6_BASE
        DMA1_SG       = SGMEM_DMA7_BASE

    else:
        print(f"ERRO")

    file_path = r".\sparse\packet_blocks_info.txt"
    List1, List2, len1, len2 = read_integer_lists_and_lengths(file_path)

    global ALL_SG_descriptors
    global SGMEM_CDMA0_start
    global SGMEM_CDMA1_start
    global ALL_SG_strat_DDR

    #global SA_setid

    descriptors_A_IN = generate_cdma0_descriptors_for_matrix_A_IN(
        list1 = List1,
        Global_base=DDR0_START,
        Shared_Men_base=data0_in
    )
    descriptors_B_IN = generate_cdma1_descriptors_for_matrix_B_IN(
        list1 = List2,
        Global_base=DDR1_START,
        Shared_Men_base=data1_in
    )

    descriptors_A = descriptors_A_IN
    descriptors_B = descriptors_B_IN

    descriptors_DMA0_S2MM = generate_dma0_descriptors_for_S2MM(
        list1 = List1,
        Shared_Men_base=data0_in
    )
    descriptors_DMA1_S2MM = generate_dma1_descriptors_for_S2MM(
        list1 = List2,
        Shared_Men_base=data1_in
    )
    descriptors_DMA0_MM2S = generate_dma0_descriptors_for_MM2S(
        list1 = List1,
        Shared_Men_base=data0_in
    )
    descriptors_DMA1_MM2S = generate_dma1_descriptors_for_MM2S(
        list1 = List2,
        Shared_Men_base=data1_in
    )
    
    CDMA0_len  = 64*len(descriptors_A)
    CDMA1_len  = 64*len(descriptors_B)

    SGMEM_DMA0_start =  DMA0_SG            #print(f'{SGMEM_CDMA0_start:08x}')
    SGMEM_DMA0_start_MM2S =  SGMEM_DMA0_start + len(descriptors_DMA0_S2MM) * 64
    SGMEM_DMA1_start =  DMA1_SG
    SGMEM_DMA1_start_MM2S =  SGMEM_DMA1_start + len(descriptors_DMA1_S2MM) * 64

    cdma0_sg_data = link_descriptors_in_memory(descriptors_A, base_addr=SGMEM_CDMA0_start, desc_size=64)
    cdma1_sg_data = link_descriptors_in_memory(descriptors_B, base_addr=SGMEM_CDMA1_start, desc_size=64)

    dma0_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA0_MM2S, base_addr=SGMEM_DMA0_start_MM2S, desc_size=64)
    dma1_MM2S_sg_data = link_descriptors_in_memory(descriptors_DMA1_MM2S, base_addr=SGMEM_DMA1_start_MM2S, desc_size=64)
    dma0_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA0_S2MM, base_addr=SGMEM_DMA0_start, desc_size=64)
    dma1_S2MM_sg_data = link_descriptors_in_memory(descriptors_DMA1_S2MM, base_addr=SGMEM_DMA1_start, desc_size=64)

    ALL_SG_descriptors = ALL_SG_descriptors + cdma0_sg_data + cdma1_sg_data + dma0_S2MM_sg_data + dma0_MM2S_sg_data + dma1_S2MM_sg_data + dma1_MM2S_sg_data

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cdma0_name = 'cdma0_sg'
    cdma1_name = 'cdma1_sg'
    dma0_MM2S_name = 'dma0_MM2S_sg'
    dma1_MM2S_name = 'dma1_MM2S_sg'
    dma0_S2MM_name = 'dma0_S2MM_sg'
    dma1_S2MM_name = 'dma1_S2MM_sg'
    txt_dir = os.path.join(script_dir,"sparse")
    cdma0_file = os.path.join(txt_dir, f"{cdma0_name}.txt")
    cdma1_file = os.path.join(txt_dir, f"{cdma1_name}.txt")
    dma0_MM2S_file = os.path.join(txt_dir, f"{dma0_MM2S_name}.txt")
    dma1_MM2S_file = os.path.join(txt_dir, f"{dma1_MM2S_name}.txt")
    dma0_S2MM_file = os.path.join(txt_dir, f"{dma0_S2MM_name}.txt")
    dma1_S2MM_file = os.path.join(txt_dir, f"{dma1_S2MM_name}.txt")

    write_txt_file(cdma0_sg_data, cdma0_file)
    write_txt_file(cdma1_sg_data, cdma1_file)
    write_txt_file(dma0_MM2S_sg_data, dma0_MM2S_file)
    write_txt_file(dma1_MM2S_sg_data, dma1_MM2S_file)
    write_txt_file(dma0_S2MM_sg_data, dma0_S2MM_file)
    write_txt_file(dma1_S2MM_sg_data, dma1_S2MM_file)
          
 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name0 = "SG"
    txt_dir = os.path.join(script_dir,"txt")
    SG_file0 = os.path.join(txt_dir, f"{name0}.txt")
    #SG_LOOP_file0 = os.path.join(txt_dir, f"{name0}LOOP.txt")
    name1 = "SA"   
    SA_file1 = os.path.join(txt_dir, f"{name1}.txt")
    #SA_LOOP_file1 = os.path.join(txt_dir, f"{name1}LOOP.txt")


    DMA0_S2MM_len = 64*len(descriptors_DMA0_S2MM)
    DMA0_MM2S_len = 64*len(descriptors_DMA0_MM2S)
    DMA1_S2MM_len = 64*len(descriptors_DMA1_S2MM)
    DMA1_MM2S_len = 64*len(descriptors_DMA1_MM2S)
    DMA0_len = 64*(len(descriptors_DMA0_MM2S)+len(descriptors_DMA0_S2MM))
    DMA1_len = 64*(len(descriptors_DMA1_MM2S)+len(descriptors_DMA1_S2MM))
    
    CDMA0_START_DDR = ALL_SG_strat_DDR
    CDMA1_START_DDR = CDMA0_START_DDR + CDMA0_len
    DMA0_START_DDR  = CDMA1_START_DDR + CDMA1_len
    DMA1_START_DDR  = DMA0_START_DDR  + DMA0_len
    
    with open(SG_file0, 'w') as f0:
        f0.write("; --- SEGMENT 1 ---" +"\n")
        f0.write("x1 0x"  + f"{(CDMA0_reg_base     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x"  + f"{(CDMA1_reg_base     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x"  + f"{(0x00001000         & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x"  + f"{(0x00001000         & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x"  + f"{(CDMA0_START_DDR    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x"  + f"{(SGMEM_CDMA0_start  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x"  + f"{(CDMA0_len          & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x"  + f"{(CDMA1_START_DDR    & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x9 0x"  + f"{(SGMEM_CDMA1_start  & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x10 0x" + f"{(CDMA1_len          & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x11 0x" + f"{(DMA0_START_DDR     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x12 0x" + f"{(DMA0_SG            & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x13 0x" + f"{(DMA0_len           & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x14 0x" + f"{(DMA1_START_DDR     & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x15 0x" + f"{(DMA1_SG            & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x16 0x" + f"{(DMA1_len           & 0xFFFFFFFF):08x}"+"\n")



    DMA0_MM2S_START = DMA0_SG + DMA0_S2MM_len
    DMA1_MM2S_START = DMA1_SG + DMA1_S2MM_len

    with open(SA_file1, 'w') as f1:
        f1.write(f"; --- SEGMENT 1 ---" +"\n")
        f1.write("x1 0x" + f"{(CDMA0_reg_base          & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(CDMA1_reg_base          & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0x00001008              & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0x00001000              & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(SGMEM_CDMA0_start       & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(SGMEM_CDMA1_start       & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((SGMEM_CDMA0_start + CDMA0_len -64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((SGMEM_CDMA1_start + CDMA1_len -64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x29 0x" + f"{(0x00000000             & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x30 0x" + f"{(0xFF005001             & 0xFFFFFFFF):08x}"+"\n")
        f1.write(f"; --- SEGMENT 2 ---" +"\n")
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
        f1.write("x29 0x" +  f"{(0xfff0fff0 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x30 0x" +  f"{(0xfff0fff0 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x31 0x" +  f"{(0xfff0fff0 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x28 0x" +  f"{(0xfff0fff0 & 0xFFFFFFFF):08x}"+"\n")

    asm_generate.main_S()
    #loop.main()
    print("1")
    translator.SA()
    print("2")
    merge_mif_files.SG()
    merge_mif_files.SA()
    SGMEM_CDMA0_start =   SGMEM_CDMA0_start + CDMA0_len 
    SGMEM_CDMA1_start =   SGMEM_CDMA1_start + CDMA1_len 
    ALL_SG_strat_DDR  =   ALL_SG_strat_DDR  + CDMA0_len + CDMA1_len + DMA0_len + DMA1_len


SGMEM_CDMA0_start     = 0xF4000000
SGMEM_CDMA1_start     = 0xF4200000
SGMEM_DMA0_BASE      = 0xF4400000
SGMEM_DMA1_BASE      = 0xF4600000
SGMEM_DMA2_BASE      = 0xF4800000
SGMEM_DMA3_BASE      = 0xF4A00000
SGMEM_DMA4_BASE      = 0xF4C00000
SGMEM_DMA5_BASE      = 0xF4E00000
SGMEM_DMA6_BASE      = 0xF5000000
SGMEM_DMA7_BASE      = 0xF5200000
SGMEM_ETH_DMA0       = 0xF5400000
SGMEM_ETH_DMA1       = 0xF5600000
SGMEM_ETH_DMA2       = 0xF5800000
SGMEM_ETH_DMA3       = 0xF5A00000
SGMEM_ETH_DMA4       = 0xF5C00000

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
DMA8_config      = 0xFF002000
DMA9_config      = 0xFF002400
DMA10_config     = 0xFF002800
DMA11_config     = 0xFF002C00

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

ALL_SG_descriptors = []
ALL_SG_strat_DDR   = 0x40000000

def main(START = 0x00000800):

    ALL_SG_LENTH = START
    global ALL_SG_descriptors
    global SGMEM_CDMA0_start
    global SGMEM_CDMA1_start
    global ALL_SG_strat_DDR
    global DDR0_START
    global DDR1_START

    bin_str = '1000'
    DDR0_START = DDR0_START + START

    script_dir = os.path.dirname(os.path.abspath(__file__))
    name0 = "ROM"
    name1 = "GM0"
    name2 = "GM1"
    name3 = "A_GM0"
    name4 = "B_GM1"
    mif_dir = os.path.join(script_dir,"mif")
    matrix_dir = os.path.join(script_dir,"matrix")
    rom_file0 = os.path.join(mif_dir, f"{name0}.mif")
    rom_file1 = os.path.join(mif_dir, f"{name1}.mif")
    rom_file2 = os.path.join(mif_dir, f"{name2}.mif")
    matrix_file0 = os.path.join(mif_dir, f"{name3}.mif")
    matrix_file1 = os.path.join(mif_dir, f"{name4}.mif")
    with open(rom_file0, 'w') as f:
        f.write("")
    with open(rom_file1, 'w') as f:
        f.write("")
    with open(rom_file2, 'w') as f:
        f.write("")
    with open(matrix_file0, 'w') as f:
        f.write("")
    with open(matrix_file1, 'w') as f:
        f.write("")
    txt_dir = os.path.join(script_dir,"txt")
    all_file = os.path.join(txt_dir, f"allsg.txt")

    print("Number of SG descriptors: ",int(ALL_SG_LENTH/64))
    
    if bin_str[0] == '1':
        op_SA(DDR0_START = DDR0_START , DDR1_START = DDR1_START, CDMA0_reg_base= CDMA0_config, CDMA1_reg_base= CDMA1_config,MPU_ID = 0)
    
    if bin_str[1] == '1':
        op_SA(DDR0_START = DDR0_START , DDR1_START = DDR1_START, CDMA0_reg_base= CDMA0_config, CDMA1_reg_base= CDMA1_config,MPU_ID = 1)
  
    if bin_str[2] == '1':
        op_SA(DDR0_START = DDR0_START , DDR1_START = DDR1_START, CDMA0_reg_base= CDMA0_config, CDMA1_reg_base= CDMA1_config,MPU_ID = 2)
    
    if bin_str[3] == '1':
        op_SA(DDR0_START = DDR0_START , DDR1_START = DDR1_START, CDMA0_reg_base= CDMA0_config, CDMA1_reg_base= CDMA1_config, MPU_ID = 3)
   
    
    sg_lenth = int(ALL_SG_strat_DDR) - int(0x40000000)
    allSGdescriptors = int(ALL_SG_LENTH/64)
    if(allSGdescriptors >= int(sg_lenth/64)):
        print("There is no need to add space to the SG descriptor")
    else:
        print("Need to add space to the SG descriptor")

    #print(f'{sg_start:08x}')
    descriptorss = []
    alllen = int(int(ALL_SG_LENTH/64) - int(sg_lenth/64))
    #print(int(A_DATA_START/64))
    #print(int(sg_lenth/64))
    for i in range(alllen):
        A = 0
        word = make_sg_dma_descriptor(A,A,A,A)
        descriptorss.append(word)
    deadata = flat(descriptorss)
    AL = ALL_SG_descriptors + deadata
    write_txt_file(AL , all_file)

    

if __name__ == "__main__":
    main(START = 0x00004000)



      
