; --- SEGMENT 1 ---
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0002
lui  x8, 0xA4002
lui  x9, 0x00401
lui  x10, 0x00001
lui  x11, 0xA0002
lui  x12, 0xA4002
addi x1, x1, 0x000      
addi x2, x2, 0x400     
addi x3, x3, 0x000  
addi x4, x4, 0x000 
addi x5, x5, 0x001     
addi x6, x6, 0x000      
addi x7, x7, 0xFC0      
addi x8, x8, 0xFC0
addi x9, x9, 0x001     
addi x10, x10, 0x000      
addi x11, x11, 0xFC0      
addi x12, x12, 0xFC0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x25, x25, 1

addi x0, x0, 0 
sw x6, 0x34(x2)
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
sw x4,  0x38(x2)
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
sw x5, 0x30(x2) 
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
sw x8, 0x40(x2)
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
sw x6, 0x34(x1)
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
sw x3,  0x38(x1)
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
sw x5, 0x30(x1)
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
sw x7, 0x40(x1) 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup  x2, 50

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
sw x6, 0x4(x1)
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
sw x9,  0x8(x1)
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
sw x5, 0x0(x1) 
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
sw x11, 0x10(x1)
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0
sw x6, 0x4(x2)
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
sw x10,  0x8(x2)
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
sw x5, 0x0(x2)
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0
sw x12, 0x10(x2) 
addi x0, x0, 0 
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup  x2, 100

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
addi x0, x0, 0 
; --- SEGMENT 2 ---
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
addi x25, x25, 1


addi x0, x0, 0
addi x0, x0, 0
sw x0, 0x0(x2) 
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
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
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
lp.goto x2, -0x450

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

