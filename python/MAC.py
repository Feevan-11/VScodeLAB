import  os
import  asm_generate
import  loop
import  translator
import  merge_mif_files

def make_mac_head(MAC_DA,MAC_SA,STYE,DATA_DA,DATA_BBT):

    word0  = (MAC_DA    & 0xFFFFFFFF) 
    word1  = (MAC_SA    & 0xFFFFFFFF)
    word2  = (STYE      & 0xFFFFFFFF) 
    word3  = (DATA_DA   & 0xFFFFFFFF)
    word4  = (DATA_BBT  & 0xFFFFFFFF) 
    word5  = (0 & 0xFFFFFFFF)
    word6  = (0 & 0xFFFFFFFF) 
    word7  = (0 & 0xFFFFFFFF)
    word8  = (0 & 0xFFFFFFFF) 
    word9  = (0 & 0xFFFFFFFF)
    word10 = (0 & 0xFFFFFFFF) 
    word11 = (0 & 0xFFFFFFFF)
    word12 = (0 & 0xFFFFFFFF) 
    word13 = (0 & 0xFFFFFFFF)
    word14 = (0 & 0xFFFFFFFF) 
    word15 = (0 & 0xFFFFFFFF)


    return [word0, word1, word2,  word3,  word4,  word5,  word6,  word7,
            word8, word9, word10, word11, word12, word13, word14, word15]

def make_LUY(L0,L1,L2,L3,L4,L5):

    word0  = (L0    & 0xFFFFFFFF) 
    word1  = (L1    & 0xFFFFFFFF)
    word2  = (L2    & 0xFFFFFFFF) 
    word3  = (L3    & 0xFFFFFFFF)
    word4  = (L4    & 0xFFFFFFFF) 
    word5  = (L5    & 0xFFFFFFFF)
    word6  = (0 & 0xFFFFFFFF) 
    word7  = (0 & 0xFFFFFFFF)
    word8  = (0 & 0xFFFFFFFF) 
    word9  = (0 & 0xFFFFFFFF)
    word10 = (0 & 0xFFFFFFFF) 
    word11 = (0 & 0xFFFFFFFF)
    word12 = (0 & 0xFFFFFFFF) 
    word13 = (0 & 0xFFFFFFFF)
    word14 = (0 & 0xFFFFFFFF) 
    word15 = (0 & 0xFFFFFFFF)


    return [word0, word1, word2,  word3,  word4,  word5,  word6,  word7,
            word8, word9, word10, word11, word12, word13, word14, word15]


def make_end(FF):

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


    txt_dir = os.path.join(script_dir,"txt")
    all_file = os.path.join(txt_dir, f"MAC.txt")
    LUY_file = os.path.join(txt_dir, f"LUY.txt")
    descriptorss = []

    A = 0
    for i in range(9):
        MAC_DA   =   0x80000000
        MAC_SA   =   0x80000000
        STYE     =   0x1
        DATA_DA  =   0xC4000000
        DATA_BBT =   576
        if(i==1):
            MAC_DA   =   0x80000000
            MAC_SA   =   0x80000000
            STYE     =   0x1
            DATA_DA  =   0xC0000000
            DATA_BBT =   576
        elif(i==2):
            MAC_DA   =   0x80000000
            MAC_SA   =   0x80000000
            STYE     =   0x1
            DATA_DA  =   0xC2000000
            DATA_BBT =   576
        elif(i==3):
            MAC_DA   =   0x80000000
            MAC_SA   =   0x80000000
            STYE     =   0x2
            DATA_DA  =   0xC0000000
            DATA_BBT =   576
        elif(i==4):
            MAC_DA   =   0x80000000
            MAC_SA   =   0x80000000
            STYE     =   0x3
            DATA_DA  =   0xC0000000
            DATA_BBT =   576
        elif(i==5):
            MAC_DA   =   0x80000004
            MAC_SA   =   0x80000000
            STYE     =   0x3
            DATA_DA  =   0xC0000000
            DATA_BBT =   576

        elif(i==6):
            MAC_DA   =   0x80000008
            MAC_SA   =   0x80000000
            STYE     =   0x3
            DATA_DA  =   0xC0000000
            DATA_BBT =   576

        elif(i==7):
            MAC_DA   =   0x8000000C
            MAC_SA   =   0x80000000
            STYE     =   0x3
            DATA_DA  =   0xC0000000
            DATA_BBT =   576
        elif(i==8):
            MAC_DA   =   0x80000010
            MAC_SA   =   0x80000000
            STYE     =   0x3
            DATA_DA  =   0xC0000000
            DATA_BBT =   576
        
        word = make_mac_head(MAC_DA,MAC_SA,STYE,DATA_DA,DATA_BBT)
        descriptorss.append(word)
        for j in range(9):
            word = make_end(0xFF)
            descriptorss.append(word)
        


    for i in range(9):
        A = 0xFFFFFFFF
        if(i==0):
            MAC_DA   =   0x80000014
            MAC_SA   =   0x80000000
            STYE     =   0x3
            DATA_DA  =   0xC0000000
            DATA_BBT =   576
            word = make_mac_head(MAC_DA,MAC_SA,STYE,DATA_DA,DATA_BBT)
            descriptorss.append(word)
        word = make_end(A)

        descriptorss.append(word)
    deadata = flat(descriptorss)
    AL =  deadata
    write_txt_file(AL , all_file)

    descriptor_LUY = []

    
    L0 =   0xFF
    L1 =   0xF1
    L2 =   0xF2
    L3 =   0xF3
    L4 =   0xF4
    L5 =   0xFFFFFFFF
    word = make_LUY(L0,L1,L2,L3,L4,L5)
    descriptor_LUY.append(word)
    LUY_DATA  = flat(descriptor_LUY)
    write_txt_file(LUY_DATA , LUY_file)

    

if __name__ == "__main__":
    main()



      
