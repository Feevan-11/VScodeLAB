import re
import os
from collections import defaultdict

def read_reg_values(file_path):
    """Read the register configuration file of the segment and return the dictionary {segment number: {register: value}}"""
    segment_regs = defaultdict(dict)
    current_segment = 0  
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # ; --- SEGMENT 1
            seg_match = re.match(r'; --- SEGMENT\s+(\d+)', line, re.I)
            if seg_match:
                current_segment = int(seg_match.group(1))
                continue

            if ' ' in line:
                reg, value = line.split()
                segment_regs[current_segment][reg.lower()] = int(value, 0)

    
    return segment_regs

def split_into_segments(asm_code):
    """Intelligently segment code snippets and automatically detect segment separators"""
    segments = []
    current_segment = []
    segment_id = 0
    
    for line in asm_code.split('\n'):
        # ; --- SEGMENT 
        seg_match = re.match(r'^\s*;\s+--- SEGMENT\s+(\d+)', line, re.I)
        if seg_match:
            if current_segment:
                segments.append(('\n'.join(current_segment), segment_id))
                current_segment = []
            segment_id = int(seg_match.group(1))
            current_segment.append(line)
            continue
        
        current_segment.append(line)
    
    if current_segment:
        segments.append(('\n'.join(current_segment), segment_id))
    
    return segments

def process_segment(segment, seg_reg_values):
    """Processes a single code segment, using the register configuration of the corresponding segment"""
    def calculate_values(value):
        """32-bit value decomposition with signed bit handling"""
        addi_imm = value & 0xFFF
        if addi_imm >= 0x800:
            addi_imm -= 0x1000
        lui_imm = (value - addi_imm) >> 12
        return lui_imm & 0xFFFFF, addi_imm & 0xFFF

    lines = []
    pending_lui = {}  
    
    for line in segment.split('\n'):
        # lui
        lui_match = re.match(r'^\s*(lui)\s+([xX]\d+)\s*,\s*(0x[\da-fA-F]+|\d+)', line)
        if lui_match:
            reg = lui_match.group(2).lower()
            if reg in seg_reg_values:
                lui_imm, _ = calculate_values(seg_reg_values[reg])
                new_line = f"{lui_match.group(1)} {reg}, 0x{lui_imm:X}"
                pending_lui[reg] = line 
                lines.append(new_line)
                continue
        
        # addi
        addi_match = re.match(r'^\s*(addi)\s+([xX]\d+)\s*,\s*([xX]\d+)\s*,\s*(0x[\da-fA-F]+|\d+)', line)
        if addi_match and addi_match.group(2) == addi_match.group(3):
            reg = addi_match.group(2).lower()
            if reg in seg_reg_values and reg in pending_lui:
                _, addi_imm = calculate_values(seg_reg_values[reg])
                new_line = f"{addi_match.group(1)} {reg}, {reg}, 0x{addi_imm:X}"
                lines.append(new_line)
                del pending_lui[reg]
                continue
        
        lines.append(line)
    
    return '\n'.join(lines)

def generate_output(processed_segments, reg_config, output_file='output.asm'):
    """Generate the final output file, making sure that the code snippet exactly matches the register configuration snig"""
    config_segment_ids = set(reg_config.keys())
    
    if len(processed_segments) != len(config_segment_ids):
        raise ValueError(
            f"Number of code segments({len(processed_segments)})with the number of segments of register configuration({len(config_segment_ids)})Mismatch"
        )
    

    segment_map = {seg_id: content for content, seg_id in processed_segments}
    

    with open(output_file, 'w') as f:

        for seg_id in sorted(reg_config.keys()):
            if seg_id not in segment_map:
                raise ValueError(f"{seg_id}There is no corresponding segment in the code")
            
            #f.write(f"; --- SEGMENT {seg_id}\n")
            f.write(segment_map[seg_id])
            f.write("\n")

def main(GM1 = 2):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    if (GM1 == 3):
        configs = [
        {
            "asm_in": os.path.join("asm", "ROMCODE.asm"),
            "reg_config": os.path.join("txt", "ROM.txt"),
            "asm_out": os.path.join("asm", "ROM.asm")
        },
        {
            "asm_in": os.path.join("asm", "GM1NI.asm"),
            "reg_config": os.path.join("txt", "GM1.txt"),
            "asm_out": os.path.join("asm", "GM1.asm")
        }
     ]
    elif(GM1 == 2):
        configs = [
        {
            "asm_in": os.path.join("asm", "ROMCODE.asm"),
            "reg_config": os.path.join("txt", "ROM.txt"),
            "asm_out": os.path.join("asm", "ROM.asm")
        },
        {
            "asm_in": os.path.join("asm", "GM1CODE.asm"),
            "reg_config": os.path.join("txt", "GM1.txt"),
            "asm_out": os.path.join("asm", "GM1.asm")
        }
        ]
    else:
        configs = [
        {
            "asm_in": os.path.join("asm", "TROMCODE.asm"),
            "reg_config": os.path.join("txt", "ROM.txt"),
            "asm_out": os.path.join("asm", "ROM.asm")
        },
        {
            "asm_in": os.path.join("asm", "TGM1CODE.asm"),
            "reg_config": os.path.join("txt", "GM1.txt"),
            "asm_out": os.path.join("asm", "GM1.asm")
        }
     ]

    for cfg in configs:
        reg_values = read_reg_values(cfg["reg_config"])
        
        with open(cfg["asm_in"], 'r') as f:
            original_asm = f.read()
        
        raw_segments = split_into_segments(original_asm)
        
        processed_segments = []
        for seg_content, seg_id in raw_segments:  
            # Gets the register configuration for the current segment
            seg_reg_values = reg_values.get(seg_id, {})
            
            # Handling code content (seg_content is a string)
            processed = process_segment(seg_content, seg_reg_values)
            processed_segments.append((processed, seg_id))
        
        # Generate an output file
        try:
            generate_output(
                processed_segments=processed_segments,
                reg_config=reg_values,
                output_file=cfg["asm_out"]
            )
            print(f"Successfully generated：{cfg['asm_out']}")
        except ValueError as e:
            print(f"erro：{str(e)}")

if __name__ == "__main__":
    main()