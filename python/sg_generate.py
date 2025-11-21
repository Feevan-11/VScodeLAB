import os

def make_sg_cdma_descriptor(
    next_desc_addr,
    src_addr,
    dst_addr,
    length_bytes
):
    """
    构造一个 AXI CDMA SG 描述符(8个32位)，并返回一个长度为8的列表，每个元素是int(32位)。
    字段布局：
      Word0 (0x00): [5:0]=0, [31:6] = next_desc_addr >> 6
      Word1 (0x04): 0
      Word2 (0x08): src_addr
      Word3 (0x0C): 0
      Word4 (0x10): dst_addr
      Word5 (0x14): 0
      Word6 (0x18): [25:0] = length_bytes, [31:26]=0
      Word7 (0x1C): 0  (status word初始化为0)
    """
    # Word0: NEXTDESC (以 64 字节对齐地址 => bits[31:6] = next_desc_addr >> 6)
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
    构造一个 AXI CDMA SG 描述符(8个32位)，并返回一个长度为8的列表，每个元素是int(32位)。
    字段布局：
      Word0 (0x00): [5:0]=0, [31:6] = next_desc_addr >> 6
      Word1 (0x04): 0
      Word2 (0x08): src_addr
      Word3 (0x0C): 0
      Word4 (0x10): dst_addr
      Word5 (0x14): 0
      Word6 (0x18): [25:0] = length_bytes, [31:26]=0
      Word7 (0x1C): 0  (status word初始化为0)
    """
    # Word0: NEXTDESC (以 64 字节对齐地址 => bits[31:6] = next_desc_addr >> 6)
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
    将 32 位 int 转为长度 32 的二进制字符串(大端：bit31在左,bit0在右)。
    """
    return format(value & 0xFFFFFFFF, '032b')




def write_txt_file(words, filename):
    """
    将 words(每个元素是32位int) 写到 .txt 文件中，每行32位二进制，不加逗号或分号。
    """
    with open(filename, 'w') as f:
        for w in words:
            bin_str = int_to_bin32(w)
            hex_string = hex(int(bin_str, 2))
            f.write(hex_string+ "\n")

"""
def generate_cdma0_descriptors_for_matrix_A_IN(
    A_rows=64,
    A_cols=128,
    B_cols=64,
    block_width=16,
    Global_0_base=0x04000000,
    Shared_Men0_base=0x80000000,
    Shared_Men2_base=0x90000000,
    element_size=4
):
    
    #生成针对矩阵 A 的 SG 描述符列表(每个描述符8个word)，
    #假设 A 按行存储，大小 A_rows x A_cols，每次搬移 block_width 行(整列)。
    #目的地址在 dest0/dest1 之间来回切换。
    #返回值: descriptors_A, 其中 descriptors_A 是 [ [word0,word1,...], [word0,word1,...], ... ]
    
    descriptors = []
    # 总共有  (A_rows / block_width) 个子块 (不考虑整除余数)
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    # 每个子块: block_width 行, 每行 A_cols 个元素, each元素=4字节 => block_size_bytes
    block_size_bytes = block_width * A_cols * element_size

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
          A = i*Bnum_blocks + j
          # 源地址：基地址 + i* (block_width*A_cols*4)
          src_addr = Global_0_base + i * block_size_bytes
          #print(f'{src_addr:08x}')
          # 目的地址在 0x80000000 / 0x90000000 间交替
          dst_addr = Shared_Men0_base if (A % 2 == 0) else Shared_Men2_base
          # 先把 next_desc_addr 设为 0，后面再由主调函数统一处理链接
          next_desc_addr = 0
          if (A != 0):
              desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
              descriptors.append(desc_words)

    return descriptors
"""

def generate_cdma0_descriptors_for_matrix_A_IN(
    A_rows=64,
    A_cols=128,
    block_width=16,
    Global_0_base=0x00010000,
    Shared_Men0_base=0x80000000,
    element_size=2
):
    """
    生成针对矩阵 A 的 SG 描述符列表(每个描述符8个word)，
    假设 A 按行存储，大小 A_rows x A_cols，每次搬移 block_width 行(整列)。
    目的地址在 dest0/dest1 之间来回切换。
    返回值: descriptors_A, 其中 descriptors_A 是 [ [word0,word1,...], [word0,word1,...], ... ]
    """
    descriptors = []
    # 总共有  (A_rows / block_width) 个子块 (不考虑整除余数)
    Anum_blocks = A_rows // block_width

    # 每个子块: block_width 行, 每行 A_cols 个元素, each元素=4字节 => block_size_bytes
    block_size_bytes = block_width * A_cols * element_size

    for i in range(Anum_blocks):
       
        # 源地址：基地址 + i* (block_width*A_cols*4)
        src_addr = Global_0_base + i * block_size_bytes
        #print(f'{src_addr:08x}')
        # 目的地址在 0x80000000 / 0x90000000 间交替
        dst_addr = Shared_Men0_base + i * block_size_bytes
        # 先把 next_desc_addr 设为 0，后面再由主调函数统一处理链接
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
    """
    生成针对矩阵 A 的 SG 描述符列表(每个描述符8个word)，
    假设 A 按行存储，大小 A_rows x A_cols，每次搬移 block_width 行(整列)。
    目的地址在 dest0/dest1 之间来回切换。
    返回值: descriptors_A, 其中 descriptors_A 是 [ [word0,word1,...], [word0,word1,...], ... ]
    """
    descriptors = []
    # 总共有  (A_rows / block_width) 个子块 (不考虑整除余数)
    Bnum_blocks = B_cols // block_width

    # 每个子块: block_width 行, 每列 B_rows 个元素, each元素=2字节 => block_size_bytes
    block_size_bytes = block_width * B_rows * element_size

    for i in range(Bnum_blocks):
       
        # 源地址：基地址 + i* (block_width*A_cols*4)
        src_addr = Global_1_base + i * block_size_bytes
        #print(f'{src_addr:08x}')
        # 目的地址在 0x80000000 / 0x90000000 间交替
        dst_addr = Shared_Men1_base + i * block_size_bytes
        # 先把 next_desc_addr 设为 0，后面再由主调函数统一处理链接
        next_desc_addr = 0
        #if (i != 0):
        desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
        descriptors.append(desc_words)

    return descriptors

"""
def generate_cdma1_descriptors_for_matrix_B_IN(
    A_rows=64,
    B_rows=128,
    B_cols=64,
    block_width=16,
    Global_1_base=0x48000000,
    Shared_Men1_base=0x88000000,
    Shared_Men3_base=0x98000000,
    element_size=4
):
    
    #生成针对矩阵 B 的 SG 描述符列表(每个描述符8个word)，
    #假设 B 按“列存储”，大小 B_rows x B_cols，每次搬移 block_width 列(整行)。
    #目的地址在 dest0/dest1 之间来回切换。
    #返回值: descriptors_B, 其中 descriptors_B 是 [ [word0,word1,...], [word0,word1,...], ... ]
    
    descriptors = []
    # 总共有 (B_cols / block_width) 个子块
    Bnum_blocks = B_cols // block_width
    Anum_blocks = A_rows // block_width

    # 每个子块: B_rows 行, block_width 列, each元素=4字节 => block_size_bytes
    # 但 B 按列存储 => 第一个子块在地址 Global_1_base, 第二个子块相对地址 = block_width * B_rows * element_size
    block_size_bytes = B_rows * block_width * element_size

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
            B = i*Bnum_blocks + j
            # 源地址(列存储) = Global_1_base + j*(B_rows*block_width*4)
            src_addr = Global_1_base + j * block_size_bytes

            # 目的地址在 0x88000000 / 0x98000000 间交替
            dst_addr = Shared_Men1_base if (B % 2 == 0) else Shared_Men3_base

            # next_desc_addr 先写0，后面再统一更新
            next_desc_addr = 0
            if (B != 0):
                desc_words = make_sg_cdma_descriptor(next_desc_addr, src_addr, dst_addr, block_size_bytes)
                descriptors.append(desc_words)

    return descriptors
"""
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
    """
    生成针对矩阵 A 的 SG 描述符列表(每个描述符8个word)，
    假设 A 按行存储，大小 A_rows x A_cols，每次搬移 block_width 行(整列)。
    目的地址在 dest0/dest1 之间来回切换。
    返回值: descriptors_A, 其中 descriptors_A 是 [ [word0,word1,...], [word0,word1,...], ... ]
    """
    descriptors = []
    # 总共有  (A_rows / block_width) 个子块 (不考虑整除余数)
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    # 每个子块: block_width 行, 每行 A_cols 个元素, each元素=4字节 => block_size_bytes
    block_size_bytes = block_width * block_width * element_size
    src_addr_add = 0

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
          A = i*Bnum_blocks + j

          dst_addr = Global_0_base + A * block_size_bytes
          #print(f'{src_addr:08x}')
          src_addr = Shared_Men0_base if (A % 2 == 0) else Shared_Men2_base
          # 先把 next_desc_addr 设为 0，后面再由主调函数统一处理链接
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
    # 总共有 (B_cols / block_width) 个子块
    Bnum_blocks = B_cols // block_width
    Anum_blocks = A_rows // block_width

    # 每个子块: B_rows 行, block_width 列, each元素=4字节 => block_size_bytes
    # 但 B 按列存储 => 第一个子块在地址 Global_1_base, 第二个子块相对地址 = block_width * B_rows * element_size
    block_size_bytes = B_rows * block_width * element_size
    src_addr_add = 0

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
            B = i*Bnum_blocks + j
            # 源地址(列存储) = Global_1_base + j*(B_rows*block_width*4)
            dst_addr = Global_1_base + B * block_size_bytes

            # 目的地址在 0x88000000 / 0x98000000 间交替
            src_addr = Shared_Men1_base if (B % 2 == 0) else Shared_Men3_base
            src_addr = src_addr + src_addr_add
            # next_desc_addr 先写0，后面再统一更新
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
    element_size=2
):
    
    descriptors = []
    # 总共有  (A_rows / block_width) 个子块 (不考虑整除余数)
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    # 每个子块: block_width 行, 每行 A_cols 个元素, each元素=4字节 => block_size_bytes
    block_size_bytes = block_width * A_B * element_size + 0x0C000000
    block_size = block_width * A_B * element_size

    for i in range(Anum_blocks):
        BUFFER_addr = Shared_Men0_base + (i * block_size)
        for j in range(Bnum_blocks):
          # 源地址：基地址 + i* (block_width*A_cols*4)
          next_desc_addr = 0
          '''
          if(i*Bnum_blocks + j == 0):
          #if((i*Bnum_blocks + j)%16 == 0):
              block_size_bytes = block_width * block_width * element_size + 0x08000000
          #elif((i*Bnum_blocks + j)%16 == 15):  
          elif(i*Bnum_blocks + j == Anum_blocks *Bnum_blocks - 1):
              block_size_bytes = block_width * block_width * element_size + 0x04000000
          else:
              block_size_bytes = block_width * block_width * element_size
          '''
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words)

    return descriptors

def generate_dma1_descriptors_for_MM2S(
    A_rows=64,
    A_B=128,
    B_cols=64,
    block_width=16,
    Shared_Men1_base=0x88000000,
    element_size=2
):
    
    descriptors = []
    # 总共有  (A_rows / block_width) 个子块 (不考虑整除余数)
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    # 每个子块: block_width 行, 每行 A_cols 个元素, each元素=4字节 => block_size_bytes
    block_size_bytes = block_width * A_B * element_size + 0x0C000000
    block_size = block_width * A_B * element_size

    for i in range(Anum_blocks):
        
        for j in range(Bnum_blocks):
          # 源地址：基地址 + i* (block_width*A_cols*4)
          BUFFER_addr = Shared_Men1_base + (j * block_size) 
          next_desc_addr = 0
          '''
          if(i*Bnum_blocks + j == 0):
          #if((i*Bnum_blocks + j)%16 == 0):
              block_size_bytes = block_width * block_width * element_size + 0x08000000
          #elif((i*Bnum_blocks + j)%16 == 15):  
          elif(i*Bnum_blocks + j == Anum_blocks *Bnum_blocks - 1):
              block_size_bytes = block_width * block_width * element_size + 0x04000000
          else:
              block_size_bytes = block_width * block_width * element_size
          '''
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          descriptors.append(desc_words)

    return descriptors

def generate_dma0_descriptors_for_S2MM(
    A_rows=64,
    B_cols=64,
    block_width=16,
    Shared_Men2_base=0x90000000,
    element_size=2
):

    descriptors = []
    # 总共有  (A_rows / block_width) 个子块 (不考虑整除余数)
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    # 每个子块: block_width 行, 每行 A_cols 个元素, each元素=4字节 => block_size_bytes
    block_size_bytes = block_width * block_width * element_size + 0x0C000000
    addr = 0

    for i in range(Anum_blocks):

        for j in range(Bnum_blocks):
          BUFFER_addr = Shared_Men2_base + addr
          next_desc_addr = 0
          '''
          if((i*Bnum_blocks + j)%16 == 0):
              block_size_bytes = block_width * block_width * element_size + 0x08000000
          elif((i*Bnum_blocks + j)%16 == 15):  
          #elif(i*Bnum_blocks + j == Anum_blocks *Bnum_blocks - 1):
              block_size_bytes = block_width * block_width * element_size + 0x04000000
          else:
              block_size_bytes = block_width * block_width * element_size
              '''
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          addr = addr + 512
          descriptors.append(desc_words)

    return descriptors

def generate_dma1_descriptors_for_S2MM(
    A_rows=64,
    B_cols=64,
    block_width=16,
    Shared_Men3_base=0x98000000,
    element_size=2
):

    descriptors = []
    # 总共有  (A_rows / block_width) 个子块 (不考虑整除余数)
    Anum_blocks = A_rows // block_width
    Bnum_blocks = B_cols // block_width

    # 每个子块: block_width 行, 每行 A_cols 个元素, each元素=4字节 => block_size_bytes
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
          elif((i*Bnum_blocks + j)%16 == 15):  
          #elif(i*Bnum_blocks + j == Anum_blocks *Bnum_blocks - 1):
              block_size_bytes = block_width * block_width * element_size + 0x04000000
          else:
              block_size_bytes = block_width * block_width * element_size'
          '''
          desc_words = make_sg_dma_descriptor(next_desc_addr, BUFFER_addr, block_size_bytes)
          addr = addr + 512
          descriptors.append(desc_words)

    return descriptors

def link_descriptors_in_memory(descriptor_list, base_addr=0x00000000, desc_size=64):
    """
    给定一组描述符(每个是16个word)，我们想象它们顺序存放在内存中，从 base_addr 开始，
    每个描述符大小 64 字节(16 word×4字节)。本函数会根据顺序更新
    每条描述符的 Word0，使其指向下一条描述符地址(除了最后一条=0)。
    最后返回 "flattened" 形式的一串 32位字(按描述符顺序存放)。
    """

    flattened = []  # 存放最终按顺序展开的 32位word

    for i in range(len(descriptor_list)):

        # 计算下一条描述符的起始物理地址
        if i < len(descriptor_list) - 1:
            next_desc_addr = base_addr + (i + 1) * desc_size
        else:
            next_desc_addr = base_addr

        # 更新当前描述符的 Word0
        words = descriptor_list[i]
        # Word0 = bits[31:6] = next_desc_addr >> 6
        #w0_rest = (next_desc_addr<<6) & 0xFFFFFFC0
        words[0] = next_desc_addr

        # 把更新完的16 word展平放到 flattened
        flattened.extend(words)

    return flattened

def flat(descriptor_list):
    flattened = []  # 存放最终按顺序展开的 32位word

    for i in range(len(descriptor_list)):
        words = descriptor_list[i]
        flattened.extend(words)

    return flattened

def op(A__ROWS=16,A__COLS=16,B__ROWS=16,B__COLS=16,A_DATA_START = 0x40010000):

    A_ROWS = A__ROWS
    A_COLS = A__COLS
    B_ROWS = B__ROWS
    B_COLS = B__COLS
    # 1) 生成 A、B 对应的描述符列表
    descriptors_A_IN = generate_cdma0_descriptors_for_matrix_A_IN(
        A_rows=A_ROWS,
        A_cols=A_COLS,
        block_width=16,
        Global_0_base=A_DATA_START,
        Shared_Men0_base=0x80008000,
        element_size=2
    )
    descriptors_B_IN = generate_cdma1_descriptors_for_matrix_B_IN(
        B_rows=B_ROWS,
        B_cols=B_COLS,
        block_width=16,
        Global_1_base=0x80000800,
        Shared_Men1_base=0x40008000,
        element_size=2
    )
    #descriptors_A_OUT = generate_cdma0_descriptors_for_matrix_A_OUT(
    #    A_rows=A_ROWS,
    #    A_cols=A_COLS,
    #    B_cols=B_COLS,
    #    block_width=16,
    #    Global_0_base=0x24000000,
    #    Shared_Men0_base=0x84000000,
    #    Shared_Men2_base=0x94000000,
    #    element_size=2
    #)
    #descriptors_B_OUT = generate_cdma1_descriptors_for_matrix_B_OUT(
    #    A_rows=A_ROWS,
    #    B_rows=B_ROWS,
    #    B_cols=B_COLS,
    #    block_width=16,
    #    Global_1_base=0x68000000,
    #    Shared_Men1_base=0x8C000000,
    #    Shared_Men3_base=0x9C000000,
    #    element_size=2
    #)
    #descriptors_A = descriptors_A_IN + descriptors_A_OUT
    #descriptors_B = descriptors_B_IN + descriptors_B_OUT
    descriptors_A = descriptors_A_IN
    descriptors_B = descriptors_B_IN

    descriptors_DMA0_S2MM = generate_dma0_descriptors_for_S2MM(
        A_rows=A_ROWS,
        B_cols=B_COLS,
        block_width=16,
        Shared_Men2_base=0x40005000,
        element_size=2
    )
    descriptors_DMA1_S2MM = generate_dma1_descriptors_for_S2MM(
        A_rows=A_ROWS,
        B_cols=B_COLS,
        block_width=16,
        Shared_Men3_base=0x80005000,
        element_size=2
    )
    descriptors_DMA0_MM2S = generate_dma0_descriptors_for_MM2S(
        A_rows=A_ROWS,
        A_B = B_ROWS,
        B_cols=B_COLS,
        block_width=16,
        Shared_Men0_base=0x40001000,
        element_size=2
    )
    descriptors_DMA1_MM2S = generate_dma1_descriptors_for_MM2S(
        A_rows=A_ROWS,
        A_B = B_ROWS,
        B_cols=B_COLS,
        block_width=16,
        Shared_Men1_base=0x80000880,
        element_size=2
    )

    # 2) 给这两份描述符列表分别创建“内存中线性存放”布局，并将 Word0 指向下一描述符
    #    这里假设 CDMA0的描述符从 0x00000000 开始, CDMA1的描述符从 0x00100000 开始 (示例)
    DMA0_SG_BASE = 0xF5A00000
    DMA1_SG_BASE = 0xF5C00000
    CDMA0_SG_BASE = 0xF4000000
    CDMA1_SG_BASE = 0xF4200000
    cdma0_base = CDMA0_SG_BASE
    cdma1_base = CDMA1_SG_BASE
    dma0_S2MM =  DMA0_SG_BASE
    dma1_S2MM =  DMA1_SG_BASE
    ADD = int(A_ROWS/16) * int(B_COLS/16) * 64
    #print('ADD',ADD)
    dma0_MM2S =  dma0_S2MM + ADD
    dma1_MM2S =  dma1_S2MM + ADD

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

    STAR = 0
    CDMA0len = 64*len(descriptors_A)
    CDMA1len = 64*len(descriptors_B)
    DMA0_S2MMlen = 64*len(descriptors_DMA0_S2MM)
    DMA0_MM2Slen = 64*len(descriptors_DMA0_MM2S)
    DMA0len = 64*(len(descriptors_DMA0_MM2S)+len(descriptors_DMA0_S2MM))
    DMA1len = 64*(len(descriptors_DMA1_MM2S)+len(descriptors_DMA1_S2MM))

    descriptorss = []
    A_DATA_START = int(A_DATA_START) - int(0x40000000) 
    print(int(A_DATA_START/64))
    alllen = int(int(A_DATA_START/64) - (CDMA0len + CDMA1len + DMA0len + DMA1len)/64)
    for i in range(alllen):
        A = 0
        word = make_sg_dma_descriptor(A,A,A)
        descriptorss.append(word)
    deadata = flat(descriptorss)
    AL = ALL + deadata
    write_txt_file(AL , all_file)
    #print("all:",len(descriptorss))
    print(" CDMA0 descriptors STAR:", STAR,"        Lenth:",f"{CDMA0len:08x}")
    print(" CDMA1 descriptors STAR:", f"{CDMA0len:08x}"," Lenth:",f"{CDMA1len:08x}")
    print(" DMA  S  2  M  M   STAR:", 0,"         tail:",f"{(DMA0_S2MMlen-64):08x}")
    print(" DMA  M  M  2  S   STAR:", f"{(DMA0_S2MMlen):08x}","  tail:",f"{(DMA0_S2MMlen + DMA0_MM2Slen-64):08x}")
    print(" DMA0 descriptors  STAR:", f"{(CDMA0len + CDMA1len):08x}"," Lenth:",f"{DMA0len:08x}")
    print(" DMA1 descriptors  STAR:", f"{(CDMA0len + CDMA1len + DMA0len):08x}"," Lenth:",f"{DMA1len:08x}")
    #print("[INFO] Successfully generated  cdma0_sg.txt  / cdma1_sg.txt")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name0 = "ROM"
    name1 = "GM1"
    txt_dir = os.path.join(script_dir,"txt")

    ROM_file0 = os.path.join(txt_dir, f"{name0}.txt")
    GM1_file1 = os.path.join(txt_dir, f"{name1}.txt")

    #reg_values0 = read_reg_values(txt_file0)
    #reg_values1 = read_reg_values(txt_file1)    
    
    DMA0_BASE = 0xFF003C00
    DMA1_BASE = 0xFF004000
    CDMA0_BASE = 0xFF004400
    CDMA1_BASE = 0xFF004440
    cdma0_sg_start = 0x40000000
    cdma1_sg_start = cdma0_sg_start + CDMA0len
    dma0_sg_start = cdma1_sg_start + CDMA1len
    dma1_sg_start = dma0_sg_start + DMA0len
    with open(ROM_file0, 'w') as f0:
        f0.write("; --- SEGMENT 1 ---" +"\n")
        f0.write("x1 0x" + f"{(CDMA0_BASE & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x2 0x" + f"{(CDMA1_BASE & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x3 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x4 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x5 0x" + f"{(cdma0_sg_start & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x6 0x" + f"{(CDMA0_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x7 0x" + f"{(0x80000000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x8 0x" + f"{(0xF0001000 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x9 0x" + f"{(CDMA0len & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x10 0x" + f"{(0x00000800 & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x11 0x" + f"{(cdma1_sg_start & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x12 0x" + f"{(CDMA1_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x13 0x" + f"{(CDMA1len & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x14 0x" + f"{(dma0_sg_start & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x15 0x" + f"{(DMA0_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x16 0x" + f"{(DMA0len & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x17 0x" + f"{(dma1_sg_start & 0xFFFFFFFF):08x}"+"\n")
        f0.write("x18 0x" + f"{(DMA1_SG_BASE & 0xFFFFFFFF):08x}"+"\n")


    with open(GM1_file1, 'w') as f1:
        #f1.write("; --- SEGMENT 1 ---" +"\n")
        #f1.write("x5 0x" + f"{(0x00400000 & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x6 0x" + f"{(0x80000000 & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x7 0x" + f"{(0x40000800 & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x8 0x" + f"{(0x88000000 & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x9 0x" + f"{((16*A_COLS*2) & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x10 0x" + f"{((16*A_COLS*2) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("; --- SEGMENT 1 ---" +"\n")
        f1.write("x1 0x" + f"{(CDMA0_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(CDMA1_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(0x00001008 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x5 0x" + f"{(CDMA0_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(CDMA1_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((CDMA0_SG_BASE+CDMA0len-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((CDMA1_SG_BASE+CDMA0len-64) & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("; --- SEGMENT 2 ---" +"\n")
        #f1.write("x1 0x" + f"{(DMA0_BASE & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x2 0x" + f"{(DMA1_BASE & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x3 0x" + f"{(DMA0_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x4 0x" + f"{(DMA1_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        #sgbbt = len(descriptors_DMA0_S2MM) << 16
        #sgbbt = sgbbt + 0x1001
        #f1.write("x5 0x" + f"{(sgbbt & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x7 0x" + f"{((DMA0_SG_BASE+DMA0_S2MMlen-64) & 0xFFFFFFFF):08x}"+"\n")
        #f1.write("x8 0x" + f"{((DMA1_SG_BASE+DMA0_S2MMlen-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("; --- SEGMENT 2 ---" +"\n")
        f1.write("x1 0x" + f"{(DMA0_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x2 0x" + f"{(DMA1_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x3 0x" + f"{(DMA0_SG_BASE+DMA0_S2MMlen & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x4 0x" + f"{(DMA1_SG_BASE+DMA0_S2MMlen & 0xFFFFFFFF):08x}"+"\n")
        sgbbt1 = len(descriptors_DMA0_MM2S) << 16
        sgbbt1 = sgbbt1 + 0x1001
        f1.write("x5 0x" + f"{(sgbbt1 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x6 0x" + f"{(0x00001000 & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x7 0x" + f"{((DMA0_SG_BASE+DMA0_MM2Slen+DMA0_S2MMlen-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x8 0x" + f"{((DMA1_SG_BASE+DMA0_MM2Slen+DMA0_S2MMlen-64) & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x11 0x" + f"{(DMA0_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x12 0x" + f"{(DMA1_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x13 0x" + f"{(DMA0_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
        f1.write("x14 0x" + f"{(DMA1_SG_BASE & 0xFFFFFFFF):08x}"+"\n")
def main(AROWS = 32,AB =32,BCOLS = 32):
    A_ROWS = AROWS
    A_B = AB
    B_COLS = BCOLS
    A_DATA_START = 0x40001000
    
    op(A__ROWS = A_ROWS,A__COLS = A_B,B__ROWS = A_B,B__COLS = B_COLS,A_DATA_START = A_DATA_START)

if __name__ == "__main__":
    main(AROWS = 32,AB =32,BCOLS = 32)
