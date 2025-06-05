; --- SEGMENT 1 ---
lui  x1, 0xC0001
lui  x2, 0xC0001
lui  x3, 0x00001
lui  x4, 0x00001
lui  x5, 0xA8000
lui  x6, 0xAC000
lui  x7, 0xA8000
lui  x8, 0xAC000
addi x1, x1, 0x800      
addi x2, x2, 0x840     
addi x3, x3, 0x008     
addi x4, x4, 0x000 
addi x5, x5, 0x000     
addi x6, x6, 0x000      
addi x7, x7, 0x180      
addi x8, x8, 0x180 
addi x0, x0, 0 
sw x3,  0x0(x2)
sw x3,  0x0(x1) 
addi x0, x0, 0 
addi x0, x0, 0 
sw x4, 0x4(x2)
sw x4, 0x4(x1)
addi x0, x0, 0
addi x0, x0, 0
sw x6, 0x8(x2)          
sw x5, 0x8(x1)   
addi x0, x0, 0 
addi x0, x0, 0  
sw x8, 0x10(x2)
sw x7, 0x10(x1) 
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
lp.setup  x3, 5
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
; --- SEGMENT 2 ---
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
lp.setup  x1,  0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x2,  10
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
; --- SEGMENT 4 ---
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
lp.setup  x1,  0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x2,  10
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
addi x8, x8, 0xFC0
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
; --- SEGMENT 6 ---
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
lp.setup  x1,  0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x2,  10
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
; --- SEGMENT 7 ---
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
; --- SEGMENT 8 ---
lui  x1, 0xC0001
lui  x2, 0xC0001
lui  x3, 0x00001
lui  x4, 0x00001
lui x5, 0x0
lui x6, 0xA8000
lui x7, 0x40000
lui x8, 0xB0001
addi x1, x1, 0x800      
addi x2, x2, 0x840     
addi x3, x3, 0x000  
addi x4, x4, 0x000 
addi x5, x5, 0x0
addi x6, x6, 0x0
addi x7, x7, 0x0
addi x8, x8, 0x0
lui  x9, 0xC0001
lui  x10, 0xC0001
lui  x11, 0x00001
lui  x12, 0x00001
lui x13, 0x0
lui x14, 0xA8000
lui x15, 0x40000
lui x16, 0xB0001
addi x9, x9, 0x0
addi x10, x10, 0x0
addi x11, x11, 0x800      
addi x12, x12, 0x840     
addi x13, x13, 0x000  
addi x14, x14, 0x000 
addi x15, x15, 0x0
addi x16, x16, 0x0
addi x0, x0, 0        
addi x0, x0, 0 
sw x2, 0x4(x1)    
addi x0, x0, 0  
addi x0, x0, 0        
addi x0, x0, 0 
sw x3, 0x0(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x4, 0x18(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x5, 0x20(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x6, 0x28(x1)    
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x1,  3
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x2,  30
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
; --- SEGMENT 9 ---
addi x0, x0, 0        
addi x0, x0, 0 
sw x2, 0x4(x1)    
addi x0, x0, 0  
addi x0, x0, 0        
addi x0, x0, 0 
sw x3, 0x0(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x7, 0x18(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x8, 0x20(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x9, 0x28(x1)    
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x1,  3
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
lp.setup  x2,  30
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
; --- SEGMENT 10 --- 
addi x0, x0, 0        
addi x0, x0, 0 
sw x2, 0x4(x1)    
addi x0, x0, 0  
addi x0, x0, 0        
addi x0, x0, 0 
sw x3, 0x0(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x10, 0x18(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x11, 0x20(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x12, 0x28(x1)    
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
; --- SEGMENT 11 --- 
addi x0, x0, 0        
addi x0, x0, 0 
sw x2, 0x4(x1)    
addi x0, x0, 0  
addi x0, x0, 0        
addi x0, x0, 0 
sw x3, 0x0(x1)    
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x13, 0x18(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x14, 0x20(x1)    
addi x0, x0, 0 
addi x0, x0, 0        
addi x0, x0, 0 
sw x15, 0x28(x1)    
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
lp.goto x3, -0x970
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 