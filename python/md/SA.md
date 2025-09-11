| PC       | Slot3                | Slot2                  | Slot1                  | Slot0                  |
|----------|----------------------|------------------------|------------------------|------------------------|
| `0x0000` | `lui x1, 0xFF004`    | `lui x2, 0xFF004`      | `lui x3, 0x1`          | `lui x4, 0x1`          |
| `0x0010` | `lui x5, 0xF4000`    | `lui x6, 0xF4200`      | `lui x7, 0xF4000`      | `lui x8, 0xF4200`      |
| `0x0020` | `addi x1, x1, 0x400` | `addi x2, x2, 0x440`   | `addi x3, x3, 0x8`     | `addi x4, x4, 0x0`     |
| `0x0030` | `addi x5, x5, 0x0`   | `addi x6, x6, 0x0`     | `addi x7, x7, 0xC0`    | `addi x8, x8, 0xC0`    |
| `0x0040` | `lui x29, 0x0`       | `lui x30, 0xFF005`     | `sw x3,  0x0(x2)`      | `addi x0, x0, 0`       |
| `0x0050` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x3,  0x0(x1)`      | `addi x0, x0, 0`       |
| `0x0060` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x4, 0x4(x2)`       | `addi x0, x0, 0`       |
| `0x0070` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x4, 0x4(x1)`       | `addi x0, x0, 0`       |
| `0x0080` | `addi x29, x29, 0x0` | `addi x30, x30, 0x1`   | `sw x6, 0x8(x2)`       | `addi x0, x0, 0`       |
| `0x0090` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x5, 0x8(x1)`       | `addi x0, x0, 0`       |
| `0x00A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x8, 0x10(x2)`      | `addi x0, x0, 0`       |
| `0x00B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x7, 0x10(x1)`      | `addi x0, x0, 0`       |
| `0x00C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.setup x1, 0xBB8`   |
| `0x00D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x00E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.goto x1, -0x10`    |
| `0x00F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0100` | `lui x1, 0xFF002`    | `lui x2, 0xFF002`      | `lui x3, 0xF6400`      | `lui x4, 0xF6800`      |
| `0x0110` | `lui x5, 0x1`        | `lui x6, 0x1`          | `lui x7, 0xF6400`      | `lui x8, 0xF6800`      |
| `0x0120` | `lui x9, 0xF6400`    | `lui x10, 0xF6800`     | `lui x11, 0xF6400`     | `lui x12, 0xF6800`     |
| `0x0130` | `addi x1, x1, 0x0`   | `addi x2, x2, 0x400`   | `addi x3, x3, 0x0`     | `addi x4, x4, 0x0`     |
| `0x0140` | `addi x5, x5, 0x1`   | `addi x6, x6, 0x0`     | `addi x7, x7, 0x3C0`   | `addi x8, x8, 0x3C0`   |
| `0x0150` | `addi x9, x9, 0x400` | `addi x10, x10, 0x400` | `addi x11, x11, 0x7C0` | `addi x12, x12, 0x7C0` |
| `0x0160` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `sw x29, 0x0(x30)`     | `addi x0, x0, 0`       |
| `0x0170` | `addi x0, x0, 0`     | `sw x6, 0x34(x2)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0180` | `addi x0, x0, 0`     | `sw x4,  0x38(x2)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0190` | `addi x0, x0, 0`     | `sw x5, 0x30(x2)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x01A0` | `addi x0, x0, 0`     | `sw x8, 0x40(x2)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x01B0` | `addi x0, x0, 0`     | `sw x6, 0x34(x1)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x01C0` | `addi x0, x0, 0`     | `sw x3,  0x38(x1)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x01D0` | `addi x0, x0, 0`     | `sw x5, 0x30(x1)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x01E0` | `addi x0, x0, 0`     | `sw x7, 0x40(x1)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x01F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.setup x1, 0x64`    |
| `0x0200` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0210` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.goto x1, -0x10`    |
| `0x0220` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0230` | `addi x0, x0, 0`     | `sw x6, 0x4(x1)`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0240` | `addi x0, x0, 0`     | `sw x9,  0x8(x1)`      | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0250` | `addi x0, x0, 0`     | `sw x5, 0x0(x1)`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0260` | `addi x0, x0, 0`     | `sw x11, 0x10(x1)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0270` | `addi x0, x0, 0`     | `sw x6, 0x4(x2)`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0280` | `addi x0, x0, 0`     | `sw x10,  0x8(x2)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x0290` | `addi x0, x0, 0`     | `sw x5, 0x0(x2)`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x02A0` | `addi x0, x0, 0`     | `sw x12, 0x10(x2)`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x02B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.setup  x2, 100`    |
| `0x02C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `addi x0, x0, 0`       |
| `0x02D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`       | `addi x0, x0, 0`       | `lp.goto x1, -0x10`    |
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