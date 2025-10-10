import os
from tabulate import tabulate

def process_asm_file(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(';'):
                    continue
            line = line.split('#')[0].split(';')[0].strip()
            if line and not line.endswith(':'):
                if ':' in line:
                    line = line.split(':', 1)[1].strip()
                instructions.append(line)
    
    # Generate Markdown tabular data
    table_data = []
    address = 0
    for i in range(0, len(instructions), 4):
        group = instructions[i:i+4]
        while len(group) < 4:
            group.append('')
        table_data.append([
            f"`0x{address:04X}`", 
            *[f"`{instr}`" if instr else "" for instr in group]  
        ])
        address += 16
    
    return table_data

def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    names = ['SA','SG','CHECK_']
    md_dir = os.path.join(script_dir,"md")
    asm_dir = os.path.join(script_dir,"asm")
    for name in names:
        filename = os.path.join(asm_dir, f"{name}.asm")

        if not filename:
            print("Not found.asm文件")
            return

        print(f"Work with files: {filename}")
    
    # Generate Markdown content
        headers = ["PC", "Slot3", "Slot2", "Slot1", "Slot0"]
        table_data = process_asm_file(filename)
        md_table = tabulate(table_data, headers=headers, tablefmt="github")
    
        # Write to a Markdown file
        outputf = os.path.join(md_dir, f"{name}.md")
        with open(outputf, 'w', encoding='utf-8') as f:

            f.write(md_table)
    
        print("A Markdown table has been generated")

if __name__ == "__main__":
    main()