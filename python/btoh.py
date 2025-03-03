import sys
import os

def convert_hex_to_bin(input_txt, output_mif):
    with open(input_txt, 'r') as f:
        hex_lines = [line.strip().upper().replace('0x', '') for line in f if line.strip()]
    
    if not hex_lines:
        print("输入文件为空或没有有效数据。")
        return
    
    hex_length = len(hex_lines[0])
    bit_width = hex_length * 4
    
    # 检查所有行长度一致
    for line in hex_lines:
        if len(line) != hex_length:
            print("错误：十六进制数的长度不一致。")
            return
        try:
            int(line, 16)
        except ValueError:
            print(f"无效的十六进制数: {line}")
            return
    
    # 检查行数是否为8的倍数
    if len(hex_lines) % 8 != 0:
        print("错误：输入数据行数不是8的倍数。")
        return
    
    bin_lines = []
    for line in hex_lines:
        dec_num = int(line, 16)
        bin_str = bin(dec_num)[2:].zfill(32)
        bin_lines.append(bin_str)
    
    # 分块处理，每8个为一组
    chunks = [bin_lines[i:i+8] for i in range(0, len(bin_lines), 8)]
    
    with open(output_mif, 'w') as f:
        for chunk in chunks:
            # 反转顺序以符合高位在后
            reversed_chunk = chunk[::-1]
            combined = ''.join(reversed_chunk)
            f.write(f"{combined}\n")

if __name__ == "__main__":

    script_dir = os.path.dirname(os.path.abspath(__file__))
    name = 'sg'
    name1 = 'GM0'
    mif_dir = os.path.join(script_dir,"mif")
    txt_dir = os.path.join(script_dir,"txt")

    input_txt = os.path.join(txt_dir, f"{name}.txt")

    output_mif = os.path.join(mif_dir, f"{name1}.mif")

    convert_hex_to_bin(input_txt, output_mif)
    print(f"转换完成！生成的MIF文件: {output_mif}")