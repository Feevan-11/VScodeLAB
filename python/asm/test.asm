; --- SEGMENT 1 ---
lui x1, 0x0
lui x2, 0x0
lui x3, 0x0
lui x4, 0x0
lui x5, 0x1
lui x6, 0x1
lui x7, 0x0
lui x8, 0x0

addi x1, x1, 0x0
addi x2, x2, 0x0
addi x3, x3, 0x0
addi x4, x4, 0x40
addi x5, x5, 0x1
addi x6, x6, 0x0
addi x7, x7, 0x80
addi x8, x8, 0xC0

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0

addi x0, x0, 0 
sw x6, 0x34(x1)
sw x6, 0x34(x2)
addi x0, x0, 0

addi x0, x0, 0 
sw x3,  0x38(x1)
sw x3,  0x38(x2)
addi x0, x0, 0

addi x0, x0, 0
sw x5, 0x30(x1) 
sw x5, 0x30(x2) 
addi x0, x0, 0

addi x0, x0, 0 
sw x4, 0x40(x2)
sw x4, 0x40(x2)
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
lp.goto x1, -0x10

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
sw x6, 0x4(x1)
sw x6, 0x4(x1)
addi x0, x0, 0

addi x0, x0, 0 
sw x7,  0x8(x1)
sw x7,  0x8(x1)
addi x0, x0, 0

addi x0, x0, 0
sw x5, 0x0(x1) 
sw x5, 0x0(x1)
addi x0, x0, 0

addi x0, x0, 0
sw x8, 0x10(x2) 
sw x8, 0x10(x2) 
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

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0

