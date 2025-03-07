import os
import sys

NUM_REGS = 32
memory = {}
regs = [0] * NUM_REGS
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
    
    elif opcode == 0b0001011:  # lp.setup
        imm = (instr_val & 0xFFFFF000)
        return {'type': 'lp.setup', 'rd': rd, 'imm': imm}
    
    elif opcode == 0b0101011:  # lp.goto
        imm = (instr_val & 0xFFFFF000)
        return {'type': 'lp.goto', 'rd': rd, 'imm': imm}


    else:
        return {'type': 'unknown'}
    
   

def execute_instructions(instructions):
    global regs, memory, PC

    exec_log = []
    old_regs = regs[:]
    old_mem = dict(memory)

    new_regs = regs[:]
    new_mem = dict(memory)

    reg_writes = []
    mem_writes = []

    for i, instr in enumerate(instructions):
        t = instr['type']
        result = None  

        rd = instr.get('rd', 0)
        rs1 = instr.get('rs1', 0)
        rs2 = instr.get('rs2', 0)
        imm = instr.get('imm', 0)
        shamt = instr.get('shamt', 0)

        if t == 'addi':
            if rd != 0:
                result = old_regs[rs1] + imm
                reg_writes.append((rd, result))
            exec_log.append(
                f"Instr {i}: addi x{rd}, x{rs1}, {imm:08X} -> x{rd} = {old_regs[rs1]:08X} + {imm:08X}"
            )

        elif t == 'lui':
            if rd != 0:
                reg_writes.append((rd, imm))
            exec_log.append(
                f"Instr {i}: lui x{rd}, 0x{imm:08X} -> x{rd} = 0x{imm:08X}"
            )

        elif t == 'sw':
            addr = old_regs[rs1] + imm
            data = old_regs[rs2]
            if addr < 0:
                exec_log.append("addr erro:")
            else:  
                mem_writes.append((addr, data))
            exec_log.append(
                f"Instr {i}: sw x{rs2}, {imm:08X}(x{rs1}) -> mem[{addr:08X}] = {data:08X}"
            )

        elif t == 'and':
            if rd != 0:
                result = old_regs[rs1] & old_regs[rs2]
                reg_writes.append((rd, result))
            exec_log.append(
                f"Instr {i}: and x{rd}, x{rs1}, x{rs2} -> x{rd} = {old_regs[rs1]:08X} & {old_regs[rs2]:08X}"
            )

        elif t == 'lp.setup':
            if rd != 0:
                reg_writes.append((rd, imm))
            exec_log.append(
                f"Instr {i}: lp.setup x{rd}, {imm:08X} -> x{rd} = {imm:08X}"
            )

        elif t == 'lp.goto':
            new_PC = PC + imm
            exec_log.append(
                f"Instr {i}: lp.goto x{rd}, {imm:08X} ->  PC = {PC} + {imm:08X} = {new_PC}"
            )
            PC = new_PC

        elif t == 'add':
            result = old_regs[rs1] + old_regs[rs2]
            exec_log.append(
                f"Instr {i}: add x{rd}, x{rs1}, x{rs2} -> x{rd} = {old_regs[rs1]:08X} + {old_regs[rs2]:08X}"
            )
        elif t == 'sub':
            result = old_regs[rs1] - old_regs[rs2]
            exec_log.append(
                f"Instr {i}: sub x{rd}, x{rs1}, x{rs2} -> x{rd} = {old_regs[rs1]:08X} - {old_regs[rs2]:08X}"
            )
        elif t == 'xor':

            result = old_regs[rs1] ^ old_regs[rs2]
            exec_log.append(
                f"Instr {i}: xor x{rd}, x{rs1}, x{rs2} -> x{rd} = {old_regs[rs1]:08X} ^ {old_regs[rs2]:08X}"
            )
        elif t == 'or':

            result = old_regs[rs1] | old_regs[rs2]
            exec_log.append(
                f"Instr {i}: or x{rd}, x{rs1}, x{rs2} -> x{rd} = {old_regs[rs1]:08X} | {old_regs[rs2]:08X}"
            )
        elif t == 'sll':

            shamt = old_regs[rs2] & 0x1F
            result = old_regs[rs1] << shamt
            exec_log.append(
                f"Instr {i}: sll x{rd}, x{rs1}, x{rs2} -> x{rd} = {old_regs[rs1]:08X} << {shamt}"
            )
        elif t == 'srl':

            shamt = old_regs[rs2] & 0x1F
            result = (old_regs[rs1] & 0xFFFFFFFF) >> shamt
            exec_log.append(
                f"Instr {i}: srl x{rd}, x{rs1}, x{rs2} -> x{rd} = {old_regs[rs1]:08X} >> {shamt} (logical)"
            )
        elif t == 'sra':

            shamt = old_regs[rs2] & 0x1F
            result = (sign_extend(old_regs[rs1], 32) >> shamt) & 0xFFFFFFFF
            exec_log.append(
                f"Instr {i}: sra x{rd}, x{rs1}, x{rs2} -> x{rd} = {sign_extend(old_regs[rs1],32):08X} >> {shamt} (arithmetic)"
            )
        elif t == 'slt':

            result = 1 if sign_extend(old_regs[rs1], 32) < sign_extend(old_regs[rs2], 32) else 0
            exec_log.append(
                f"Instr {i}: slt x{rd}, x{rs1}, x{rs2} -> x{rd} = ({sign_extend(old_regs[rs1],32):08X} < {sign_extend(old_regs[rs2],32):08X}) ? 1 : 0"
            )
        elif t == 'sltu':

            result = 1 if (old_regs[rs1] & 0xFFFFFFFF) < (old_regs[rs2] & 0xFFFFFFFF) else 0
            exec_log.append(
                f"Instr {i}: sltu x{rd}, x{rs1}, x{rs2} -> x{rd} = ({old_regs[rs1]:08X} < {old_regs[rs2]:08X}) ? 1 : 0 (unsigned)"
            )


        elif t == 'xori':

            result = old_regs[rs1] ^ imm
            exec_log.append(
                f"Instr {i}: xori x{rd}, x{rs1}, {imm:08X} -> x{rd} = {old_regs[rs1]:08X} ^ {imm:08X}"
            )
        elif t == 'ori':

            result = old_regs[rs1] | imm
            exec_log.append(
                f"Instr {i}: ori x{rd}, x{rs1}, {imm:08X} -> x{rd} = {old_regs[rs1]:08X} | {imm:08X}"
            )
        elif t == 'andi':

            result = old_regs[rs1] & imm
            exec_log.append(
                 f"Instr {i}: andi x{rd}, x{rs1}, {imm:08X} -> x{rd} = {old_regs[rs1]:08X} & {imm:08X}"
            )
        elif t == 'slli':

            result = old_regs[rs1] << imm
            exec_log.append(
                 f"Instr {i}: slli x{rd}, x{rs1}, {shamt} -> x{rd} = {old_regs[rs1]:08X} << {shamt}"
            )
        elif t == 'srli':

            result = (old_regs[rs1] & 0xFFFFFFFF) >> imm
            exec_log.append(
                 f"Instr {i}: srli x{rd}, x{rs1}, {shamt} -> x{rd} = {old_regs[rs1]:08X} >> {shamt} (logical)"
            )
        elif t == 'srai':

            result = (sign_extend(old_regs[rs1], 32) >> imm) & 0xFFFFFFFF
            exec_log.append(
                 f"Instr {i}: srai x{rd}, x{rs1}, {shamt} -> x{rd} = {sign_extend(old_regs[rs1],32):08X} >> {shamt} (arithmetic)"
            )
        elif t == 'slti':

            result = 1 if sign_extend(old_regs[rs1], 32) < imm else 0
            exec_log.append(
                 f"Instr {i}: slti x{rd}, x{rs1}, {imm:08X} -> x{rd} = 1 if {sign_extend(old_regs[rs1],32):08X} < {imm:08X} else 0"
            )

        elif t == 'sltiu':

            result = 1 if (old_regs[rs1] & 0xFFFFFFFF) < (imm & 0xFFFFFFFF) else 0
            exec_log.append(
                 f"Instr {i}: sltiu x{rd}, x{rs1}, {imm:08X} -> x{rd} = 1 if {old_regs[rs1]:08X} < {imm & 0xFFFFFFFF:08X} (unsigned) else 0"
            )


        elif t in ['lb', 'lh', 'lw', 'lbu', 'lhu']:
            addr = old_regs[rs1] + imm
            mem_val = memory.get(addr, 0)
            if t == 'lb':
                result = sign_extend(mem_val & 0xFF, 8)
                exec_log.append(
                    f"Instr {i}: lb x{rd}, {imm:08X}(x{rs1}) -> mem[{addr:08X}] (half) sign-extended"
                )
            elif t == 'lh':
                result = sign_extend(mem_val & 0xFFFF, 16)
                exec_log.append(
                    f"Instr {i}: lh x{rd}, {imm:08X}(x{rs1}) -> mem[{addr:08X}] (half) sign-extended"
                )
            elif t == 'lw':
                result = mem_val & 0xFFFFFFFF
                exec_log.append(
                    f"Instr {i}: lw x{rd}, {imm:08X}(x{rs1}) -> mem[{addr:08X}] (half) sign-extended"
                )
            elif t == 'lbu':
                result = mem_val & 0xFF
                exec_log.append(
                    f"Instr {i}: lbu x{rd}, {imm:08X}(x{rs1}) -> mem[{addr:08X}] (half) sign-extended"
                )
            elif t == 'lhu':
                result = mem_val & 0xFFFF
                exec_log.append(
                    f"Instr {i}: lhu x{rd}, {imm:08X}(x{rs1}) -> mem[{addr:08X}] (half) sign-extended"
                )
        

        elif t in ['sb', 'sh']:
            addr = old_regs[rs1] + imm
            data = old_regs[rs2]
            if t == 'sb':
                if addr < 0:
                    exec_log.append("addr erro:")
                else:    
                    mem_writes.append((addr, data & 0xFF))
                exec_log.append(
                    f"Instr {i}: sb x{rs2}, {imm:08X}(x{rs1}) -> mem[{addr:08X}] = {old_regs[rs2] & 0xFF:02X} (byte)"
                )
            elif t == 'sh':
                if addr < 0:
                    exec_log.append("addr erro:")
                else:  
                    mem_writes.append((addr, data & 0xFFFF))
                exec_log.append(
                    f"Instr {i}: sh x{rs2}, {imm:08X}(x{rs1}) -> mem[{addr:08X}] = {old_regs[rs2] & 0xFFFF:04X} (half)"
                )
        

        elif t == 'auipc':
            result = (PC & 0xFFFFF000) + imm  
            pc_upper = (PC & 0xFFFFF000)
            exec_log.append(
                f"Instr {i}: auipc x{rd}, 0x{(imm >> 12):05X} -> x{rd} = 0x{pc_upper:05X}000 + 0x{(imm >> 12):05X}000"
            )    

        else:
            exec_log.append(f"Instr {i}: unknown or unimplemented opcode.")


        if result is not None and rd != 0:
            reg_writes.append((instr['rd'], result & 0xFFFFFFFF))        


    print("====== Cycle Execution ======")
    for line in exec_log:
        print(line)

    #print("----- Write Back -----")
    for (r, val) in reg_writes:
        new_regs[r] = val & 0xFFFFFFFF
        #print(f"  x{r} <- 0x{val & 0xFFFFFFFF:08X}")

    for (addr, val) in mem_writes:
        new_mem[addr] = val & 0xFFFFFFFF
        #print(f"  mem[{addr}] <- 0x{val & 0xFFFFFFFF:08X}")

    regs = new_regs
    memory = new_mem


def main():
    global PC

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    name = 'TROM'

    mif_dir = os.path.join(script_dir,"mif")
    filename = os.path.join(mif_dir, f"{name}.mif")

    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if len(line) != 128:
            print(f"warming：Line length is not 128，The number of bits is incorrect.Line content：{line}")
            continue


        instr_bin_list = []
        for i in range(4):
            # i*32 to i*32+32
            chunk_32 = line[i*32 : (i+1)*32]  #  32 bits

            b0 = chunk_32[0 : 8]   
            b1 = chunk_32[8 :16]
            b2 = chunk_32[16:24]
            b3 = chunk_32[24:32]  
            

            real_32 = b3 + b2 + b1 + b0
            REAL_32 = b0 + b1 + b2 + b3

            instr_bin_list.append(REAL_32)

        instructions = [decode_instruction(bits) for bits in instr_bin_list]

        execute_instructions(instructions)
        PC += 16

    print("===== Final Registers =====")
    for i, val in enumerate(regs):
        print(f"x{i} = 0x{val & 0xFFFFFFFF:08X}")

    print("\n===== Final Memory (non-zero) =====")
    for addr, val in sorted(memory.items()):
        print(f"mem[{addr:08X}] = 0x{val & 0xFFFFFFFF:08X}")

if __name__ == "__main__":
    main()
