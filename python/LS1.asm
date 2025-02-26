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
addi  x1,  x1, 0x101      
addi  x2,  x2, 0x102   
addi  x3,  x3, 0x103
addi  x4,  x4, 0x800
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
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
sw x6, 0(x4)         
sb x7, 0(x15) 
sh x8, 0(x16)
addi x0, x0, 0
sw x1, 0x4(x4)         
sb x2, 0x4(x15) 
sh x3, 0x4(x16)
addi x0, x0, 0
sw x4, 0x8(x4)         
sb x5, 0x8(x15) 
sh x9, 0x8(x16)
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
lb    x21, 0(x15)     
lh    x22, 0(x16)      
lbu   x23, 0(x15)
addi x0, x0, 0
lw    x24, 0(x4)     
lhu   x25, 0(x16) 
lb    x26, 0x4(x15)
addi x0, x0, 0
lh    x27, 0x4(x16)      
lbu   x28, 0x4(x15)
lw    x29, 0x4(x4)
addi x0, x0, 0
lhu   x30, 0x4(x16) 
lb    x31, 0x8(x15)
lh    x17, 0x8(x16) 
addi x0, x0, 0