| PC       | Slot3                | Slot2                | Slot1                | Slot0                |
|----------|----------------------|----------------------|----------------------|----------------------|
| `0x0000` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.setup  x3, 100`  |
| `0x0010` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0020` | `lui x1, 0xFF005`    | `lui x2, 0xFF010`    | `lui x3, 0xFF020`    | `lui x4, 0xFF030`    |
| `0x0030` | `lui x5, 0xFF040`    | `lui x6, 0xF4000`    | `lui x7, 0x0`        | `lui x8, 0x40006`    |
| `0x0040` | `addi x1, x1, 0x0`   | `addi x2, x2, 0x101` | `addi x3, x3, 0x202` | `addi x4, x4, 0x303` |
| `0x0050` | `addi x5, x5, 0x404` | `addi x6, x6, 0x500` | `addi x7, x7, 0x100` | `addi x8, x8, 0xB00` |
| `0x0060` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0070` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x2,  0x0(x1)`    | `addi x0, x0, 0`     |
| `0x0080` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x3,  0x0(x1)`    | `addi x0, x0, 0`     |
| `0x0090` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x4, 0x0(x1)`     | `addi x0, x0, 0`     |
| `0x00A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `sw x5, 0x0(x1)`     | `addi x0, x0, 0`     |
| `0x00B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.setup  x1, 50`   |
| `0x00C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.setup  x2, 10`   |
| `0x00D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x00E0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.goto x2, -0x10`  |
| `0x00F0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0100` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.goto x1, -0x40`  |
| `0x0110` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0120` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `lp.goto x3, -0x110` |
| `0x0130` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0140` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0150` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0160` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0170` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0180` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x0190` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x01A0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x01B0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x01C0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |
| `0x01D0` | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     | `addi x0, x0, 0`     |