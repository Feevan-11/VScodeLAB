import re
import os
from collections import defaultdict

def read_reg_values(file_path):
    """读取分段的寄存器配置文件，返回字典{段编号: {寄存器: 值}}"""
    segment_regs = defaultdict(dict)
    current_segment = 0  # 默认从第0段开始
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # 检测段分隔符，例如：; --- SEGMENT 1
            seg_match = re.match(r'; --- SEGMENT\s+(\d+)', line, re.I)
            if seg_match:
                current_segment = int(seg_match.group(1))
                continue
            
            # 解析寄存器赋值
            reg, value = line.split()
            segment_regs[current_segment][reg.lower()] = int(value, 0)
    
    return segment_regs

def split_into_segments(asm_code):
    """智能分割代码段，自动检测段分隔符"""
    segments = []
    current_segment = []
    segment_id = 0
    
    for line in asm_code.split('\n'):
        # 检测段分隔符，例如：; --- SEGMENT 1
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
    def calculate_values(value):
        """带符号位处理的32位值分解"""
        addi_imm = value & 0xFFF
        if addi_imm >= 0x800:
            addi_imm -= 0x1000
        lui_imm = (value - addi_imm) >> 12
        return lui_imm & 0xFFFFF, addi_imm & 0xFFF

    lines = []
    pending_lui = {}  # 跟踪需要匹配addi的lui指令
    
    for line in segment.split('\n'):
        # 处理lui指令
        lui_match = re.match(r'^\s*(lui)\s+([xX]\d+)\s*,\s*(0x[\da-fA-F]+|\d+)', line)
        if lui_match:
            reg = lui_match.group(2).lower()
            if reg in seg_reg_values:
                lui_imm, _ = calculate_values(seg_reg_values[reg])
                new_line = f"{lui_match.group(1)} {reg}, 0x{lui_imm:X}"
                pending_lui[reg] = line  # 保存原始行用于后续处理
                lines.append(new_line)
                continue
        
        # 处理addi指令
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
    """生成最终输出文件，确保代码段与寄存器配置段完全匹配"""
    # 获取配置中的所有段编号
    config_segment_ids = set(reg_config.keys())
    
    # 验证段数量一致性
    if len(processed_segments) != len(config_segment_ids):
        raise ValueError(
            f"代码段数({len(processed_segments)})与寄存器配置段数({len(config_segment_ids)})不匹配"
        )
    
    # 构建段内容映射字典
    segment_map = {seg_id: content for content, seg_id in processed_segments}
    
    # 生成带段标记的最终汇编
    with open(output_file, 'w') as f:
        # 按寄存器配置的原始顺序写入（假设配置有顺序）
        for seg_id in sorted(reg_config.keys()):
            if seg_id not in segment_map:
                raise ValueError(f"寄存器配置段{seg_id}在代码中不存在对应段")
            
            #f.write(f"; --- SEGMENT {seg_id}\n")
            f.write(segment_map[seg_id])
            f.write("\n")

def main():
    # 初始化路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 文件配置
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

    for cfg in configs:
        # 读取寄存器配置
        reg_values = read_reg_values(cfg["reg_config"])
        
        # 读取汇编代码
        with open(cfg["asm_in"], 'r') as f:
            original_asm = f.read()
        
        # 分割代码段（返回结构：[(代码内容, 段ID), ...]）
        raw_segments = split_into_segments(original_asm)
        
        # 处理每个代码段（正确解包元组）
        processed_segments = []
        for seg_content, seg_id in raw_segments:  # 正确解包元组
            # 获取当前段的寄存器配置
            seg_reg_values = reg_values.get(seg_id, {})
            
            # 处理代码内容（seg_content是字符串）
            processed = process_segment(seg_content, seg_reg_values)
            processed_segments.append((processed, seg_id))
        
        # 生成输出文件
        try:
            generate_output(
                processed_segments=processed_segments,
                reg_config=reg_values,
                output_file=cfg["asm_out"]
            )
            print(f"成功生成：{cfg['asm_out']}")
        except ValueError as e:
            print(f"生成失败：{str(e)}")

if __name__ == "__main__":
    main()