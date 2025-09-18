| PC       | Slot3                | Slot2                | Slot1                | Slot0                |
|----------|----------------------|----------------------|----------------------|----------------------|
| `0x0000` | `lui x1, 0xFF004`    | `lui x2, 0xFF004`    | `lui x3, 0x1`        | `lui x4, 0x1`        |
| `0x0010` | `lui x5, 0xF4000`    | `lui x6, 0xF4200`    | `lui x7, 0xF4000`    | `lui x8, 0xF4200`    |
| `0x0020` | `addi x1, x1, 0x400` | `addi x2, x2, 0x440` | `addi x3, x3, 0x8`   | `addi x4, x4, 0x0`   |
| `0x0030` | `addi x5, x5, 0x0`   | `addi x6, x6, 0x0`   | `addi x7, x7, 0x0`   | `addi x8, x8, 0x0`   |
| `0x0040` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x3,  0x0(x2)`    | `addi x0, x0, 0`     |
| `0x0050` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x3,  0x0(x1)`    | `addi x0, x0, 0`     |
| `0x0060` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x4, 0x4(x2)`     | `addi x0, x0, 0`     |
| `0x0070` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x4, 0x4(x1)`     | `addi x0, x0, 0`     |
| `0x0080` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x6, 0x8(x2)`     | `addi x0, x0, 0`     |
| `0x0090` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x5, 0x8(x1)`     | `addi x0, x0, 0`     |
| `0x00A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x8, 0x10(x2)`    | `addi x0, x0, 0`     |
| `0x00B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x7, 0x10(x1)`    | `addi x0, x0, 0`     |
| `0x00C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.setup  x1, 100`  |
| `0x00D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x00E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.goto x1, -0x10`  |
| `0x00F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0100` | `lui x1, 0xFF003`    | `lui x2, 0xFF003`    | `lui x3, 0xF7400`    | `lui x4, 0xF7600`    |
| `0x0110` | `lui x5, 0x11`       | `lui x6, 0x1`        | `lui x7, 0xF7400`    | `lui x8, 0xF7600`    |
| `0x0120` | `lui x11, 0xF7400`   | `lui x12, 0xF7600`   | `lui x13, 0xF7400`   | `lui x14, 0xF7600`   |
| `0x0130` | `addi x1, x1, 0x0`   | `addi x2, x2, 0x400` | `addi x3, x3, 0x40`  | `addi x4, x4, 0x40`  |
| `0x0140` | `addi x5, x5, 0x1`   | `addi x6, x6, 0x0`   | `addi x7, x7, 0x40`  | `addi x8, x8, 0x40`  |
| `0x0150` | `addi x11, x11, 0x0` | `addi x12, x12, 0x0` | `addi x13, x13, 0x0` | `addi x14, x14, 0x0` |
| `0x0160` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x6, 0x4(x2)`     | `addi x0, x0, 0`     |
| `0x0170` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x4,  0x8(x2)`    | `addi x0, x0, 0`     |
| `0x0180` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x5, 0x0(x2)`     | `addi x0, x0, 0`     |
| `0x0190` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x8, 0x10(x2)`    | `addi x0, x0, 0`     |
| `0x01A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x6, 0x4(x1)`     | `addi x0, x0, 0`     |
| `0x01B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x3,  0x8(x1)`    | `addi x0, x0, 0`     |
| `0x01C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x5, 0x0(x1)`     | `addi x0, x0, 0`     |
| `0x01D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x7, 0x10(x1)`    | `addi x0, x0, 0`     |
| `0x01E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.setup  x1, 100`  |
| `0x01F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0200` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.goto x1, -0x10`  |
| `0x0210` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0220` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x6, 0x34(x2)`    | `addi x0, x0, 0`     |
| `0x0230` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x12,  0x38(x2)`  | `addi x0, x0, 0`     |
| `0x0240` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x5, 0x30(x2)`    | `addi x0, x0, 0`     |
| `0x0250` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x14, 0x40(x2)`   | `addi x0, x0, 0`     |
| `0x0260` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x6, 0x34(x1)`    | `addi x0, x0, 0`     |
| `0x0270` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x11,  0x38(x1)`  | `addi x0, x0, 0`     |
| `0x0280` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x5, 0x30(x1)`    | `addi x0, x0, 0`     |
| `0x0290` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x13, 0x40(x1)`   | `addi x0, x0, 0`     |
| `0x02A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x02B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x02C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x02D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x02E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x02F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0300` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0310` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0320` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0330` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0340` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0350` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0360` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0370` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0380` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0390` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x03A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x03B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x03C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x03D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x03E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x03F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0400` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0410` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0420` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0430` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0440` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0450` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0460` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0470` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0480` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0490` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x04A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x04B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x04C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x04D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x04E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x04F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0500` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0510` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0520` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0530` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0540` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0550` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0560` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0570` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0580` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0590` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x05A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x05B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x05C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x05D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x05E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x05F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0600` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0610` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0620` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0630` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0640` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0650` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0660` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0670` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0680` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0690` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x06A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x06B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x06C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x06D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x06E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x06F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0700` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0710` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0720` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0730` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0740` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0750` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0760` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0770` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0780` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0790` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x07A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x07B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x07C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x07D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x07E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x07F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0800` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0810` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0820` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0830` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0840` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0850` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0860` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0870` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0880` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0890` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |