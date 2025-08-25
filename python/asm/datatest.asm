; --- SEGMENT 1 ---
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0000
lui  x4, 0xA4000
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0001
lui  x8, 0xA4001
addi x1, x1, 0x000      
addi x2, x2, 0x400     
addi x3, x3, 0x000  
addi x4, x4, 0x000 
addi x5, x5, 0x001     
addi x6, x6, 0x000      
addi x7, x7, 0xFC0      
addi x8, x8, 0xFC0
lui  x9, 0xC0000
sw x4,  0x38(x2)
sw x3,  0x38(x1)
lui  x10, 0xC0000
lui  x11, 0xC0000
sw x8,  0x8(x2)
sw x7,  0x8(x1)
lui  x12, 0xC0000
addi x9, x9, 0
sw x6, 0x34(x2)
sw x6, 0x34(x1)
addi x10, x10, 0
addi x11, x11, 0 
sw x6, 0x4(x2)
sw x6, 0x4(x1)
addi x12, x12, 0 
addi x0, x0, 0 
sw x5, 0x30(x2)
sw x5, 0x30(x1)
addi x0, x0, 0
addi x0, x0, 0
sw x5, 0x0(x2) 
sw x5, 0x0(x1)
addi x0, x0, 0  
addi x0, x0, 0 
sw x10, 0x10(x2)
sw x9, 0x10(x1) 
addi x0, x0, 0
addi x0, x0, 0 
sw x12, 0x10(x2)
sw x11, 0x10(x1) 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x1,  5
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x2,  100
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
lp.goto x1, -0x40 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0  
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 