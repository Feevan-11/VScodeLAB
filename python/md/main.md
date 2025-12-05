| PC       | Slot3                  | Slot2                  | Slot1                 | Slot0                  |
|----------|------------------------|------------------------|-----------------------|------------------------|
| `0x0000` | `lui x1, 0xFF004`      | `lui x2, 0xFF004`      | `lui x3, 0x1`         | `lui x4, 0x1`          |
| `0x0010` | `lui x5, 0xF4000`      | `lui x6, 0xF5A00`      | `lui x7, 0x0`         | `lui x8, 0xF4000`      |
| `0x0020` | `lui x9, 0xF4200`      | `lui x10, 0xFF004`     | `lui x11, 0xF5A00`    | `lui x12, 0xF5A00`     |
| `0x0030` | `addi x1, x1, 0x400`   | `addi x2, x2, 0x440`   | `addi x3, x3, 0x1`    | `addi x4, x4, 0x0`     |
| `0x0040` | `addi x5, x5, 0x0`     | `addi x6, x6, 0x0`     | `addi x7, x7, 0x240`  | `addi x8, x8, 0x240`   |
| `0x0050` | `addi x9, x9, 0x0`     | `addi x10, x10, 0xC00` | `addi x11, x11, 0x0`  | `addi x12, x12, 0x200` |
| `0x0060` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4,  0x0(x1)`     | `addi x0, x0, 0`       |
| `0x0070` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`      | `addi x0, x0, 0`       |
| `0x0080` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x5, 0x18(x1)`     | `addi x0, x0, 0`       |
| `0x0090` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x20(x1)`     | `addi x0, x0, 0`       |
| `0x00A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x7, 0x28(x1)`     | `addi x0, x0, 0`       |
| `0x00B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4,  0x0(x2)`     | `addi x0, x0, 0`       |
| `0x00C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x2)`      | `addi x0, x0, 0`       |
| `0x00D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x8, 0x18(x2)`     | `addi x0, x0, 0`       |
| `0x00E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x9, 0x20(x2)`     | `addi x0, x0, 0`       |
| `0x00F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x7, 0x28(x2)`     | `addi x0, x0, 0`       |
| `0x0100` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x100`   |
| `0x0110` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0120` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0130` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0140` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x0, 0x30(x10)`    | `addi x0, x0, 0`       |
| `0x0150` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x34(x10)`    | `addi x0, x0, 0`       |
| `0x0160` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x11,  0x38(x10)`  | `addi x0, x0, 0`       |
| `0x0170` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x3, 0x30(x10)`    | `addi x0, x0, 0`       |
| `0x0180` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x12, 0x40(x10)`   | `addi x0, x0, 0`       |
| `0x0190` | `addi x0, x0, 0`       | `addi x10, x10, 0xff`  | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x01A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x01B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x01C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x01D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x01E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x01F0` | `lui x11, 0x0`         | `lui x12, 0x0`         | `lui x13, 0x0`        | `lui x14, 0x0`         |
| `0x0200` | `lui x15, 0x0`         | `lui x16, 0x0`         | `lui x17, 0x0`        | `lui x18, 0xCCA41`     |
| `0x0210` | `lui x19, 0x0`         | `lui x20, 0x40000`     | `lui x21, 0x40000`    | `lui x22, 0x0`         |
| `0x0220` | `lui x23, 0x40003`     | `lui x24, 0x0`         | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0230` | `addi x11, x11, 0x0`   | `addi x12, x12, 0x0`   | `addi x13, x13, 0xFF` | `addi x14, x14, 0xF4`  |
| `0x0240` | `addi x15, x15, 0xF0`  | `addi x16, x16, 0xF1`  | `addi x17, x17, 0xF2` | `addi x18, x18, 0x704` |
| `0x0250` | `addi x19, x19, 0x0`   | `addi x20, x20, 0x0`   | `addi x21, x21, 0x40` | `addi x22, x22, 0x500` |
| `0x0260` | `addi x23, x23, 0x800` | `addi x24, x24, 0x0`   | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0270` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0280` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x1, 0x20`    |
| `0x0290` | `lw x19, 0x0(x23)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x02A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x02B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x02C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x02D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x02E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x02F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x19, x18, 0x60`   |
| `0x0300` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0310` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0320` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0330` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0340` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x1, -0xC0`    |
| `0x0350` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0360` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x1, 0x10`    |
| `0x0370` | `lw x12, 0x4(x20)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0380` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x0390` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x03A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x03B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x03C0` | `lw x11 0x4(x20)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x03D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x03E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x03F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0400` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0410` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x14, x11, 0x340`  |
| `0x0420` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0430` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0440` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0450` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0460` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x15, x11, 0x4B0`  |
| `0x0470` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0480` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0490` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x04A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x04B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x16, x11, 0x620`  |
| `0x04C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x04D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x04E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x04F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0500` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x17, x11, 0x790`  |
| `0x0510` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0520` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0530` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0540` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0550` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x13, x11, 0x900`  |
| `0x0560` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0570` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0580` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0590` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x05A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x05B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x05C0` | `addi x0, x0, 0`       | `addi x24, x24, 0x40`  | `add x21, x21, x22`   | `add x20, x20, x22`    |
| `0x05D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x05E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x1, -0x280`   |
| `0x05F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0600` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x23, x20 0x80`    |
| `0x0610` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0620` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0630` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0640` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0650` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x3, 0x10`    |
| `0x0660` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0670` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x3, -0xD0`    |
| `0x0680` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0690` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x3, 0x10`    |
| `0x06A0` | `sw x0, 0x0(x23)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x06B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x06C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x06D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x06E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x06F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x3, -0x6F0`   |
| `0x0700` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0710` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x0720` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0730` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0740` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0750` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0760` | `lui x5, 0xF4200`      | `lui x6, 0xF5C00`      | `lui x7, 0x0`         | `lui x8, 0x0`          |
| `0x0770` | `lui x1, 0xFF004`      | `lui x2, 0xFF004`      | `lui x3, 0x1`         | `lui x4, 0x1`          |
| `0x0780` | `addi x5, x5, 0x0`     | `addi x6, x6, 0x0`     | `addi x7, x7, 0x40`   | `addi x8, x8, 0x0`     |
| `0x0790` | `addi x1, x1, 0x400`   | `addi x2, x2, 0x0`     | `addi x3, x3, 0x1`    | `addi x4, x4, 0x0`     |
| `0x07A0` | `add x5, x24, x5`      | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x07B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x07C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4,  0x0(x1)`     | `addi x0, x0, 0`       |
| `0x07D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`      | `addi x0, x0, 0`       |
| `0x07E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x5, 0x18(x1)`     | `addi x0, x0, 0`       |
| `0x07F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x20(x1)`     | `addi x0, x0, 0`       |
| `0x0800` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x7, 0x28(x1)`     | `addi x0, x0, 0`       |
| `0x0810` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 200`     |
| `0x0820` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0830` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0840` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0850` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x0, 0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0860` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x2)`      | `addi x0, x0, 0`       |
| `0x0870` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6,  0x8(x2)`     | `addi x0, x0, 0`       |
| `0x0880` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x3, 0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0890` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x10(x2)`     | `addi x0, x0, 0`       |
| `0x08A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x100`   |
| `0x08B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x08C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x08D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x08E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x08F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0900` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x310`   |
| `0x0910` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0920` | `lui x5, 0xF4200`      | `lui x6, 0xF5400`      | `lui x7, 0x0`         | `lui x8, 0x0`          |
| `0x0930` | `lui x1, 0xFF004`      | `lui x2, 0xFF003`      | `lui x3, 0x1`         | `lui x4, 0x1`          |
| `0x0940` | `addi x5, x5, 0x0`     | `addi x6, x6, 0x0`     | `addi x7, x7, 0x40`   | `addi x8, x8, 0x0`     |
| `0x0950` | `addi x1, x1, 0x400`   | `addi x2, x2, 0x0`     | `addi x3, x3, 0x1`    | `addi x4, x4, 0x0`     |
| `0x0960` | `add x5, x24, x5`      | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0970` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0980` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4,  0x0(x1)`     | `addi x0, x0, 0`       |
| `0x0990` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`      | `addi x0, x0, 0`       |
| `0x09A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x5, 0x18(x1)`     | `addi x0, x0, 0`       |
| `0x09B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x20(x1)`     | `addi x0, x0, 0`       |
| `0x09C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x7, 0x28(x1)`     | `addi x0, x0, 0`       |
| `0x09D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 200`     |
| `0x09E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x09F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0A00` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0A10` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x0, 0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0A20` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x2)`      | `addi x0, x0, 0`       |
| `0x0A30` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6,  0x8(x2)`     | `addi x0, x0, 0`       |
| `0x0A40` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x3, 0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0A50` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x10(x2)`     | `addi x0, x0, 0`       |
| `0x0A60` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x100`   |
| `0x0A70` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0A80` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0A90` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0AA0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x0AB0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0AC0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x4D0`   |
| `0x0AD0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0AE0` | `lui x5, 0xF4200`      | `lui x6, 0xF5600`      | `lui x7, 0x0`         | `lui x8, 0x0`          |
| `0x0AF0` | `lui x1, 0xFF004`      | `lui x2, 0xFF003`      | `lui x3, 0x1`         | `lui x4, 0x1`          |
| `0x0B00` | `addi x5, x5, 0x0`     | `addi x6, x6, 0x0`     | `addi x7, x7, 0x40`   | `addi x8, x8, 0x0`     |
| `0x0B10` | `addi x1, x1, 0x400`   | `addi x2, x2, 0x400`   | `addi x3, x3, 0x1`    | `addi x4, x4, 0x0`     |
| `0x0B20` | `add x5, x24, x5`      | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0B30` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0B40` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4,  0x0(x1)`     | `addi x0, x0, 0`       |
| `0x0B50` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`      | `addi x0, x0, 0`       |
| `0x0B60` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x5, 0x18(x1)`     | `addi x0, x0, 0`       |
| `0x0B70` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x20(x1)`     | `addi x0, x0, 0`       |
| `0x0B80` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x7, 0x28(x1)`     | `addi x0, x0, 0`       |
| `0x0B90` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 200`     |
| `0x0BA0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0BB0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0BC0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0BD0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x0, 0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0BE0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x2)`      | `addi x0, x0, 0`       |
| `0x0BF0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6,  0x8(x2)`     | `addi x0, x0, 0`       |
| `0x0C00` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x3, 0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0C10` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x10(x2)`     | `addi x0, x0, 0`       |
| `0x0C20` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x100`   |
| `0x0C30` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0C40` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0C50` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0C60` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x0C70` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0C80` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x690`   |
| `0x0C90` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0CA0` | `lui x5, 0xF4200`      | `lui x6, 0xF5800`      | `lui x7, 0x0`         | `lui x8, 0x0`          |
| `0x0CB0` | `lui x1, 0xFF004`      | `lui x2, 0xFF004`      | `lui x3, 0x1`         | `lui x4, 0x1`          |
| `0x0CC0` | `addi x5, x5, 0x0`     | `addi x6, x6, 0x0`     | `addi x7, x7, 0x40`   | `addi x8, x8, 0x0`     |
| `0x0CD0` | `addi x1, x1, 0x400`   | `addi x2, x2, 0x800`   | `addi x3, x3, 0x1`    | `addi x4, x4, 0x0`     |
| `0x0CE0` | `add x5, x24, x5`      | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0CF0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0D00` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4,  0x0(x1)`     | `addi x0, x0, 0`       |
| `0x0D10` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`      | `addi x0, x0, 0`       |
| `0x0D20` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x5, 0x18(x1)`     | `addi x0, x0, 0`       |
| `0x0D30` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x20(x1)`     | `addi x0, x0, 0`       |
| `0x0D40` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x7, 0x28(x1)`     | `addi x0, x0, 0`       |
| `0x0D50` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 200`     |
| `0x0D60` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0D70` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0D80` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0D90` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x0, 0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0DA0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x2)`      | `addi x0, x0, 0`       |
| `0x0DB0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6,  0x8(x2)`     | `addi x0, x0, 0`       |
| `0x0DC0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x3, 0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0DD0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x10(x2)`     | `addi x0, x0, 0`       |
| `0x0DE0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x100`   |
| `0x0DF0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0E00` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0E10` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0E20` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x0E30` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0E40` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x850`   |
| `0x0E50` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0E60` | `lui x1, 0x0`          | `lui x2, 0x0`          | `lui x3, 0x0`         | `lui x4, 0x0`          |
| `0x0E70` | `addi x0, x0, 0x0`     | `addi x0, x0, 0x0`     | `addi x0, x0, 0x0`    | `addi x0, x0, 0x0`     |
| `0x0E80` | `addi x1, x1, 0x1`     | `addi x2, x2, 0x2`     | `addi x3, x3, 0x3`    | `addi x4, x4, 0x4`     |
| `0x0E90` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0EA0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0EB0` | `lw x5, 0x8(x20)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0EC0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x0ED0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0EE0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x0EF0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0F00` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x1, x5, 0x160`    |
| `0x0F10` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0F20` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0F30` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0F40` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0F50` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x2, x5, 0x330`    |
| `0x0F60` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0F70` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0F80` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0F90` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0FA0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `beq x3, x5, 0x400`    |
| `0x0FB0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0FC0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0FD0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0FE0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x0FF0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x1000` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1010` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0xA20`   |
| `0x1020` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1030` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1040` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1050` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1060` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1070` | `lui x1, 0xFF004`      | `lui x2, 0x0`          | `lui x3, 0x1`         | `lui x4, 0x1`          |
| `0x1080` | `lui x5, 0x0`          | `lui x6, 0x0`          | `lui x7, 0x0`         | `lui x8, 0x0`          |
| `0x1090` | `addi x1, x1, 0x400`   | `addi x2, x2, 0x0`     | `addi x3, x3, 0x0`    | `addi x4, x4, 0x0`     |
| `0x10A0` | `addi x5, x5, 0x0`     | `addi x6, x6, 0x0`     | `addi x7, x7, 0x0`    | `addi x8, x8, 0x0`     |
| `0x10B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x10C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x10D0` | `lw x6, 0x10(x20)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x10E0` | `lw x7, 0x14(x20)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x10F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x1100` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1110` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x10`    |
| `0x1120` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1130` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1140` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x3,  0x0(x1)`     | `addi x0, x0, 0`       |
| `0x1150` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`      | `addi x0, x0, 0`       |
| `0x1160` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x21, 0x18(x1)`    | `addi x0, x0, 0`       |
| `0x1170` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x6, 0x20(x1)`     | `addi x0, x0, 0`       |
| `0x1180` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `sw x7, 0x28(x1)`     | `addi x0, x0, 0`       |
| `0x1190` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x11A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x1`     |
| `0x11B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x3, 0x5`     |
| `0x11C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x11D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x3, -0x10`    |
| `0x11E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x11F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x40`    |
| `0x1200` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1210` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1220` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1230` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x1240` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1250` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x290`   |
| `0x1260` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1270` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1280` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1290` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x12A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x12B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x12C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, 0x240`    |
| `0x12D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x12E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x12F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1300` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1310` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1320` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1330` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1340` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1350` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1360` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1370` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1380` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1390` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x13A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x13B0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x13C0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x13D0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x13E0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x13F0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1400` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1410` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.setup x2, 0x10`    |
| `0x1420` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1430` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `lp.goto x2, -0x470`   |
| `0x1440` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1450` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1460` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1470` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1480` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x1490` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |
| `0x14A0` | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`      | `addi x0, x0, 0`       |