; --- SEGMENT 1 ---
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0002
lui  x8, 0xA4002
addi x1, x1, 0x000      
addi x2, x2, 0x400     
addi x3, x3, 0x000  
addi x4, x4, 0x000 
addi x5, x5, 0x001     
addi x6, x6, 0x000      
addi x7, x7, 0xFC0      
addi x8, x8, 0xFC0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x4, 0x34(x1)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x5,  0x38(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x30(x1) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6, 0x40(x1)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
; --- SEGMENT 2 ---
lui x1, 0x0
lui x2, 0x0
lui x3, 0x0
lui x4, 0x0
lui x5, 0x0
lui x6, 0x0
lui x7, 0x0
lui x8, 0x0
lui x15, 0x0
lui x16, 0x0
lui x17, 0x0
lui x18, 0x0
addi x1, x1, 0x0
addi x2, x2, 0x0
addi x3, x3, 0x0
addi x4, x4, 0x0
addi x5, x5, 0x0
addi x6, x6, 0x0
addi x7, x7, 0x0
addi x8, x8, 0x0
addi x15, x15, 0x0
addi x16, x16, 0x0
addi x17, x17, 0x0
addi x18, x18, 0x0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x1, 0x10

lw x10, 0xD(x7)
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x2, 0x10

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
lp.goto x2, -0x10

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
beq x10, x8, 0x60

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
lp.goto x1, -0xC0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x1, 0x10

lw x9, 0xD(x1)
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x2, 0x10
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
lp.goto x2, -0x10

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x9, x3, 0x110
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
beq x9, x4, 0x100
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
add x1, x1, x2 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
lp.goto x1, -0x110
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
lp.goto x2, 0xA0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x2, 100

addi x0, x0, 0 
addi x0, x0, 0 
add x5, x5, x3 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x2, -0x110

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x2, 100

addi x0, x0, 0 
addi x0, x0, 0 
add x6, x6, x4 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x2, -0x100

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


sw x16, 0x0(x15)
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
sw x17, 0x4(x15)
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
sw x5, 0xE(x15)
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
sw x6, 0x16(x15)
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x2, 0x30
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
lp.goto x2, -0x10

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0



; --- SEGMENT 3 ---
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0002
lui  x8, 0xA4002
addi x1, x1, 0x000      
addi x2, x2, 0x400     
addi x3, x3, 0x000  
addi x4, x4, 0x000 
addi x5, x5, 0x001     
addi x6, x6, 0x000      
addi x7, x7, 0xFC0      
addi x8, x8, 0xFC0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x4, 0x4(x1)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x5,  0x8(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x1) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6, 0x10(x1)
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
