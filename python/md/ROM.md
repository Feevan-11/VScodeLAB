| PC       | Slot3                | Slot2                  | Slot1                  | Slot0                  |
|----------|----------------------|------------------------|------------------------|------------------------|
| `0x0000` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.setup  x1,  200`   |
| `0x0010` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0020` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.setup  x2,  100`   |
| `0x0030` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0040` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.goto x2, -0x10`    |
| `0x0050` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0060` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0070` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.goto x1, -0x50`    |
| `0x0080` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0090` | `lui x1, 0xFF004`    | `lui x2, 0xFF004`      | `lui x3, 0x1`          | `lui x4, 0x1`          |
| `0x00A0` | `lui x5, 0xF4000`    | `lui x6, 0x40000`      | `lui x7, 0xF4000`      | `lui x8, 0x80000`      |
| `0x00B0` | `addi x1, x1, 0x400` | `addi x2, x2, 0x440`   | `addi x3, x3, 0x0`     | `addi x4, x4, 0x0`     |
| `0x00C0` | `addi x5, x5, 0x0`   | `addi x6, x6, 0x0`     | `addi x7, x7, 0x200`   | `addi x8, x8, 0xE00`   |
| `0x00D0` | `lui x9, 0x0`        | `lui x10, 0x0`         | `sw x3,  0x0(x2)`      | `addi x0, x0, 0`       |
| `0x00E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x00F0` | `addi x9, x9, 0x200` | `addi x10, x10, 0x200` | `sw x4, 0x4(x2)`       | `addi x0, x0, 0`       |
| `0x0100` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x7, 0x18(x2)`      | `addi x0, x0, 0`       |
| `0x0110` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x8, 0x20(x2)`      | `addi x0, x0, 0`       |
| `0x0120` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x10, 0x28(x2)`     | `addi x0, x0, 0`       |
| `0x0130` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x3,  0x0(x1)`      | `addi x0, x0, 0`       |
| `0x0140` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`       | `addi x0, x0, 0`       |
| `0x0150` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x5, 0x18(x1)`      | `addi x0, x0, 0`       |
| `0x0160` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x6, 0x20(x1)`      | `addi x0, x0, 0`       |
| `0x0170` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x9, 0x28(x1)`      | `addi x0, x0, 0`       |
| `0x0180` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.setup  x1,  100`   |
| `0x0190` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x01A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.goto x1, -0x10`    |
| `0x01B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x01C0` | `lui x11, 0x40000`   | `lui x12, 0xF4001`     | `lui x13, 0x0`         | `lui x14, 0x80000`     |
| `0x01D0` | `lui x15, 0xF4400`   | `lui x16, 0x2`         | `lui x17, 0xF4001`     | `lui x18, 0x0`         |
| `0x01E0` | `addi x11, x11, 0x0` | `addi x12, x12, 0x0`   | `addi x13, x13, 0x200` | `addi x14, x14, 0xE00` |
| `0x01F0` | `addi x15, x15, 0x0` | `addi x16, x16, 0x0`   | `addi x17, x17, 0x200` | `addi x18, x18, 0x200` |
| `0x0200` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0210` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x3,  0x0(x1)`      | `addi x0, x0, 0`       |
| `0x0220` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`       | `addi x0, x0, 0`       |
| `0x0230` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x11, 0x18(x1)`     | `addi x0, x0, 0`       |
| `0x0240` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x12, 0x20(x1)`     | `addi x0, x0, 0`       |
| `0x0250` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x13, 0x28(x1)`     | `addi x0, x0, 0`       |
| `0x0260` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0270` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x3,  0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0280` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0290` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x4, 0x4(x2)`       | `addi x0, x0, 0`       |
| `0x02A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x14, 0x18(x2)`     | `addi x0, x0, 0`       |
| `0x02B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x17, 0x20(x2)`     | `addi x0, x0, 0`       |
| `0x02C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x18, 0x28(x2)`     | `addi x0, x0, 0`       |
| `0x02D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x02E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x02F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0300` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0310` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0320` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0330` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0340` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0350` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0360` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0370` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0380` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0390` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x03A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x03B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x03C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x03D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x03E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x03F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0400` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0410` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0420` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0430` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0440` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0450` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0460` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0470` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0480` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0490` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x04A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x04B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x04C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x04D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x04E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x04F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0500` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0510` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0520` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0530` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |