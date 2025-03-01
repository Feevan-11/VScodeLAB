import os
from tabulate import tabulate

def process_asm_file(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f:
            # 清理注释和空行
            line = line.split('#')[0].split(';')[0].strip()
            if line and not line.endswith(':'):
                if ':' in line:
                    line = line.split(':', 1)[1].strip()
                instructions.append(line)
    
    # 生成Markdown表格数据
    table_data = []
    address = 0
    for i in range(0, len(instructions), 4):
        group = instructions[i:i+4]
        while len(group) < 4:
            group.append('')
        table_data.append([
            f"`0x{address:04X}`",  # 地址用代码块包裹
            *[f"`{instr}`" if instr else "" for instr in group]  # 指令用代码块包裹
        ])
        address += 16
    
    return table_data

def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    name = 'DMN'
    md_dir = os.path.join(script_dir,"md")
    asm_dir = os.path.join(script_dir,"asm")

    filename = os.path.join(asm_dir, f"{name}.asm")

    if not filename:
        print("未找到.asm文件")
        return

    print(f"处理文件: {filename}")
    
    # 生成Markdown内容
    headers = ["PC", "Slot3", "Slot2", "Slot1", "Slot0"]
    table_data = process_asm_file(filename)
    md_table = tabulate(table_data, headers=headers, tablefmt="github")
    
    # 写入Markdown文件
    outputf = os.path.join(md_dir, f"{name}.md")
    with open(outputf, 'w', encoding='utf-8') as f:

        f.write(md_table)
    
    print("Markdown表格已生成")

if __name__ == "__main__":
    from datetime import datetime
    main()