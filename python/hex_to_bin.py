import sys
import os

def convert_hex_to_bin(input_txt, output_mif):
    with open(input_txt, 'r') as f:
        hex_lines = []
        for line in f:
            stripped_line = line.strip()
            if not stripped_line:
                continue  # 跳过空行
            # 去掉0x前缀并转换为大写
            stripped_line = stripped_line.upper().replace('0X', '')
            # 检查十六进制长度是否超过8位
            if len(stripped_line) > 8:
                print(f"错误：十六进制数过长（超过8位）: {stripped_line}")
                return
            # 高位补零到8位
            padded_line = stripped_line.zfill(8)
            hex_lines.append(padded_line)
    
    if not hex_lines:
        print("输入文件为空或没有有效数据。")
        return
    
    hex_length = 8  # 经过处理后，所有行都保证为8位
    bit_width = hex_length * 4  # 固定为32位
    
    # 检查所有行长度是否一致（此时应均为8位）
    for line in hex_lines:
        if len(line) != hex_length:
            print("错误：十六进制数的长度不一致。")
            return
        try:
            int(line, 16)
        except ValueError:
            print(f"无效的十六进制数: {line}")
            return
    
    # 检查行数是否为16的倍数（因为512位/32位=16个元素）
    if len(hex_lines) % 16 != 0:
        print("错误：输入数据行数不是16的倍数。")
        return
    
    bin_lines = []
    for line in hex_lines:
        dec_num = int(line, 16)
        bin_str = bin(dec_num)[2:].zfill(32)  # 确保二进制长度为32位
        bin_lines.append(bin_str)
    
    # 分块处理，每16个为一组（512位）
    chunks = [bin_lines[i:i+16] for i in range(0, len(bin_lines), 16)]
    
    with open(output_mif, 'w') as f:
        for chunk in chunks:
            # 反转顺序以符合高位在后
            reversed_chunk = chunk[::-1]
            combined = ''.join(reversed_chunk)
            f.write(f"{combined}\n")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name = 'allsg'
    name1 = 'GM0'
    mif_dir = os.path.join(script_dir, "mif")
    txt_dir = os.path.join(script_dir, "txt")

    input_txt = os.path.join(txt_dir, f"{name}.txt")
    output_mif = os.path.join(mif_dir, f"{name1}.mif")

    convert_hex_to_bin(input_txt, output_mif)
    print(f"转换完成！生成的MIF文件: {output_mif}")

def MACT():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name = 'MACT'
    name1 = 'MAC_GM1'
    mif_dir = os.path.join(script_dir, "mif")
    txt_dir = os.path.join(script_dir, "txt")

    input_txt = os.path.join(txt_dir, f"{name}.txt")
    output_mif = os.path.join(mif_dir, f"{name1}.mif")

    convert_hex_to_bin(input_txt, output_mif)
    print(f"转换完成！生成的MIF文件: {output_mif}")

def MAC():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name = 'MAC'
    name1 = 'MAC_GM0'
    name0 = 'LUY'
    name01 = 'LUY_GM1'
    mif_dir = os.path.join(script_dir, "mif")
    txt_dir = os.path.join(script_dir, "txt")

    input_txt0 = os.path.join(txt_dir, f"{name}.txt")
    output_mif0 = os.path.join(mif_dir, f"{name1}.mif")

    input_txt1 = os.path.join(txt_dir, f"{name0}.txt")
    output_mif1 = os.path.join(mif_dir, f"{name01}.mif")
    convert_hex_to_bin(input_txt0, output_mif0)
    convert_hex_to_bin(input_txt1, output_mif1)
    print(f"转换完成！生成的MIF文件: {output_mif0}")

def test():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    name = 'dma0_test_sg'
    name1 = 'test_sg'
    mif_dir = os.path.join(script_dir, "mif")
    txt_dir = os.path.join(script_dir, "txt")

    input_txt = os.path.join(txt_dir, f"{name}.txt")
    output_mif = os.path.join(mif_dir, f"{name1}.mif")

    convert_hex_to_bin(input_txt, output_mif)
    print(f"转换完成！生成的MIF文件: {output_mif}")

def dmasg():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    file_configs = [
        {'input_name': 'dma0_sg', 'output_name': 'DMA0'},
        {'input_name': 'dma1_sg', 'output_name': 'DMA1'},
        {'input_name': 'ethdma4_sg', 'output_name': 'ETHDMA4'}
        
         
    ]
    
    mif_dir = os.path.join(script_dir, "mif")
    txt_dir = os.path.join(script_dir, "txt")

    for config in file_configs:
        input_txt = os.path.join(txt_dir, f"{config['input_name']}.txt")
        output_mif = os.path.join(mif_dir, f"{config['output_name']}.mif")

        convert_hex_to_bin(input_txt, output_mif)
        print(f"转换完成！生成的MIF文件: {output_mif}")

def ETH_TILE_sg():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    file_configs = [

        {'input_name': 'eth_tile_sg', 'output_name': 'ETH_TILE_SG'}
         
    ]
    
    mif_dir = os.path.join(script_dir, "mif_test")
    txt_dir = os.path.join(script_dir, "txt")

    for config in file_configs:
        input_txt = os.path.join(txt_dir, f"{config['input_name']}.txt")
        output_mif = os.path.join(mif_dir, f"{config['output_name']}.mif")

        convert_hex_to_bin(input_txt, output_mif)
        print(f"转换完成！生成的MIF文件: {output_mif}")


if __name__ == "__main__":
    main()