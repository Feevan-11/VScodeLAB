import  os
import  asm_generate
import  translator
import  merge_mif_files

def make_sg_dma_descriptor(addr):

    word0 = 0 
    word1 = 0
    word2 = (addr+1)
    word3 = (addr & 0xFFFFFFFF)
    word4 = 0
    word5 = 0
    word6 = 0
    word7 = 0
    word8 = 0 
    word9 = 0
    word10 = 0
    word11 = 0
    word12 = 0
    word13 = 0
    word14 = 0
    word15 = 0


    return [word0, word1, word2,  word3,  word4,  word5,  word6,  word7,
            word8, word9, word10, word11, word12, word13, word14, word15]

def make_F(A,B,C,D,E,F,G,H):

    word0 = A
    word1 = B
    word2 = C
    word3 = D
    word4 = E
    word5 = F
    word6 = G
    word7 = H
    word8 =  A
    word9 =  B
    word10 = C
    word11 = D
    word12 = E
    word13 = F
    word14 = G
    word15 = H


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

    for i in range(90):
        if(i%2 == 0):
            A = 0x01
            B = 0x02
            C = 0x03
            D = 0x04
            E = 0x05
            F = 0x06
            G = 0x07
            H = 0x08
            word = make_F(A,B,C,D,E,F,G,H)
            descriptorss.append(word)
        if(i%2 == 1):
            A = 0x01
            B = 0x02
            C = 0x03
            D = 0x04
            E = 0x05
            F = 0x06
            G = 0x07
            H = 0x08
            word = make_F(A,B,C,D,E,F,G,H)
            descriptorss.append(word)
        #for j in range(31):
        #    A = 0
        #    word = make_sg_dma_descriptor(A)
        #    descriptorss.append(word)
    for i in range(10):
        
        A = 0x01
        B = 0x02
        C = 0x03
        D = 0x04
        E = 0x05
        F = 0x06
        G = 0x07
        H = 0x08
        word = make_F(A,B,C,D,E,F,G,H)
        descriptorss.append(word)
    deadata = flat(descriptorss)
    AL =  deadata
    write_txt_file(AL , all_file)

    

if __name__ == "__main__":
    main()



      
