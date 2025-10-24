; --- SEGMENT 1 ---
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x1, 0x10

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

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
addi x8, x8, 0xFC
addi x9, x9, 0x001
addi x10, x10, 0x000
addi x11, x11, 0xFC0
addi x12, x12, 0xFC

addi x0, x0, 0        
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
sw x8, 0x18(x2)  
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
sw x9, 0x20(x2)
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
sw x10, 0x28(x2)    
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
; --- SEGMENT 2 ---

lui  x1, 0xC0000
lui  x2, 0xC0000
lui  x3, 0xA0001
lui  x4, 0xA4001
lui  x5, 0x00401
lui  x6, 0x00001
lui  x7, 0xA0002
lui  x8, 0xA4002
lui  x15, 0x00401
lui  x16, 0x00001
lui  x17, 0xA0002
lui  x18, 0xA4002
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

addi x15, x15, 0x001     
addi x16, x16, 0x000      
addi x17, x17, 0xFC0      
addi x18, x18, 0xFC0

addi x0, x0, 0
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
sw x6, 0x40(x1)
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x2, 0x60

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

addi x0, x0, 0
addi x0, x0, 0 
sw x4, 0x34(x2)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x15,  0x38(x2)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x30(x2) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x16, 0x40(x2)
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup x2, 0x60

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
sw x4, 0x4(x1)
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x17,  0x8(x1)
addi x0, x0, 0 

addi x0, x0, 0
addi x0, x0, 0
sw x3, 0x0(x1) 
addi x0, x0, 0

addi x0, x0, 0
addi x0, x0, 0 
sw x18, 0x10(x1)
addi x0, x0, 0

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
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

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
lp.goto x1, -0x410

addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0


addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0
addi x0, x0, 0
