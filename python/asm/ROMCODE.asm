; --- SEGMENT 1 ---
lui  x1, 0xC0001
lui  x2, 0xC0001
lui  x3, 0x00001
lui  x4, 0x00001
lui  x5, 0x00000
lui  x6, 0xA8000
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
lui  x10, 0x00001
sw x3,  0x0(x2)
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0
addi x0, x0, 0        
addi x0, x0, 0
addi x9, x9, 0x1C0
addi x10, x10, 0x800
sw x4, 0x4(x2)
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
sw x7, 0x18(x2)
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x8, 0x20(x2)
addi x0, x0, 0 
addi x0, x0, 0   
addi x0, x0, 0        
sw x10, 0x28(x2)
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
sw x5, 0x18(x1)  
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
sw x6, 0x20(x1)
addi x0, x0, 0  
addi x0, x0, 0 
addi x0, x0, 0 
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
lui  x11, 0x00000
lui  x12, 0xAC000
lui  x13, 0x00000
lui  x14, 0x00000
lui  x15, 0xA0000
lui  x16, 0x00002
lui  x17, 0x00002
lui  x18, 0xA4000
addi x11, x11, 0x1C0      
addi x12, x12, 0x000     
addi x13, x13, 0x1C0  
addi x14, x14, 0x380
addi x15, x15, 0x000      
addi x16, x16, 0x000      
addi x17, x17, 0x380      
addi x18, x18, 0x000 
addi x0, x0, 0        
addi x0, x0, 0 
sw x3, 0x4(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x4, 0x0(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x11, 0x18(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x12, 0x20(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x13, 0x28(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
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
sw x3, 0x4(x1)    
addi x0, x0, 0  
addi x0, x0, 0        
addi x0, x0, 0 
sw x4, 0x0(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x14, 0x18(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x15, 0x20(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x16, 0x28(x1)    
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x1,  100
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x2,  1
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
sw x3, 0x4(x1)    
addi x0, x0, 0  
addi x0, x0, 0        
addi x0, x0, 0 
sw x4, 0x0(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x17, 0x18(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x18, 0x20(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x16, 0x28(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x1,  100
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x2,  1
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
lp.setup  x1, 50
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.goto x1, 0xC30
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0