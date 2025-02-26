lui  x1, 0xC0001
lui  x2, 0xC0001
lui  x3, 0x00001
lui  x4, 0x00001
lui  x5, 0x00000
lui  x6, 0xA0000
lui  x7, 0x40000
lui  x8, 0xB0001
addi x1, x1, 0x800      
addi x2, x2, 0x840     
addi x3, x3, 0x000  
addi x4, x4, 0x000 
addi x5, x5, 0x000      
addi x6, x6, 0x000      
addi x7, x7, 0x000      
addi x8, x8, 0x000 
lui  x9, 0x00000
sw x3,  0x0(x2)
sw x3,  0x0(x1)
lui  x10, 0x00001
addi x0, x0, 0 
sw x4, 0x4(x2)
sw x4, 0x4(x1)
addi x0, x0, 0
addi x9, x9, 0x200
sw x7, 0x18(x2)         
sw x5, 0x18(x1)  
addi x10, x10, 0x800
addi x0, x0, 0 
sw x8, 0x20(x2)
sw x6, 0x20(x1) 
addi x0, x0, 0   
addi x0, x0, 0        
sw x10, 0x28(x2)
sw x9, 0x28(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x1,  100
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
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup  x1, 10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x1, 0xF10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0