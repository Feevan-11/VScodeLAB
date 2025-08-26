import os

def sign_extend(value, bits):
    """
    Do a symbolic extension of value, assuming that value is at most bits.
    If the highest bit is 1, it indicates that it is a negative number and is processed as a complement.
    """
    sign_bit = 1 << (bits - 1)
    mask = (1 << bits) - 1
    value &= mask
    if value & sign_bit:
        
        value = value - (1 << bits)
    return value

def encode_addi(rd, rs1, imm):
    """
    addi xrd, xrs1, imm
    I ： imm[11:0], rs1, funct3=0, rd, opcode=0x13
    31:20=imm, 19:15=rs1, 14:12=funct3=0, 11:7=rd, 6:0=opcode=0x13
    """
    # 12 bit symbolic extension
    imm_12 = imm & 0xFFF  
    
    opcode = 0x13
    funct3 = 0x0
    machine = ((imm_12 & 0xFFF) << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_beq(rs1, rs2, imm):
    """
    beq xrs1, xrs2, imm
    B-type: imm[12|10:5], rs2, rs1, funct3=0, imm[4:1|11], opcode=0x63
    立即数处理：B-type指令的立即数是13位有符号数（以字节为单位，但偏移必须是偶数）
    """
    # 检查偏移量是否对齐（必须为2的倍数）
    if imm % 2 != 0:
        raise ValueError(f"BEQ offset must be even, got {imm}")
    
    # 转换为半字偏移量（除2）
    offset = imm // 2
    
    # 检查偏移范围（-4096到4094半字，即-8192到8188字节）
    if not (-4096 <= offset <= 4094):
        raise ValueError(f"BEQ offset out of range: {offset} half-words")
    
    # 提取立即数的各个部分
    imm_12 = (offset >> 11) & 0x1   # 最高位（第12位）
    imm_11 = (offset >> 10) & 0x1   # 第11位
    imm_10_5 = (offset >> 4) & 0x3F # 第10~5位（6位）
    imm_4_1 = (offset >> 0) & 0x0F  # 第4~1位（4位）
    
    # 合并高位立即数部分
    imm_31_25 = (imm_12 << 6) | imm_10_5  # [31:25] = {imm[12], imm[10:5]}
    
    opcode = 0x63
    funct3 = 0x0
    
    # 组合机器码
    machine = (imm_31_25 << 25) | (rs2 << 20) | (rs1 << 15) | (funct3 << 12) | (imm_4_1 << 8)  | (imm_11 << 7)  | opcode
              
    return machine

def encode_lui(rd, imm):
    """
    lui xrd, imm
    U ： imm[31:12], rd, opcode=0x37

    """
    opcode = 0x37

    imm_20 = (imm & 0xFFFFF)  # save 20 bits
    machine = (imm_20 << 12) | (rd << 7) | opcode
    return machine

def encode_and(rd, rs1, rs2):
    """
    and xrd, xrs1, xrs2
    R type： funct7=0x00, rs2, rs1, funct3=0x7, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x7
    funct7 = 0x00
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_sw(rs2, rs1, imm):
    """
    sw xrs2, offset(xrs1)
    S type： imm[11:5], rs2, rs1, funct3=2, imm[4:0], opcode=0x23
    """
    opcode = 0x23
    funct3 = 0x2
    imm_12 = imm & 0xFFF
    imm_11_5 = (imm_12 >> 5) & 0x7F
    imm_4_0  = imm_12 & 0x1F
    machine = (imm_11_5 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (imm_4_0 << 7) \
              | opcode
    return machine

def encode_add(rd, rs1, rs2):
    """
    add xrd, xrs1, xrs2
    R type： funct7=0x00, rs2, rs1, funct3=0x0, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x0
    funct7 = 0x00
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_sub(rd, rs1, rs2):
    """
    sub xrd, xrs1, xrs2
    R type： funct7=0x20, rs2, rs1, funct3=0x0, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x0
    funct7 = 0x20
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_xor(rd, rs1, rs2):
    """
    xor xrd, xrs1, xrs2
    R type： funct7=0x00, rs2, rs1, funct3=0x4, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x4
    funct7 = 0x00
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_or(rd, rs1, rs2):
    """
    or xrd, xrs1, xrs2
    R type： funct7=0x00, rs2, rs1, funct3=0x6, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x6
    funct7 = 0x00
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_sll(rd, rs1, rs2):
    """
    sll xrd, xrs1, xrs2
    R type： funct7=0x00, rs2, rs1, funct3=0x1, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x1
    funct7 = 0x00
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_srl(rd, rs1, rs2):
    """
    srl xrd, xrs1, xrs2
    R type： funct7=0x00, rs2, rs1, funct3=0x5, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x5
    funct7 = 0x00
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_sra(rd, rs1, rs2):
    """
    sra xrd, xrs1, xrs2
    R type： funct7=0x20, rs2, rs1, funct3=0x5, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x5
    funct7 = 0x20
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_slt(rd, rs1, rs2):
    """
    slt xrd, xrs1, xrs2
    R type： funct7=0x00, rs2, rs1, funct3=0x2, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x2
    funct7 = 0x00
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_sltu(rd, rs1, rs2):
    """
    sltu xrd, xrs1, xrs2
    R type： funct7=0x00, rs2, rs1, funct3=0x3, rd, opcode=0x33
    """
    opcode = 0x33
    funct3 = 0x3
    funct7 = 0x00
    machine = (funct7 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_xori(rd, rs1, imm):
    """
    xori xrd, xrs1, imm
    I type： imm[11:0], rs1, funct3=0x4, rd, opcode=0x13
    """
    opcode = 0x13
    funct3 = 0x4
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_ori(rd, rs1, imm):
    """
    ori xrd, xrs1, imm
    I type： imm[11:0], rs1, funct3=0x6, rd, opcode=0x13
    """
    opcode = 0x13
    funct3 = 0x6
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_andi(rd, rs1, imm):
    """
    andi xrd, xrs1, imm
    I type： imm[11:0], rs1, funct3=0x7, rd, opcode=0x13
    """
    opcode = 0x13
    funct3 = 0x7
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_slli(rd, rs1, shamt):
    """
    slli xrd, xrs1, shamt
    I type： shamt[4:0], rs1, funct3=0x1, rd, opcode=0x13
    """
    opcode = 0x13
    funct3 = 0x1
    shamt_5 = shamt & 0x1F
    machine = (shamt_5 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_srli(rd, rs1, shamt):
    """
    srli xrd, xrs1, shamt
    I type： shamt[4:0], rs1, funct3=0x5, rd, opcode=0x13
    """
    opcode = 0x13
    funct3 = 0x5
    shamt_5 = shamt & 0x1F
    machine = (shamt_5 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_srai(rd, rs1, shamt):
    """
    srai xrd, xrs1, shamt
    I type： shamt[4:0], rs1, funct3=0x5, rd, opcode=0x13
    funct7=0x20
    """
    opcode = 0x13
    funct3 = 0x5
    shamt_5 = shamt & 0x1F
    funct7 = 0x20
    machine = (funct7 << 25) \
              | (shamt_5 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_slti(rd, rs1, imm):
    """
    slti xrd, xrs1, imm
    I type： imm[11:0], rs1, funct3=0x2, rd, opcode=0x13
    """
    opcode = 0x13
    funct3 = 0x2
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_sltiu(rd, rs1, imm):
    """
    sltiu xrd, xrs1, imm
    I type： imm[11:0], rs1, funct3=0x3, rd, opcode=0x13
    """
    opcode = 0x13
    funct3 = 0x3
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_lb(rd, rs1, imm):
    """
    lb xrd, offset(xrs1)
    I type： imm[11:0], rs1, funct3=0x0, rd, opcode=0x03
    """
    opcode = 0x03
    funct3 = 0x0
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_lw(rd, rs1, imm):
    """
    lw xrd, offset(xrs1)
    I type： imm[11:0], rs1, funct3=0x1, rd, opcode=0x03
    """
    opcode = 0x03
    funct3 = 0x2
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_lh(rd, rs1, imm):
    """
    lh xrd, offset(xrs1)
    I type： imm[11:0], rs1, funct3=0x1, rd, opcode=0x03
    """
    opcode = 0x03
    funct3 = 0x1
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_lbu(rd, rs1, imm):
    """
    lbu xrd, offset(xrs1)
    I type： imm[11:0], rs1, funct3=0x4, rd, opcode=0x03
    """
    opcode = 0x03
    funct3 = 0x4
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_lhu(rd, rs1, imm):
    """
    lhu xrd, offset(xrs1)
    I type： imm[11:0], rs1, funct3=0x5, rd, opcode=0x03
    """
    opcode = 0x03
    funct3 = 0x5
    imm_12 = imm & 0xFFF
    machine = (imm_12 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_sb(rs2, rs1, imm):
    """
    sb xrs2, offset(xrs1)
    S type： imm[11:5], rs2, rs1, funct3=0x0, imm[4:0], opcode=0x23
    """
    opcode = 0x23
    funct3 = 0x0
    imm_12 = imm & 0xFFF
    imm_11_5 = (imm_12 >> 5) & 0x7F
    imm_4_0  = imm_12 & 0x1F
    machine = (imm_11_5 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (imm_4_0 << 7) \
              | opcode
    return machine

def encode_sh(rs2, rs1, imm):
    """
    sh xrs2, offset(xrs1)
    S type： imm[11:5], rs2, rs1, funct3=0x1, imm[4:0], opcode=0x23
    """
    opcode = 0x23
    funct3 = 0x1
    imm_12 = imm & 0xFFF
    imm_11_5 = (imm_12 >> 5) & 0x7F
    imm_4_0  = imm_12 & 0x1F
    machine = (imm_11_5 << 25) \
              | (rs2 << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (imm_4_0 << 7) \
              | opcode
    return machine

def encode_auipc(rd, imm):
    """
    auipc xrd, imm
    U type： imm[31:12], rd, opcode=0x17
    """
    opcode = 0x17
    imm_20 = (imm & 0xFFFFF)  # 只保留 20 bits
    machine = (imm_20 << 12) | (rd << 7) | opcode
    return machine


def encode_setup(rd, imm):
    """
    setup xrd, offset
    """
    opcode = 0x0B

    imm_12 = imm & 0xFFF  

    funct3 = 0x0
    rs1 = 0b00000
    machine = ((imm_12 & 0xFFF) << 20) \
              | (rs1 << 15) \
              | (funct3 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def encode_goto(rd, imm):
    """
    j xrd, offset
    J type:
      imm[20], imm[10:1], imm[11], imm[19:12], rd, opcode=0x0B
    """
    opcode = 0x2B
    imm_21 = imm & 0x1FFFFF

    imm_20   = (imm_21 >> 20) & 0x1
    imm_10_1 = (imm_21 >> 1) & 0x3FF
    imm_11   = (imm_21 >> 11) & 0x1
    imm_19_12= (imm_21 >> 12) & 0xFF

    machine = (imm_20 << 31) \
              | (imm_10_1 << 21) \
              | (imm_11 << 20) \
              | (imm_19_12 << 12) \
              | (rd << 7) \
              | opcode
    return machine

def reg_index(reg_str):
    """
     turn 'x3' to 3；
    """
    reg_str = reg_str.strip()
    if reg_str.startswith('x'):
        idx = int(reg_str[1:])
        if 0 <= idx < 32:
            return idx
    raise ValueError(f"Invalid register name: {reg_str}")

def parse_one_instruction(line):


    parts = line.replace(',', '').split()
    if not parts:
        return None

    inst = parts[0].lower()
    if inst == 'addi':
        #  addi x1, x2, imm
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        imm = int(parts[3], 0) 

        imm = sign_extend(imm, 12)
        return encode_addi(rd, rs1, imm)

    elif inst == 'lui':
        #  lui x1, imm
        if len(parts) != 3:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        imm = int(parts[2], 0)

        imm = sign_extend(imm, 20)
        return encode_lui(rd, imm)

    elif inst == 'and':
        #  and x1, x2, x3
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_and(rd, rs1, rs2)

    elif inst == 'sw':
        #  sw x2, 8(x3)
        if len(parts) != 3:
            raise ValueError(f"erro: {line}")
        rs2_str = parts[1]  # x2
        offset_part = parts[2]  # 8(x3)

        offset_str, base_str = offset_part.split('(')
        base_str = base_str.replace(')', '')
        
        rs2 = reg_index(rs2_str)
        rs1 = reg_index(base_str)
        imm = int(offset_str, 0)

        imm = sign_extend(imm, 12)
        return encode_sw(rs2, rs1, imm)

    elif inst == 'lp.setup':
        #  lp.setup x5, 200
        if len(parts) != 3:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        imm = int(parts[2], 0)

        imm = sign_extend(imm, 12)
        return encode_setup(rd, imm)
    
    elif inst == 'lp.goto':
        #  lp.goto x5, 200
        if len(parts) != 3:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        imm = int(parts[2], 0)

        imm = sign_extend(imm, 21)
        return encode_goto(rd, imm)
    
    elif inst == 'beq':
        # beq rs1, rs2, offset
        if len(parts) != 4:
            raise ValueError(f"Invalid BEQ format: {line}")
        
        rs1 = reg_index(parts[1])
        rs2 = reg_index(parts[2])
        imm = int(parts[3], 0)  # 立即数可以是10进制或16进制
        
        # 符号扩展并检查范围
        imm = sign_extend(imm, 13)
        return encode_beq(rs1, rs2, imm)

    elif inst == 'add':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_add(rd, rs1, rs2)

    elif inst == 'sub':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_sub(rd, rs1, rs2)

    elif inst == 'xor':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_xor(rd, rs1, rs2)

    elif inst == 'or':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_or(rd, rs1, rs2)

    elif inst == 'sll':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_sll(rd, rs1, rs2)
    
    elif inst == 'srl':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_srl(rd, rs1, rs2)
    
    elif inst == 'sra':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_sra(rd, rs1, rs2)
    
    elif inst == 'slt':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_slt(rd, rs1, rs2)
    
    elif inst == 'sltu':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        rs2 = reg_index(parts[3])
        return encode_sltu(rd, rs1, rs2)

    elif inst == 'xori':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        imm = int(parts[3], 0)
        imm = sign_extend(imm, 12)
        return encode_xori(rd, rs1, imm)

    elif inst == 'ori':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        imm = int(parts[3], 0)
        imm = sign_extend(imm, 12)
        return encode_ori(rd, rs1, imm)

    elif inst == 'andi':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        imm = int(parts[3], 0)
        imm = sign_extend(imm, 12)
        return encode_andi(rd, rs1, imm)

    elif inst in ['slli', 'srli', 'srai']:
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        shamt = int(parts[3], 0)
        if not (0 <= shamt < 32):
            raise ValueError(f" {shamt} over (0-31)")
        if inst == 'slli':
            return encode_slli(rd, rs1, shamt)
        elif inst == 'srli':
            return encode_srli(rd, rs1, shamt)
        elif inst == 'srai':
            return encode_srai(rd, rs1, shamt)

    elif inst == 'slti':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        imm = int(parts[3], 0)
        imm = sign_extend(imm, 12)
        return encode_slti(rd, rs1, imm)

    elif inst == 'sltiu':
        if len(parts) != 4:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        rs1 = reg_index(parts[2])
        imm = int(parts[3], 0)
        imm = sign_extend(imm, 12)
        return encode_sltiu(rd, rs1, imm)

    elif inst in ['lb', 'lh', 'lbu', 'lhu','lw']:
        # lb x1, 8(x2)
        if len(parts) != 3:
            raise ValueError(f"erro: {line}")
        rd_str = parts[1]
        offset_part = parts[2]
        offset_str, base_str = offset_part.split('(')
        base_str = base_str.replace(')', '')
        
        rd = reg_index(rd_str)
        rs1 = reg_index(base_str)
        imm = int(offset_str, 0)
        imm = sign_extend(imm, 12)
        
        if inst == 'lb':
            return encode_lb(rd, rs1, imm)
        elif inst == 'lh':
            return encode_lh(rd, rs1, imm)
        elif inst == 'lbu':
            return encode_lbu(rd, rs1, imm)
        elif inst == 'lhu':
            return encode_lhu(rd, rs1, imm)
        elif inst == 'lw':
            return encode_lw(rd, rs1, imm)

    elif inst in ['sb', 'sh']:
        # sb x2, 8(x3)
        if len(parts) != 3:
            raise ValueError(f"erro: {line}")
        rs2_str = parts[1]
        offset_part = parts[2]
        offset_str, base_str = offset_part.split('(')
        base_str = base_str.replace(')', '')
        
        rs2 = reg_index(rs2_str)
        rs1 = reg_index(base_str)
        imm = int(offset_str, 0)
        imm = sign_extend(imm, 12)
        
        if inst == 'sb':
            return encode_sb(rs2, rs1, imm)
        elif inst == 'sh':
            return encode_sh(rs2, rs1, imm)

    elif inst == 'auipc':
        # auipc x1, 0x12345
        if len(parts) != 3:
            raise ValueError(f"erro: {line}")
        rd = reg_index(parts[1])
        imm = int(parts[2], 0)
        imm = sign_extend(imm, 20)
        return encode_auipc(rd, imm)
    
    else:
        raise ValueError(f"erro: {line}")

def int_to_little_endian_32bits(value):
    """
    Converts a 32-bit integer to a 32-bit binary string ('0'/'1') of 32 characters in small-endian mode.
    Order: First the lowest byte, then the lowest byte, then the highest byte.
    For example, 0x12345678 -> Byte order b8 b7 b6 b5 b4 b3 b2 b1
    Where b1=0x12, b2=0x34, b3=0x56, b4=0x78
    But at the binary level, we want b4, b3, b2, and b1 to be 8 bits each, right?
    """

    b0 = value & 0xff
    b1 = (value >> 8) & 0xff
    b2 = (value >> 16) & 0xff
    b3 = (value >> 24) & 0xff

    s0 = f"{b0:08b}"
    s1 = f"{b1:08b}"
    s2 = f"{b2:08b}"
    s3 = f"{b3:08b}"

    return s0 + s1 + s2 + s3

def int_to_little_endian_4bytes(value):


    b0 = value & 0xff
    b1 = (value >> 8) & 0xff
    b2 = (value >> 16) & 0xff
    b3 = (value >> 24) & 0xff
    return bytes([b0, b1, b2, b3])

def write_line_with_ending(f, line_content, is_last_line=False):
    """
     line_content write in f 
    if is_last_line=False，add (",\n")。
    if is_last_line=True，add (";\n")。
    """
    if is_last_line:
        f.write(line_content + ";\n")
    else:
        f.write(line_content + ",\n")

def process_mif(input_filename, output_filename):
    # Reads input files and preprocesses them
    try:
        with open(input_filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"error: file {input_filename} not found")
        return

    # Verify the formatting of each line
    valid_lines = []
    for idx, line in enumerate(lines, 1):
        if len(line) != 128:
            print(f"Line {idx} length error: It should be 128 bits, but it is {len(line)}")
            return
        if not all(c in {'0', '1'} for c in line):
            print(f"Line {idx} contains illegal characters")
            return
        valid_lines.append(line)

    # Combine binary data into 512-bit lines
    combined = []
    for i in range(0, len(valid_lines), 4):
        if i+3 < len(valid_lines):
            # Combine four lines: line4 + line3 + line2 + line1 (靠上的行放在右边)
            combined_line = valid_lines[i+3] + valid_lines[i+2] + valid_lines[i+1] + valid_lines[i]
            combined.append(combined_line)

    # Write to the output file
    with open(output_filename, 'w') as f:
        f.write('\n'.join(combined))
    
    print(f"Conversion completed! Processed {len(valid_lines)} rows, generated {len(combined)} lines of 512 bits")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mif_dir = os.path.join(script_dir, "mif")
    asm_dir = os.path.join(script_dir, "asm")

    names = [
        {"input":"ROM",
         "output":"AROM",
        },
        {"input":"GM1",
         "output":"AGM1",
        } 
    ]

    for name in names:
        input_n = name["input"]
        output_n = name["output"]
        asm_file = os.path.join(asm_dir, f"{input_n}.asm")
        mif_file = os.path.join(mif_dir, f"{output_n}.mif")

        if not os.path.exists(asm_file):
            print(f"[Error] Cannot find: {asm_file}")
            continue  

        with open(asm_file, 'r') as f:
            all_lines = []
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                all_lines.append(line)

        groups = []
        ins = 4
        for i in range(0, len(all_lines), ins):
            chunk = all_lines[i:i+ins]
            if len(chunk) < ins:
                chunk += [""] * (ins - len(chunk))
            groups.append(chunk)

        # write MIF 
        with open(mif_file, 'w') as f_mif:
            for chunk_index, chunk in enumerate(groups):
                instr_mif_list = []
                for line in chunk:
                    machine_int = parse_one_instruction(line)  
                    machine_bin = format(machine_int, '032b')   
                    instr_mif_list.append(machine_bin)
                
                all_128_bits = "".join(instr_mif_list)
                f_mif.write(all_128_bits + "\n")

        print(f"Successfully Generated :{mif_file}")

    script_dir = os.path.dirname(os.path.abspath(__file__))

    NS = [
        {"input":"AROM",
         "output":"ROM",
        },
        {"input":"AGM1",
         "output":"GM1",
        } 
    ]
    for n in NS:
        input_file = n["input"]  
        output_file = n["output"]

        mif_dir = os.path.join(script_dir,"mif")

        input_filename = os.path.join(mif_dir, f"{input_file}.mif")
        output_filename = os.path.join(mif_dir, f"{output_file}.mif")
    
        process_mif(input_filename, output_filename)

if __name__ == "__main__":
    main()
