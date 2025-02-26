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
addi  x0,  x0, 0x0
addi  x0,  x0, 0x0
addi  x0,  x0, 0x0
addi  x0,  x0, 0x0
lp.setup  x1, 5
add   x5,  x4,  x3    
sub   x6,  x2,  x1    
xor   x7,  x8,  x9 
or    x10, x11, x12
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x1, -0x10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
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
lui   x1,  0x10000
lui   x2,  0x20000
lui   x3,  0x30000
lui   x4,  0x40000
lui   x5,  0x50000
lui   x6,  0x60000
lui   x7,  0x70000
lui   x8,  0x80000
lui   x9,  0x90000
lui   x10,  0xA0000
lui   x11,  0xB0000
lui   x12,  0xC0000
lui   x13,  0xD0000
lui   x14,  0xE0000
lui   x15,  0xF0000
lui   x16,  0xC0000
lui   x17,  0xC0000
lui   x18,  0xC0001
lui   x19,  0xC0001
lui   x20,  0x00000
lui   x21,  0x40000
lui   x22,  0x10000
lui   x23,  0x20000
lui   x24,  0x30000
lui   x25,  0x40000
lui   x26,  0x50000
lui   x27,  0x60000
lui   x28,  0x70000
lui   x29,  0x80000
lui   x30,  0x90000
lui   x31,  0xf0000
addi  x0,  x0, 0x1 
addi  x1,  x1, 0x2      
addi  x2,  x2, 0x3   
addi  x3,  x3, 0x4
addi  x4,  x4, 0x5
addi  x5,  x5, 0x6
addi  x6,  x6, 0x7      
addi  x7,  x7, 0x8   
addi  x8,  x8, 0x9
addi  x9,  x9, 0xA
addi  x10, x10, 0xB
addi  x11,  x11, 0xC      
addi  x12,  x12, 0xD  
addi  x13,  x13, 0xE
addi  x14,  x14, 0xF
addi  x15,  x15, 0x000
addi  x16,  x16, 0x000      
addi  x17,  x17, 0x400   
addi  x18,  x18, 0x800
addi  x19,  x19, 0x840
addi  x20, x20, 0x000
addi  x21,  x21, 0x000      
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
addi  x0,  x0, 0x0
sw  x1, 0x0(x20)
sw  x1, 0x0(x17)
sw  x1, 0x0(x16)
addi  x0,  x0, 0x0
sb  x1, 0x4(x20)
sb  x1, 0x4(x17)
sb  x1, 0x4(x16)
addi  x0,  x0, 0x0
sh  x1, 0x8(x20)
sh  x1, 0x8(x17)
sh  x1, 0x8(x16)
addi  x0,  x0, 0x0
lw  x2, 0x0(x20)
lw  x2, 0x0(x17)
lw  x2, 0x0(x16)
addi  x0,  x0, 0x0
lb  x2, 0x4(x20)
lb  x2, 0x4(x17)
lb  x2, 0x4(x16)
addi  x0,  x0, 0x0
lh  x2, 0x8(x20)
lh  x2, 0x8(x17)
lh  x2, 0x8(x16)
addi  x0,  x0, 0x0
lbu  x3, 0x4(x20)
lbu  x3, 0x4(x17)
lbu  x3, 0x4(x16)
addi  x0,  x0, 0x0
lhu  x3, 0x8(x20)
lhu  x3, 0x8(x17)
lhu  x3, 0x8(x16)
addi  x0,  x0, 0x0
addi  x0,  x0, 0x0
addi  x0,  x0, 0x0
addi  x0,  x0, 0x0
lp.setup  x1, 5
lw  x4, 0x0(x20)
lw  x4, 0x0(x17)
lw  x4, 0x0(x16)
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.goto x1, -0x10
sw  x1, 0x18(x20)
sw  x1, 0x18(x17)
sw  x1, 0x18(x16)
addi  x0,  x0, 0x0
sw  x1, 0x24(x20)
sw  x1, 0x24(x17)
sw  x1, 0x24(x16)
addi  x0,  x0, 0x0
sw  x2, 0x28(x20)
sw  x2, 0x28(x17)
sw  x2, 0x28(x16)
addi  x0,  x0, 0x0
sw  x3, 0x2c(x20)
sw  x3, 0x2c(x17)
sw  x3, 0x2c(x16)
addi  x0,  x0, 0x0
sw  x4, 0x34(x20)
sw  x4, 0x34(x17)
sw  x4, 0x34(x16)
addi  x0,  x0, 0x0
sw  x5, 0x38(x20)
sw  x5, 0x38(x17)
sw  x5, 0x38(x16)
addi  x0,  x0, 0x0
sw  x6, 0x3c(x20)
sw  x6, 0x3c(x17)
sw  x6, 0x3c(x16)
addi  x0,  x0, 0x0
sw  x7, 0x48(x20)
sw  x7, 0x48(x17)
sw  x7, 0x48(x16)
addi  x0,  x0, 0x0
sw  x8, 0x4c(x20)
sw  x8, 0x4c(x17)
sw  x8, 0x4c(x16)
addi  x0,  x0, 0x0
sw  x9, 0x4c(x20)
sw  x9, 0x4c(x17)
sw  x9, 0x4c(x16)
addi  x0,  x0, 0x0
sw  x10, 0x50(x20)
sw  x10, 0x50(x17)
sw  x10, 0x50(x16)
addi  x0,  x0, 0x0
sw  x11, 0x124(x20)
sw  x11, 0x124(x17)
sw  x11, 0x124(x16)
addi  x0,  x0, 0x0
sw  x12, 0x128(x20)
sw  x12, 0x128(x17)
sw  x12, 0x128(x16)
addi  x0,  x0, 0x0
sw  x13, 0x12c(x20)
sw  x13, 0x12c(x17)
sw  x13, 0x12c(x16)
addi  x0,  x0, 0x0
sw  x14, 0x134(x20)
sw  x14, 0x134(x17)
sw  x14, 0x134(x16)
addi  x0,  x0, 0x0
sw  x15, 0x138(x20)
sw  x15, 0x138(x17)
sw  x15, 0x138(x16)
addi  x0,  x0, 0x0
sw  x16, 0x13c(x20)
sw  x16, 0x13c(x17)
sw  x16, 0x13c(x16)
addi  x0,  x0, 0x0
sw  x17, 0x148(x20)
sw  x17, 0x148(x17)
sw  x17, 0x148(x16)
addi  x0,  x0, 0x0
sw  x18, 0x14c(x20)
sw  x18, 0x14c(x17)
sw  x18, 0x14c(x16)
addi  x0,  x0, 0x0
sw  x19, 0x14c(x20)
sw  x19, 0x14c(x17)
sw  x19, 0x14c(x16)
addi  x0,  x0, 0x0
sw  x20, 0x150(x20)
sw  x20, 0x150(x17)
sw  x20, 0x150(x16)
addi  x0,  x0, 0x0
lw  x1, 0x24(x20)
lw  x11, 0x24(x17)
lw  x12, 0x24(x16)
addi  x0,  x0, 0x0
lw  x2, 0x28(x20)
lw  x21, 0x28(x17)
lw  x22, 0x28(x16)
addi  x0,  x0, 0x0
sw  x3, 0x2c(x20)
lw  x30, 0x2c(x17)
lw  x31, 0x2c(x16)
addi  x0,  x0, 0x0
lw  x14, 0x34(x20)
lw  x24, 0x34(x17)
lw  x4, 0x34(x16)
addi  x0,  x0, 0x0
lw  x15, 0x38(x20)
lw  x25, 0x38(x17)
lw  x5, 0x38(x16)
addi  x0,  x0, 0x0
lw  x16, 0x3c(x20)
lw  x26, 0x3c(x17)
lw  x6, 0x3c(x16)
addi  x0,  x0, 0x0
lw  x17, 0x48(x20)
lw  x27, 0x48(x17)
lw  x7, 0x48(x16)
addi  x0,  x0, 0x0
lw  x18, 0x4c(x20)
lw  x28, 0x4c(x17)
lw  x8, 0x4c(x16)
addi  x0,  x0, 0x0
lw  x19, 0x4c(x20)
lw  x29, 0x4c(x17)
lw  x9, 0x4c(x16)
addi  x0,  x0, 0x0
lw  x10, 0x50(x20)
lw  x12, 0x50(x17)
lw  x13, 0x50(x16)
addi  x0,  x0, 0x0
lw  x11, 0x124(x20)
lw  x21, 0x124(x17)
lw  x1, 0x124(x16)
addi  x0,  x0, 0x0
lw  x12, 0x128(x20)
lw  x22, 0x128(x17)
lw  x2, 0x128(x16)
addi  x0,  x0, 0x0
lw  x13, 0x12c(x20)
lw  x23, 0x12c(x17)
lw  x3, 0x12c(x16)
addi  x0,  x0, 0x0
lw  x14, 0x134(x20)
lw  x24, 0x134(x17)
lw  x4, 0x134(x16)
addi  x0,  x0, 0x0
lw  x15, 0x138(x20)
lw  x25, 0x138(x17)
lw  x5, 0x138(x16)
addi  x0,  x0, 0x0
lw  x16, 0x13c(x20)
lw  x26, 0x13c(x17)
lw  x6, 0x13c(x16)
addi  x0,  x0, 0x0
lw  x7, 0x148(x20)
lw  x17, 0x148(x17)
lw  x27, 0x148(x16)
addi  x0,  x0, 0x0
lw  x8, 0x14c(x20)
lw  x18, 0x14c(x17)
lw  x28, 0x14c(x16)
addi  x0,  x0, 0x0
lw  x9, 0x14c(x20)
lw  x19, 0x14c(x17)
lw  x29, 0x14c(x16)
addi  x0,  x0, 0x0
lw  x2, 0x150(x20)
lw  x20, 0x150(x17)
lw  x30, 0x150(x16)
addi  x0,  x0, 0x0
sw  x16, 0x13c(x20)
sw  x16, 0x13c(x17)
sw  x16, 0x13c(x16)
addi  x0,  x0, 0x0
lw  x2, 0x150(x20)
lw  x20, 0x150(x17)
lw  x30, 0x150(x16)
addi  x0,  x0, 0x0
sw  x16, 0x13c(x20)
sw  x16, 0x13c(x17)
sw  x16, 0x13c(x16)
addi  x0,  x0, 0x0
lw  x2, 0x150(x20)
lw  x20, 0x150(x17)
lw  x30, 0x150(x16)
addi  x0,  x0, 0x0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup  x1, 6
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup  x2, 3
add   x5,  x4,  x3    
sub   x6,  x2,  x1    
xor   x7,  x8,  x9 
or    x10, x11, x12
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x1, -0x10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x0, -0x40
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0