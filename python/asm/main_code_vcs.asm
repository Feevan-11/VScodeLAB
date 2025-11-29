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
sw x3,  0x0(x1)
addi x0, x0, 0


addi x0, x0, 0
addi x0, x0, 0
sw x4, 0x4(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
sw x5, 0x18(x1)
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
sw x3,  0x0(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
sw x4, 0x4(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
sw x5, 0x18(x2)
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
sw x8, 0x20(x2)
addi x0, x0, 0 

addi x0, x0, 0   
addi x0, x0, 0        
sw x7, 0x28(x2)
addi x0, x0, 0 


addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x2, 0x100

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

lui  x11, 0xC0000
lui  x12, 0xC0000
lui  x13, 0xA0001
lui  x14, 0xA4001
lui  x15, 0x00401
lui  x16, 0x00001
lui  x17, 0xA0002
lui  x18, 0xA4002
addi x11, x11, 0x000      
addi x12, x12, 0x400     
addi x13, x13, 0x000  
addi x14, x14, 0x000 
addi x15, x15, 0x001     
addi x16, x16, 0x000      
addi x17, x17, 0xFC0      
addi x18, x18, 0xFC0

addi x0, x0, 0
addi x0, x0, 0 
sw x14, 0x34(x11)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x15,  0x38(x11)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x13, 0x30(x11) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
sw x16, 0x40(x11) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x14, 0x4(x12)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x17,  0x8(x12)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
sw x13, 0x0(x12)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x18, 0x10(x12)
addi x0, x0, 0 

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
lui x16, 0x0
lui x17, 0x0
lui x18, 0x0
lui x19, 0x0
lui x20, 0x0
lui x21, 0x0
lui x22, 0x0

lui x23, 0x0
lui x24, 0x0
addi x0, x0, 0
addi x0, x0, 0 

addi x11, x11, 0x0
addi x12, x12, 0x0
addi x13, x13, 0x0
addi x14, x14, 0x0
addi x15, x15, 0x0
addi x16, x16, 0x0
addi x17, x17, 0x0
addi x18, x18, 0x0
addi x19, x19, 0x0
addi x20, x20, 0x0
addi x21, x21, 0x0
addi x22, x22, 0x0

addi x23, x23, 0x0
addi x24, x24, 0x0
addi x0, x0, 0
addi x0, x0, 0

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
beq x19, x18, 0x60

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
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

lw x12, 0x4(x20)
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

lw x11 0x4(x20)
;lw x11, 0x0(x12)
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
beq x14, x11, 0x340

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
beq x15, x11, 0x4B0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x16, x11, 0x620

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x17, x11, 0x790

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x13, x11, 0x900

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0
addi x24, x24, 0x40 
add x21, x21, x22 
add x20, x20, x22 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
lp.goto x1, -0x280

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
beq x23, x20 0x80

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x3, 0x10

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
lp.goto x3, -0xD0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x3, 0x10

sw x0, 0x0(x23) 
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
lp.goto x3, -0x6F0

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

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

; --- SEGMENT 3 ---
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0002
lui  x8, 0xA4002
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
addi x5, x5, 0x001
addi x6, x6, 0x000
addi x7, x7, 0xFC0
addi x8, x8, 0xFC
addi x1, x1, 0x000
addi x2, x2, 0x400
addi x3, x3, 0x000
addi x4, x4, 0x000

add x5, x24, x5
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x4,  0x0(x1)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
sw x4, 0x4(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
sw x5, 0x18(x1)
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
lp.setup x2, 100

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
sw x0, 0x0(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6, 0x10(x2)
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
lp.goto x2, -0x310

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

; --- SEGMENT 4 ---
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0002
lui  x8, 0xA4002
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
addi x5, x5, 0x001
addi x6, x6, 0x000
addi x7, x7, 0xFC0
addi x8, x8, 0xFC
addi x1, x1, 0x000
addi x2, x2, 0x400
addi x3, x3, 0x000
addi x4, x4, 0x000

add x5, x24, x5
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x4,  0x0(x1)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
sw x4, 0x4(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
sw x5, 0x18(x1)
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
lp.setup x2, 100

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
sw x0, 0x0(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6, 0x10(x2)
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
lp.goto x2, -0x4D0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0


; --- SEGMENT 5 ---
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0002
lui  x8, 0xA4002
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
addi x5, x5, 0x001
addi x6, x6, 0x000
addi x7, x7, 0xFC0
addi x8, x8, 0xFC
addi x1, x1, 0x000
addi x2, x2, 0x400
addi x3, x3, 0x000
addi x4, x4, 0x000

add x5, x24, x5
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x4,  0x0(x1)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
sw x4, 0x4(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
sw x5, 0x18(x1)
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
lp.setup x2, 100

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
sw x0, 0x0(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6, 0x10(x2)
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
lp.goto x2, -0x690

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

; --- SEGMENT 6 ---
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0002
lui  x8, 0xA4002
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
addi x5, x5, 0x001
addi x6, x6, 0x000
addi x7, x7, 0xFC0
addi x8, x8, 0xFC
addi x1, x1, 0x000
addi x2, x2, 0x400
addi x3, x3, 0x000
addi x4, x4, 0x000

add x5, x24, x5
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x4,  0x0(x1)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
sw x4, 0x4(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
sw x5, 0x18(x1)
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
lp.setup x2, 100

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
sw x0, 0x0(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x4, 0x4(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6,  0x8(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x6, 0x10(x2)
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
lp.goto x2, -0x850

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0


; --- SEGMENT 7 ---

lui x1, 0x0
lui x2, 0x0
lui x3, 0x0
lui x4, 0x0

addi x0, x0, 0x0
addi x0, x0, 0x0
addi x0, x0, 0x0
addi x0, x0, 0x0

addi x1, x1, 0x0
addi x2, x2, 0x0
addi x3, x3, 0x0
addi x4, x4, 0x0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

lw x5, 0x8(x20)
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
beq x1, x5, 0x160

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0
beq x2, x5, 0x330

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
beq x3, x5, 0x110


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0
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
lp.goto x2, -0xA20

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
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

addi x0, x0, 0       
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
lp.setup x2, 0x5

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x3, 0x5

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
lp.goto x2, -0x290

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
lp.goto x2, 0x240

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

# 10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
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
lp.goto x2, -0x470

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
