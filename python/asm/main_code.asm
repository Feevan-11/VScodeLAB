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
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x7,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
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

; --- SEGMENT 2 ---
lui x11, 0x0
lui x12, 0x0
lui x13, 0x0
lui x14, 0x0
lui x15, 0x0
lui x10, 0x0
lui x7, 0x0
lui x8, 0x0
lui x20, 0x0
lui x21, 0x0
lui x22, 0x0
lui x23, 0x0
addi x11, x11, 0x0
addi x12, x12, 0x0
addi x13, x13, 0x0
addi x14, x14, 0x0
addi x15, x15, 0x0
addi x10, x10, 0x0
addi x7, x7, 0x0
addi x8, x8, 0x0
addi x20, x20, 0x0
addi x21, x21, 0x0
addi x22, x22, 0x0
addi x23, x23, 0x0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x1, 0x20

lw x19, 0x0(x23)
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
beq x19, x15, 0x60

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
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
lp.setup x1, 0x100

lw x2, 0x4(x20)
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

lw x1, 0x0(x2)
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
beq x11, x1, 0x2C0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
beq x12, x1, 0x3D0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x13, x1, 0x5F0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x14, x1, 0x700

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x10, x1, 0x810

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x15, x1, 0x80

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
add x21, x21, x22 
add x20, x20, x22 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
lp.goto x1, -0x380

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

sw x2, 0x0(x23)
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
lp.setup x2, 0x10

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
lp.goto x2, -0x5C0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

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
addi x8, x8, 0xFC

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

sw x20, 0x8(x5)
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
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x7,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x8, 0x10(x2)
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
lp.setup x2, 0x10

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x2, -0x260

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

; --- SEGMENT 4 ---
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
addi x8, x8, 0xFC
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

sw x20, 0x8(x5)
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
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x7,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x8, 0x10(x2)
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
lp.setup x2, 0x10

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x2, -0x3C0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0


; --- SEGMENT 5 ---
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
addi x8, x8, 0xFC
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

sw x20, 0x8(x5)
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
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x7,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x8, 0x10(x2)
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
lp.setup x2, 0x10

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x2, -0x650

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

; --- SEGMENT 6 ---
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
addi x8, x8, 0xFC
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

sw x20, 0x8(x5)
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
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x7,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x8, 0x10(x2)
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
lp.setup x2, 0x10

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x2, -0x790

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

; --- SEGMENT 7 ---

lui x9, 0x0
lui x16, 0x0
lui x17, 0x0
lui x18, 0x0

addi x0, x0, 0x0
addi x0, x0, 0x0
addi x0, x0, 0x0
addi x0, x0, 0x0

addi x9, x9, 0x0
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
addi x0, x0, 0 

lw x9, 0x8(x20)
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
beq x16, x9, 0x160

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
beq x17, x9, 0x320

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x9, x18, 0x110


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
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
lp.goto x2, -0x960

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0


; --- SEGMENT 8 ---
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
addi x8, x8, 0xFC

addi x26, x26, 1       
addi x0, x0, 0
addi x0, x0, 0        
addi x0, x0, 0

addi x0, x0, 0        
addi x0, x0, 0
addi x0, x0, 0        
addi x0, x0, 0

lw x6, 0x10(x20)
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

lw x7, 0x14(x20)
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
sw x3,  0x0(x1)
addi x0, x0, 0 

addi x0, x0, 0        
addi x0, x0, 0
sw x4, 0x4(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
sw x21, 0x18(x1)
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
sw x6, 0x20(x1)
addi x0, x0, 0 

addi x0, x0, 0   
addi x0, x0, 0        
sw x7, 0x28(x1)
addi x0, x0, 0 

addi x0, x0, 0 
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
lp.setup x3, 0x4

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
lp.goto x3, -0x10

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
lp.goto x2, -0x40

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
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
lp.goto x2, -0x270

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
# 9
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x30, x30, 100

addi x0, x0, 0 
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
lp.goto x2, 0x210

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

# 10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x31, x31, 200

addi x0, x0, 0 
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
lp.goto x2, -0x340

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
