| PC       | Slot3              | Slot2              | Slot1               | Slot0               |
|----------|--------------------|--------------------|---------------------|---------------------|
| `0x0000` | `lui x1, 0x0`      | `lui x2, 0x0`      | `lui x3, 0x0`       | `lui x4, 0x0`       |
| `0x0010` | `lui x5, 0x1`      | `lui x6, 0x1`      | `lui x7, 0x0`       | `lui x8, 0x0`       |
| `0x0020` | `addi x1, x1, 0x0` | `addi x2, x2, 0x0` | `addi x3, x3, 0x0`  | `addi x4, x4, 0x40` |
| `0x0030` | `addi x5, x5, 0x1` | `addi x6, x6, 0x0` | `addi x7, x7, 0x80` | `addi x8, x8, 0xC0` |
| `0x0040` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x0050` | `addi x0, x0, 0`   | `sw x6, 0x34(x1)`  | `sw x6, 0x34(x2)`   | `addi x0, x0, 0`    |
| `0x0060` | `addi x0, x0, 0`   | `sw x3,  0x38(x1)` | `sw x3,  0x38(x2)`  | `addi x0, x0, 0`    |
| `0x0070` | `addi x0, x0, 0`   | `sw x5, 0x30(x1)`  | `sw x5, 0x30(x2)`   | `addi x0, x0, 0`    |
| `0x0080` | `addi x0, x0, 0`   | `sw x4, 0x40(x2)`  | `sw x4, 0x40(x2)`   | `addi x0, x0, 0`    |
| `0x0090` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `lp.setup  x1, 50`  |
| `0x00A0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x00B0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `lp.goto x1, -0x10` |
| `0x00C0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x00D0` | `addi x0, x0, 0`   | `sw x6, 0x4(x1)`   | `sw x6, 0x4(x1)`    | `addi x0, x0, 0`    |
| `0x00E0` | `addi x0, x0, 0`   | `sw x7,  0x8(x1)`  | `sw x7,  0x8(x1)`   | `addi x0, x0, 0`    |
| `0x00F0` | `addi x0, x0, 0`   | `sw x5, 0x0(x1)`   | `sw x5, 0x0(x1)`    | `addi x0, x0, 0`    |
| `0x0100` | `addi x0, x0, 0`   | `sw x8, 0x10(x2)`  | `sw x8, 0x10(x2)`   | `addi x0, x0, 0`    |
| `0x0110` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `lp.setup  x2, 100` |
| `0x0120` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x0130` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `lp.goto x1, -0x10` |
| `0x0140` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x0150` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x0160` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x0170` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x0180` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x0190` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x01A0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x01B0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x01C0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x01D0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x01E0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x01F0` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |
| `0x0200` | `addi x0, x0, 0`   | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`    |