import re
import os
from collections import defaultdict

def read_reg_values(file_path):
    """读取段的寄存器配置文件，返回字典 {段号: {寄存器: 值}}"""
    segment_regs = defaultdict(dict)
    current_segment = 0  # 默认段号为0，如果没有段注释
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue  # 跳过空行和注释
            
            # 解析段注释，例如：; --- SEGMENT 1
            seg_match = re.match(r'; --- SEGMENT\s+(\d+)', line, re.I)
            if seg_match:
                current_segment = int(seg_match.group(1))
                continue
            
            # 解析寄存器赋值，例如：x1 0x2000
            if ' ' in line:
                reg, value = line.split()
                segment_regs[current_segment][reg.lower()] = int(value, 0)
    
    return segment_regs

def split_into_segments(asm_code):
    """将汇编代码按段分割，自动检测段分隔符"""
    segments = []
    current_segment = []
    segment_id = 0  # 默认段号
    
    for line in asm_code.split('\n'):
        # 检测段注释，例如：; --- SEGMENT 1
        seg_match = re.match(r'^\s*;\s+--- SEGMENT\s+(\d+)', line, re.I)
        if seg_match:
            if current_segment:
                segments.append(('\n'.join(current_segment), segment_id))
                current_segment = []
            segment_id = int(seg_match.group(1))
            continue
        
        current_segment.append(line)
    
    if current_segment:
        segments.append(('\n'.join(current_segment), segment_id))
    
    return segments

def process_segment(segment, seg_reg_values):
    """处理单个代码段，使用对应段的寄存器配置"""
    lines = []
    
    for line in segment.split('\n'):
        # 匹配 lp.setup 指令，例如：lp.setup x1, 0x1000
        setup_match = re.match(r'^\s*(lp\.setup)\s+([xX]\d+)\s*,\s*(0x[\da-fA-F]+|\d+)', line)
        if setup_match:
            reg = setup_match.group(2).lower()
            if reg in seg_reg_values:
                # 直接替换立即数为寄存器配置中的值
                reg_value = seg_reg_values[reg]
                new_line = f"{setup_match.group(1)} {reg}, 0x{reg_value:X}"
                lines.append(new_line)
                continue  # 跳过原行
        
        # 未匹配或无需替换时保留原行
        lines.append(line)
    
    return '\n'.join(lines)

def generate_output(processed_segments, reg_config, output_file='output.asm'):
    """生成最终输出文件，确保代码段与寄存器配置严格匹配"""
    config_segment_ids = set(reg_config.keys())

    if len(processed_segments) != len(config_segment_ids):
        raise ValueError(
            f"Number of code segments({len(processed_segments)})with the number of segments of register configuration({len(config_segment_ids)})Mismatch"
        )
    
    segment_map = {seg_id: content for content, seg_id in processed_segments}
    
    with open(output_file, 'w') as f:
        for seg_id in sorted(reg_config.keys()):
            if seg_id not in segment_map:
                raise ValueError(f"段 {seg_id} 在代码中无对应内容")
            f.write(segment_map[seg_id])
            f.write("\n")

def main():
    """主函数：处理所有配置"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    configs = [
        {
            "asm_in": os.path.join("asm", "ROM.asm"),
            "reg_config": os.path.join("txt", "ROMLOOP.txt"),
            "asm_out": os.path.join("asm", "ROM.asm")
        },
        {
            "asm_in": os.path.join("asm", "GM1.asm"),
            "reg_config": os.path.join("txt", "GM1LOOP.txt"),
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
            seg_reg_values = reg_values.get(seg_id, {})
            processed = process_segment(seg_content, seg_reg_values)
            processed_segments.append((processed, seg_id))
        
        try:
            generate_output(
                processed_segments=processed_segments,
                reg_config=reg_values,
                output_file=cfg["asm_out"]
            )
            print(f"成功生成：{cfg['asm_out']}")
        except ValueError as e:
            print(f"错误：{str(e)}")

if __name__ == "__main__":
    main()