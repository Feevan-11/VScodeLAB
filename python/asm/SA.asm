; --- SEGMENT 1 ---
lui x1, 0xFF004
lui x2, 0xFF004
lui x3, 0x1
lui x4, 0x1
lui x5, 0xF4000
lui x6, 0xF4200
lui x7, 0xF4000
lui x8, 0xF4200
addi x1, x1, 0x400
addi x2, x2, 0x440
addi x3, x3, 0x8
addi x4, x4, 0x0
addi x5, x5, 0x0
addi x6, x6, 0x0
addi x7, x7, 0xC0
addi x8, x8, 0xC0
lui x29, 0x0
lui x30, 0xFF005
sw x3,  0x0(x2)
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x3,  0x0(x1) 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x4, 0x4(x2)
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x4, 0x4(x1)
addi x0, x0, 0
addi x29, x29, 0x0
addi x30, x30, 0x1
sw x6, 0x8(x2)
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0           
sw x5, 0x8(x1)   
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0  
sw x8, 0x10(x2)
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
sw x7, 0x10(x1) 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lp.setup  x1, 1000
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
; --- SEGMENT 2 ---
lui x1, 0xFF000
lui x2, 0xFF000
lui x3, 0xF4400
lui x4, 0xF4600
lui x5, 0x1
lui x6, 0x1
lui x7, 0xF4400
lui x8, 0xF4600
lui x9, 0xF4400
lui x10, 0xF4600
lui x11, 0xF4400
lui x12, 0xF4600
addi x1, x1, 0x0
addi x2, x2, 0x400
addi x3, x3, 0x0
addi x4, x4, 0x0
addi x5, x5, 0x1
addi x6, x6, 0x0
addi x7, x7, 0x3C0
addi x8, x8, 0x3C0
addi x9, x9, 0x400
addi x10, x10, 0x400
addi x11, x11, 0x7C0
addi x12, x12, 0x7C0
addi x0, x0, 0 
addi x0, x0, 0 
sw x29, 0x0(x30)
addi x0, x0, 0
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
lp.goto x1, -0x10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
lui x31, 0xFFF10
lui x30, 0xFFF10
lui x29, 0xFFF10
lui x28, 0xFFF10
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x31, x31, 0xFF0
addi x30, x30, 0xFF0
addi x29, x29, 0xFF0
addi x28, x28, 0xFF0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
