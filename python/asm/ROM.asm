lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0000
lui  x4, 0xA4000
lui x5, 0x0
lui x6, 0xA8000
lui x7, 0x40000
lui x8, 0xB0001
addi x1, x1, 0x000      
addi x2, x2, 0x400     
addi x3, x3, 0x000  
addi x4, x4, 0x000 
addi x5, x5, 0x0
addi x6, x6, 0x0
addi x7, x7, 0x0
addi x8, x8, 0x0
addi x0, x0, 0 
sw x4,  0x38(x2)
sw x3,  0x38(x1)
addi x0, x0, 0 
addi x0, x0, 0 
sw x5, 0x30(x2)
sw x5, 0x30(x1)
addi x0, x0, 0
addi x0, x0, 0
sw x6, 0x34(x2)
sw x6, 0x34(x1)
addi x0, x0, 0
addi x0, x0, 0
sw x8, 0x40(x2)  
sw x7, 0x40(x1) 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup  x1, 3
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x1, -0x10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
lui x5, 0x0
lui x6, 0xA8000
lui x7, 0x40000
lui x8, 0xB0001
addi x1, x1, 0x000      
addi x2, x2, 0x400     
addi x3, x3, 0x000  
addi x4, x4, 0x000 
addi x5, x5, 0x0
addi x6, x6, 0x0
addi x7, x7, 0x0
addi x8, x8, 0x0
addi x0, x0, 0 
sw x4,  0x8(x2)
sw x3,  0x8(x1)
addi x0, x0, 0 
addi x0, x0, 0
sw x5, 0x0(x2) 
sw x5, 0x0(x1)
addi x0, x0, 0 
addi x0, x0, 0 
sw x6, 0x4(x2)
sw x6, 0x4(x1)
addi x0, x0, 0 
addi x0, x0, 0 
sw x8, 0x10(x2)
sw x7, 0x10(x1) 
addi x0, x0, 0 
