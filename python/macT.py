import  os
import  asm_generate
import  loop
import  translator
import  merge_mif_files

def make_sg_dma_descriptor(addr):

    word0 = (addr & 0xFFFFFFFF) 
    word1 = (0x419 & 0xFFFFFFFF)
    word2 = ((addr+1) & 0xFFFFFFFF) 
    word3 = (0x419 & 0xFFFFFFFF)
    word4 = ((addr+2) & 0xFFFFFFFF) 
    word5 = (0x419 & 0xFFFFFFFF)
    word6 = ((addr+3) & 0xFFFFFFFF) 
    word7 = (0x419 & 0xFFFFFFFF)
    word8 = ((addr+4) & 0xFFFFFFFF) 
    word9 = (0x419 & 0xFFFFFFFF)
    word10 = ((addr+5) & 0xFFFFFFFF) 
    word11 = (0x419 & 0xFFFFFFFF)
    word12 = ((addr+6) & 0xFFFFFFFF) 
    word13 = (0x419 & 0xFFFFFFFF)
    word14 = ((addr+7) & 0xFFFFFFFF) 
    word15 = (0x419 & 0xFFFFFFFF)


    return [word0, word1, word2,  word3,  word4,  word5,  word6,  word7,
            word8, word9, word10, word11, word12, word13, word14, word15]

def make_F(FF):

    word0 = FF
    word1 = FF
    word2 = FF
    word3 = FF
    word4 = FF
    word5 = FF
    word6 = FF
    word7 = FF
    word8 = FF
    word9 = FF
    word10 = FF
    word11 = FF
    word12 = FF
    word13 = FF
    word14 = FF
    word15 = FF


    return [word0, word1, word2,  word3,  word4,  word5,  word6,  word7,
            word8, word9, word10, word11, word12, word13, word14, word15]



def int_to_bin8(value):
    """
    Convert a 8-bit int to a binary string of length 8 (big-endian: bit31 on the left, bit0 on the right).
    """
    return format(value & 0xFFFFFFFF, '32b')




def write_txt_file(words, filename):
    """
    Write words (each element is a 8-bit int) to the .txt file, with 8-bit binary per line, without commas or semicolons.
    """
    with open(filename, 'w') as f:
        for w in words:
            bin_str = int_to_bin8(w)
            hex_string = hex(int(bin_str, 2))
            f.write(hex_string+ "\n")

def flat(descriptor_list):
    flattened = []  # Stores the final sequentially expanded 8-bit word

    for i in range(len(descriptor_list)):
        words = descriptor_list[i]
        flattened.extend(words)

    return flattened

def main():


    script_dir = os.path.dirname(os.path.abspath(__file__))

    name1 = "GM0"

    mif_dir = os.path.join(script_dir,"mif")

    rom_file1 = os.path.join(mif_dir, f"{name1}.mif")


    with open(rom_file1, 'w') as f:
        f.write("")


    txt_dir = os.path.join(script_dir,"txt")
    all_file = os.path.join(txt_dir, f"MACT.txt")
    
    descriptorss = []

    # for i in range(90):
    #     if(i%2 == 0):
    #         A = 0
    #         word = make_sg_dma_descriptor(A)
    #         descriptorss.append(word)
    #     if(i%2 == 1):
    #         A = 0x2
    #         word = make_sg_dma_descriptor(A)
    #         descriptorss.append(word)
    #     #for j in range(31):
    #     #    A = 0
    #     #    word = make_sg_dma_descriptor(A)
    #     #    descriptorss.append(word)
    A = 0
    for i in range(10):
        
        word = make_sg_dma_descriptor(A)
        descriptorss.append(word)
        A=A+8


    for i in range(10):
        
        A = 0xFFFFFFFF
        word = make_F(A)
        descriptorss.append(word)
    deadata = flat(descriptorss)
    AL =  deadata
    write_txt_file(AL , all_file)

    

if __name__ == "__main__":
    main()



      
