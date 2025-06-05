import os
import sys

NUM_REGS = 32
memory = {}
regs_normal = [0] * NUM_REGS
regs_lp = [0] * NUM_REGS
PC = 0

def sign_extend(value, bit_width):
    sign_bit = 1 << (bit_width - 1)
    return (value ^ sign_bit) - sign_bit

def decode_instruction(instr_32_bits):

    instr_val = int(instr_32_bits, 2)
    opcode = instr_val & 0x7F
    rd = (instr_val >> 7) & 0x1F
    funct3 = (instr_val >> 12) & 0x7
    rs1 = (instr_val >> 15) & 0x1F
    rs2 = (instr_val >> 20) & 0x1F
    funct7 = (instr_val >> 25) & 0x7F

    if opcode == 0b0010011:  
        imm = sign_extend((instr_val >> 20) & 0xFFF, 12)
        if funct3 == 0b000:    # ADDI
            return {'type': 'addi', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b100:  # XORI
            return {'type': 'xori', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b110:  # ORI
            return {'type': 'ori', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b111:  # ANDI
            return {'type': 'andi', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b001:  # SLLI
            if funct7 == 0b0000000:
                return {'type': 'slli', 'rd': rd, 'rs1': rs1, 'shamt': (instr_val >> 20) & 0x1F}
        elif funct3 == 0b101:  # SRLI/SRAI
            shamt = (instr_val >> 20) & 0x1F
            if funct7 == 0b0000000:
                return {'type': 'srli', 'rd': rd, 'rs1': rs1, 'shamt': shamt}
            elif funct7 == 0b0100000:
                return {'type': 'srai', 'rd': rd, 'rs1': rs1, 'shamt': shamt}
        elif funct3 == 0b010:  # SLTI
            return {'type': 'slti', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b011:  # SLTIU
            return {'type': 'sltiu', 'rd': rd, 'rs1': rs1, 'imm': imm}
        return {'type': 'unknown_i'}

    elif opcode == 0b0110011:  # R-type 
        if funct3 == 0b000:
            if funct7 == 0b0000000:   # ADD
                return {'type': 'add', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
            elif funct7 == 0b0100000:  # SUB
                return {'type': 'sub', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
        elif funct3 == 0b111:  # and
            return {'type': 'and', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
        elif funct3 == 0b100:  # XOR
            return {'type': 'xor', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
        elif funct3 == 0b110:  # OR
            return {'type': 'or', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
        elif funct3 == 0b001:  # SLL
            return {'type': 'sll', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
        elif funct3 == 0b101:   # SRL/SRA
            if funct7 == 0b0000000:   # SRL
                return {'type': 'srl', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
            elif funct7 == 0b0100000:  # SRA
                return {'type': 'sra', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
        elif funct3 == 0b010:  # SLT
            return {'type': 'slt', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
        elif funct3 == 0b011:  # SLTU
            return {'type': 'sltu', 'rd': rd, 'rs1': rs1, 'rs2': rs2}
        return {'type': 'unknown_r'}

    elif opcode == 0b0000011:  # Load 
        imm = sign_extend((instr_val >> 20) & 0xFFF, 12)
        if funct3 == 0b000:    # LB
            return {'type': 'lb', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b001:  # LH
            return {'type': 'lh', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b010:   # LW
            return {'type': 'lw', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b100:  # LBU
            return {'type': 'lbu', 'rd': rd, 'rs1': rs1, 'imm': imm}
        elif funct3 == 0b101:  # LHU
            return {'type': 'lhu', 'rd': rd, 'rs1': rs1, 'imm': imm}
        return {'type': 'unknown_load'}

    elif opcode == 0b0100011:  # Store 
        imm = sign_extend(((instr_val >> 25) & 0x7F) << 5 | ((instr_val >> 7) & 0x1F), 12)
        if funct3 == 0b000:    # SB
            return {'type': 'sb', 'rs1': rs1, 'rs2': rs2, 'imm': imm}
        elif funct3 == 0b001:  # SH
            return {'type': 'sh', 'rs1': rs1, 'rs2': rs2, 'imm': imm}
        elif funct3 == 0b010:  # SW
            return {'type': 'sw', 'rs1': rs1, 'rs2': rs2, 'imm': imm}
        return {'type': 'unknown_store'}

    elif opcode == 0b0110111:  # LUI
        imm = ((instr_val >> 12) & 0xFFFFF) << 12
        return {'type': 'lui', 'rd': rd, 'imm': imm}

    elif opcode == 0b0010111:  # AUIPC
        imm = (instr_val & 0xFFFFF000)
        return {'type': 'auipc', 'rd': rd, 'imm': imm}
    
    # ...其他解码逻辑
    elif opcode == 0b0001011:  # lp.setup
        imm = (instr_val & 0xFFFFF000)
        return {'type': 'lp.setup', 'rd': rd, 'imm': imm}
    elif opcode == 0b0101011:  # lp.goto
        imm = (instr_val & 0xFFFFF000)
        return {'type': 'lp.goto', 'rd': rd, 'imm': imm}
    # ...
    else:
        return {'type': 'unknown'}

def execute_instructions(instructions):
    global regs_normal, regs_lp, memory, PC

    exec_log = []
    old_regs_normal = regs_normal.copy()
    old_regs_lp = regs_lp.copy()
    old_mem = dict(memory)

    new_regs_normal = old_regs_normal.copy()
    new_regs_lp = old_regs_lp.copy()
    new_mem = dict(old_mem)

    reg_writes_normal = []
    reg_writes_lp = []
    mem_writes = []

    for i, instr in enumerate(instructions):
        t = instr['type']
        result = None

        # 确定使用的寄存器组
        if t == 'lp.setup':
            current_old_regs = old_regs_lp
            reg_writes = reg_writes_lp
        else:
            current_old_regs = old_regs_normal
            reg_writes = reg_writes_normal

        rd = instr.get('rd', 0)
        rs1 = instr.get('rs1', 0)
        rs2 = instr.get('rs2', 0)
        imm = instr.get('imm', 0)
        shamt = instr.get('shamt', 0)

        # 指令执行逻辑（使用current_old_regs读取源寄存器）
        if t == 'addi':
            # ...示例指令处理...
            if rd != 0:
                result = current_old_regs[rs1] + imm
                reg_writes.append((rd, result))
            exec_log.append(f"Instr {i}: addi x{rd}, x{rs1}, {imm:08X} -> x{rd} = {current_old_regs[rs1]:08X} + {imm:08X}")

        # ...其他指令处理...

        # 处理lp.setup的输出
        if t == 'lp.setup':
            log_msg = []
            log_msg.append(f"===== lp.setup encountered at PC {PC} =====")
            log_msg.append("Normal Registers:")
            for idx in range(NUM_REGS):
                log_msg.append(f"x{idx} = 0x{old_regs_normal[idx]:08X}")
            log_msg.append("LP Registers:")
            for idx in range(NUM_REGS):
                log_msg.append(f"x{idx} = 0x{old_regs_lp[idx]:08X}")
            log_msg.append("Memory (non-zero):")
            for addr in sorted(old_mem):
                log_msg.append(f"mem[{addr:08X}] = 0x{old_mem[addr]:08X}")
            exec_log.extend(log_msg)

    # 应用写入操作
    for r, val in reg_writes_normal:
        new_regs_normal[r] = val & 0xFFFFFFFF
    for r, val in reg_writes_lp:
        new_regs_lp[r] = val & 0xFFFFFFFF
    for addr, val in mem_writes:
        new_mem[addr] = val & 0xFFFFFFFF

    # 更新全局状态
    regs_normal = new_regs_normal
    regs_lp = new_regs_lp
    memory = new_mem

    # 打印执行日志
    print("====== Cycle Execution ======")
    for line in exec_log:
        print(line)

def main():
    global PC

    script_dir = os.path.dirname(os.path.abspath(__file__))
    name = 'ROM'
    mif_dir = os.path.join(script_dir, "mif")
    filename = os.path.join(mif_dir, f"{name}.mif")

    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        line_len = len(line)
        if line_len not in (128, 256):
            print(f"Invalid line length {line_len}")
            continue

        # 处理 256 位行
        blocks = []
        if line_len == 128:
            blocks.append(line)
        else:
            # 分割为两个 128 位块：右侧（低位）优先
            blocks.append(line[128:256])  # 右侧 128 位
            blocks.append(line[0:128])    # 左侧 128 位

        for block in blocks:
            instr_bin_list = []
            # 按槽解析（槽 0 在最右侧）
            for slot in reversed(range(4)):  # 3,2,1,0
                start = slot * 32
                end = start + 32
                chunk_32 = block[start:end]
                # 验证位宽
                if len(chunk_32) != 32:
                    print(f"Invalid 32-bit chunk: {chunk_32}")
                    continue
                # 调整字节序
                byte0 = chunk_32[24:32]  # 最低有效字节
                byte1 = chunk_32[16:24]
                byte2 = chunk_32[8:16]
                byte3 = chunk_32[0:8]     # 最高有效字节
                real_32 = byte3 + byte2 + byte1 + byte0
                Real_32 = byte0 + byte1 + byte2 + byte3
                instr_bin_list.append(real_32)

            # 解码并执行
            instructions = []
            for bits in instr_bin_list:
                decoded = decode_instruction(bits)
                if decoded['type'] != 'invalid':
                    instructions.append(decoded)
                else:
                    print(f"Failed to decode: {bits}")

            execute_instructions(instructions)
            PC += 16

    # 最终状态输出
    print("===== Final Normal Registers =====")
    for i, val in enumerate(regs_normal):
        print(f"x{i} = 0x{val & 0xFFFFFFFF:08X}")

    print("\n===== Final LP Registers =====")
    for i, val in enumerate(regs_lp):
        print(f"x{i} = 0x{val & 0xFFFFFFFF:08X}")

    print("\n===== Final Memory (non-zero) =====")
    for addr, val in sorted(memory.items()):
        print(f"mem[{addr:08X}] = 0x{val & 0xFFFFFFFF:08X}")

if __name__ == "__main__":
    main()