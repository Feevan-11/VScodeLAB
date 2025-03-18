import sys
import os

def convert_hex_to_bin(input_txt, output_mif):
    with open(input_txt, 'r') as f:
        hex_lines = []
        for line in f:
            stripped_line = line.strip()
            if not stripped_line:
                continue  
            # Remove the 0x prefix and convert to uppercase
            stripped_line = stripped_line.upper().replace('0X', '')
            # Check if the hexadecimal length is more than 8 bits
            if len(stripped_line) > 8:
                print(f"Error: Hexadecimal number is too long (more than 8 digits): {stripped_line}")
                return
            # The high post makes up zero to 8
            padded_line = stripped_line.zfill(8)
            hex_lines.append(padded_line)
    
    if not hex_lines:
        print("The input file is empty or has no valid data.")
        return
    
    hex_length = 8  # After processing, all rows are guaranteed to be 8 bits
    bit_width = hex_length * 4  
    
    # Check that all rows are the same length (in this case they should all be 8 bits)
    for line in hex_lines:
        if len(line) != hex_length:
            print("Error: The length of the hexadecimal number is inconsistent.")
            return
        try:
            int(line, 16)
        except ValueError:
            print(f"Invalid hexadecimal numbers: {line}")
            return
    
    # Check if the number of rows is a multiple of 8
    if len(hex_lines) % 8 != 0:
        print("Error: The number of rows of input data is not a multiple of 8.")
        return
    
    bin_lines = []
    for line in hex_lines:
        dec_num = int(line, 16)
        bin_str = bin(dec_num)[2:].zfill(32)  
        bin_lines.append(bin_str)
    
   # Divided into blocks, every group of 8
    chunks = [bin_lines[i:i+8] for i in range(0, len(bin_lines), 8)]
    
    with open(output_mif, 'w') as f:
        for chunk in chunks:
            # Reverse the order to conform to the high post last
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
    print(f"The conversion is complete! MIF file generated: {output_mif}")

if __name__ == "__main__":
    main()