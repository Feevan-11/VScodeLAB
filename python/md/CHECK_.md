| PC       | Slot3              | Slot2               | Slot1              | Slot0                |
|----------|--------------------|---------------------|--------------------|----------------------|
| `0x0000` | `lui x1, 0x40000`  | `lui x2, 0x0`       | `lui x3, 0x0`      | `lui x4, 0x0`        |
| `0x0010` | `lui x5, 0x0`      | `lui x6, 0x0`       | `lui x7, 0x0`      | `lui x8, 0x0`        |
| `0x0020` | `addi x1, x1, 0x0` | `addi x2, x2, 0x40` | `addi x3, x3, 0x1` | `addi x4, x4, 0x2`   |
| `0x0030` | `addi x5, x5, 0x0` | `addi x6, x6, 0x0`  | `addi x7, x7, 0x0` | `addi x8, x8, 0x0`   |
| `0x0040` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.setup x1, 0x10`  |
| `0x0050` | `lw x9, 0xD(x1)`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0060` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.setup x2, 0x10`  |
| `0x0070` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0080` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.goto x2, -0x10`  |
| `0x0090` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x00A0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `beq x9, x3, 0x110`  |
| `0x00B0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x00C0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x00D0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x00E0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x00F0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `beq x9, x4, 0x100`  |
| `0x0100` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0110` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0120` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0130` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0140` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `add x1, x1, x2`     |
| `0x0150` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0160` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.goto x1, -0x110` |
| `0x0170` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0180` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0190` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.goto x2, 0xA0`   |
| `0x01A0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x01B0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.setup x2, 100`   |
| `0x01C0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `add x5, x5, x3`   | `addi x0, x0, 0`     |
| `0x01D0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.goto x2, -0x110` |
| `0x01E0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x01F0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.setup x2, 100`   |
| `0x0200` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `add x6, x6, x4`   | `addi x0, x0, 0`     |
| `0x0210` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `lp.goto x2, -0x100` |
| `0x0220` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0230` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0240` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0250` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0260` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0270` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0280` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0290` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x02A0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x02B0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x02C0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x02D0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x02E0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x02F0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0300` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0310` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0320` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0330` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0340` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0350` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0360` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0370` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0380` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0390` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x03A0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x03B0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x03C0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x03D0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x03E0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x03F0` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0400` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0410` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0420` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |
| `0x0430` | `addi x0, x0, 0`   | `addi x0, x0, 0`    | `addi x0, x0, 0`   | `addi x0, x0, 0`     |