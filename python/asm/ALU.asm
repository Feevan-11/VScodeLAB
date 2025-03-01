lui   x1,  0x10000
lui   x2,  0x20000
lui   x3,  0x30000
lui   x4,  0x40000
lui   x5,  0x00000
lui   x6,  0x80000
lui   x7,  0x90000
lui   x8,  0xf0000
lui   x9,  0xf0000
lui   x10,  0xf0000
lui   x11,  0x10000
lui   x12,  0x20000
lui   x13,  0x30000
lui   x14,  0x40000
lui   x15,  0x00000
lui   x16,  0x80000
lui   x17,  0x90000
lui   x18,  0xf0000
lui   x19,  0xf0000
lui   x20,  0xf0000
lui   x21,  0x10000
lui   x22,  0x20000
lui   x23,  0x30000
lui   x24,  0x40000
lui   x25,  0x00000
lui   x26,  0x80000
lui   x27,  0x90000
lui   x28,  0xf0000
lui   x29,  0xf0000
lui   x30,  0xf0000
lui   x31,  0xf0000
addi  x0,  x0, 0x0 
addi  x1,  x1, 0x101      
addi  x2,  x2, 0x102   
addi  x3,  x3, 0x103
addi  x4,  x4, 0x104
addi  x5,  x5, 0xfff
addi  x6,  x6, 0x101      
addi  x7,  x7, 0x102   
addi  x8,  x8, 0x103
addi  x9,  x9, 0x104
addi  x10, x10, 0xfff
addi  x11,  x11, 0x101      
addi  x12,  x12, 0x102   
addi  x13,  x13, 0x103
addi  x14,  x14, 0x104
addi  x15,  x15, 0x000
addi  x16,  x16, 0x101      
addi  x17,  x17, 0x102   
addi  x18,  x18, 0x103
addi  x19,  x19, 0x104
addi  x20, x20, 0xfff
addi  x21,  x21, 0x101      
addi  x22,  x22, 0x102   
addi  x23,  x23, 0x103
addi  x24,  x24, 0x104
addi  x25,  x25, 0xfff
addi  x26,  x26, 0x101      
addi  x27,  x27, 0x102   
addi  x28,  x28, 0x103
addi  x29,  x29, 0x104
addi  x30, x30, 0xfff
addi  x31, x31, 0xfff
add   x5,  x2,  x3    
sub   x6,  x2,  x1    
xor   x7,  x8,  x9    
or    x10, x11, x12   
and   x13, x14, x15   
sll   x16, x17, x18   
srl   x19, x20, x21   
sra   x22, x23, x24   
slt   x25, x26, x27  
sltu  x28, x29, x30   
xori  x31, x1,  0xFF   
ori   x2,  x3,  0x1F   
andi  x4,  x5,  0x555  
slli  x6,  x7,  3      
srli  x8,  x9,  5      
srai  x10, x11, 7      
slti  x12, x13, -5     
sltiu x14, x15, 0x800      
auipc x28, 0x12345     
addi  x0,  x0, 0x0 
addi  x0,  x0, 0x0  