; --- SEGMENT 1 ---
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
addi x7, x7, 0x0
addi x8, x8, 0x0
addi x9, x9, 0x40
addi x10, x10, 0x40
addi x11, x11, 0x40
addi x12, x12, 0x40
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
lui x1, 0x0
lui x2, 0xFF003
lui x3, 0x1
lui x4, 0x1
lui x5, 0xF5400
lui x6, 0xF5400
lui x7, 0xF5600
lui x8, 0xF5600
addi x1, x1, 0x0
addi x2, x2, 0x400
addi x3, x3, 0x1
addi x4, x4, 0x0
addi x5, x5, 0x0
addi x6, x6, 0x0
addi x7, x7, 0x0
addi x8, x8, 0x40
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
;sw x4, 0x4(x2)
addi x0, x0, 0
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
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 
addi x0, x0, 0 

