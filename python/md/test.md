| PC       | Slot3                 | Slot2                 | Slot1                 | Slot0                 |
|----------|-----------------------|-----------------------|-----------------------|-----------------------|
| `0x0000` | `lui x1, 0xFF006`     | `lui x2, 0x0`         | `lui x3, 0x0`         | `lui x4, 0x0`         |
| `0x0010` | `lui x5, 0x0`         | `lui x6, 0x0`         | `lui x7, 0x0`         | `lui x8, 0x0`         |
| `0x0020` | `lui x9, 0x0`         | `lui x10, 0x0`        | `lui x11, 0x0`        | `lui x12, 0x0`        |
| `0x0030` | `lui x13, 0x0`        | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0040` | `addi x1, x1, 0x0`    | `addi x2, x2, 0x74`   | `addi x3, x3, 0x65`   | `addi x4, x4, 0x73`   |
| `0x0050` | `addi x5, x5, 0x74`   | `addi x6, x6, 0x20`   | `addi x7, x7, 0x73`   | `addi x8, x8, 0x75`   |
| `0x0060` | `addi x9, x9, 0x63`   | `addi x10, x10, 0x63` | `addi x11, x11, 0x65` | `addi x12, x12, 0x65` |
| `0x0070` | `addi x13, x13, 0x64` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0080` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `sw x3,  0x0(x1)`     | `addi x0, x0, 0`      |
| `0x0090` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `sw x4, 0x4(x1)`      | `addi x0, x0, 0`      |
| `0x00A0` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `sw x5, 0x18(x1)`     | `addi x0, x0, 0`      |
| `0x00B0` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `sw x6, 0x20(x1)`     | `addi x0, x0, 0`      |
| `0x00C0` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `sw x7, 0x28(x1)`     | `addi x0, x0, 0`      |
| `0x00D0` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x00E0` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `lp.setup  x2,  100`  |
| `0x00F0` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0100` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `lp.goto x2, -0x10`   |
| `0x0110` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0120` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0130` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0140` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0150` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0160` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |
| `0x0170` | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      | `addi x0, x0, 0`      |