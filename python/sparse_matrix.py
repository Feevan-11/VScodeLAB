#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
将稀疏矩阵 A、B 压缩为数据包并输出为 512bit 对齐的二进制 txt 文件。

主要功能：
1. 根据给定尺寸和稀疏度，生成随机稀疏矩阵 A(M×K)、B(K×N)，数据类型为 fp16。
2. 按 16×4096 / 4096×16 规则对 A、B 分块，并按照给定的格式压缩：
   - 包头（512bit，对齐，右对齐）
   - Row Data（64Byte = 512bit）
   - Column Mask（每个 16bit，数量 = total_cols + 1）
   - Non-zero Values（每个 16bit，按行/列优先顺序）
3. 每个数据包末尾补 0 到 512bit 整数倍。
4. 输出：
   - A_packets.txt：矩阵 A 所有数据包拼接后的 512bit 行
   - B_packets.txt：矩阵 B 所有数据包拼接后的 512bit 行
   - packet_stats.txt：
       第一行：矩阵 A 每两个数据包占用的 512bit 行数（空格分隔）
       第二行：矩阵 B 每两个数据包占用的 512bit 行数（空格分隔）
"""

import numpy as np
from typing import List, Tuple



def int_to_bits_le(value: int, bit_width: int) -> List[int]:
    """
    将整数编码为小端 bit 序列（LSB-first），长度固定为 bit_width。
    比如 value = 5 (0b0101), bit_width = 4 -> [1,0,1,0]
    """
    bits = [(value >> i) & 1 for i in range(bit_width)]
    return bits


def float16_to_bits_le(value: np.float16) -> List[int]:
    """
    将 fp16（numpy.float16）转换为 16bit 小端 bit 序列。
    """
    # view 为 uint16 以便取原始二进制
    u16 = value.view(np.uint16).item()
    return int_to_bits_le(u16, 16)


def bits_to_512bit_lines(bits_le: List[int]) -> List[str]:
    """
    将整体 bit 流（LSB-first）切分为 512bit 一行的字符串列表。
    输出字符串为 MSB 在左，LSB 在右（即对每个 512bit 块 reversed）。
    """
    lines = []
    n = len(bits_le)
    for i in range(0, n, 512):
        block = bits_le[i:i + 512]
        if len(block) < 512:
            block = block + [0] * (512 - len(block))  # 末尾补 0
        # 打印时左边是高位，右边是低位：需要将 LSB-first 的列表反转
        line_bits = ''.join(str(b) for b in reversed(block))
        lines.append(line_bits)
    return lines


# =========================
# 包头、行信息打包
# =========================

def pack_header_bits(
    data_type: int,
    r_last: int,
    c_last: int,
    total_cols_encoded: int,
    nnz_count: int
) -> List[int]:
    """
    打包包头字段为 bit（小端），并在高位补 0 到 512bit。

    字段布局（共 32bit）：
    [0:1]   data_type (2bit)      这里只用 00 表示 fp16
    [2]     RLast (1bit)
    [3]     CLast (1bit)
    [4:15]  total_cols (12bit)    0 -> 1, 0xFFF -> 4096
    [16:31] nnz_count (16bit)     当前包中的非零数量（若超过 0xFFFF 则裁剪）
    """
    bits = []
    bits.extend(int_to_bits_le(data_type, 2))
    bits.extend(int_to_bits_le(r_last, 1))
    bits.extend(int_to_bits_le(c_last, 1))
    bits.extend(int_to_bits_le(total_cols_encoded, 12))
    bits.extend(int_to_bits_le(nnz_count, 16))

    assert len(bits) == 32

    # 包头补 0 至 512bit。注意我们是小端存储：
    # bits[0:32] 是低位，补在后面的是高位，在输出时会位于 512bit 行的左边。
    padding = [0] * (512 - 32)
    bits.extend(padding)
    return bits


def pack_row_data_for_A(
    row_start: int,
    num_rows_block: int,
    row_nnz_list: List[int],
    total_rows_A: int
) -> List[int]:
    """
    A 矩阵的 Row Data 打包，总长度固定 64Byte = 512bit。

    对块内最多 16 行，每行：
      row_idx(2B) + nnz_per_row(2B)，均为小端字节序。
    若当前块行数 < 16，多余 slot 填 0。
    行号使用 0-based（0~65535），假设总行数 < 65536。
    """
    bits = []
    for slot in range(16):
        if slot < num_rows_block:
            global_row_idx = row_start + slot  # 0-based
            nnz_per_row = row_nnz_list[slot]
        else:
            global_row_idx = 0
            nnz_per_row = 0

        # row_idx: 16bit 小端
        bits.extend(int_to_bits_le(global_row_idx, 16))
        # nnz_per_row: 16bit 小端
        bits.extend(int_to_bits_le(nnz_per_row, 16))

    assert len(bits) == 16 * 32  # 16 行 * 4B * 8bit = 512bit
    return bits


def pack_row_data_for_B(
    col_start: int,
    num_cols_block: int,
    col_nnz_list: List[int],
    total_cols_B: int
) -> List[int]:
    """
    B 矩阵的 Row Data 打包，总长度固定 64Byte = 512bit。

    此时“行信息”中的 row_idx 实际表示 B 的列号：
      row_idx(2B) = 原始 B 的列索引（0-based）
      nnz_per_row(2B) = 当前块内该列的非零数量
    若当前块列数 < 16，多余 slot 填 0。
    """
    bits = []
    for slot in range(16):
        if slot < num_cols_block:
            global_col_idx = col_start + slot  # 0-based
            nnz_per_col = col_nnz_list[slot]
        else:
            global_col_idx = 0
            nnz_per_col = 0

        bits.extend(int_to_bits_le(global_col_idx, 16))
        bits.extend(int_to_bits_le(nnz_per_col, 16))

    assert len(bits) == 16 * 32
    return bits


# =========================
# 单个数据包打包：A
# =========================

def build_packet_bits_A(
    A: np.ndarray,
    row_start: int,
    row_end: int,
    col_start: int,
    col_end: int,
    total_rows_A: int,
    total_cols_A: int,
    is_last_packet: bool
) -> List[int]:
    """
    构造矩阵 A 的一个数据包的 bit 流（LSB-first），并补齐到 512bit 的整数倍。

    分块尺寸：最多 16 行 × 4096 列
    对应字段含义：
      - total_cols: 当前块的列数（K 方向），编码为 cols-1
      - RLast: 若这是 A 的最后一个数据包则置 1
      - CLast: 若该包包含 A 的最后一列（col_end == total_cols_A）则置 1
    """
    block = A[row_start:row_end, col_start:col_end]  # shape: (num_rows_block, num_cols_block)
    num_rows_block, num_cols_block = block.shape

    # 行非零统计
    row_nnz = np.count_nonzero(block, axis=1).astype(int).tolist()
    # 总非零数
    nnz_total = int(np.count_nonzero(block))
    nnz_clipped = min(nnz_total, 0xFFFF)  # 超过 16bit 的部分这里简单裁剪（极端全 1 才会超）

    # 列掩码：对当前块中每一列产生 16bit 掩码，bit r 表示块内第 r 行是否非零
    col_masks: List[int] = []
    for c in range(num_cols_block):
        col_vec = block[:, c]
        mask = 0
        for r in range(num_rows_block):
            if col_vec[r] != 0:
                mask |= (1 << r)  # row r -> bit r
        col_masks.append(mask)

    # total_cols 字段编码：0->1, 0xFFF->4096
    total_cols_encoded = num_cols_block - 1  # num_cols_block 至多 4096

    # RLast / CLast 约定：
    # - RLast: 若这是整个 A 的最后一个数据包则置 1
    # - CLast: 若该包包含 A 的最后一列（col_end == total_cols_A）则置 1
    r_last = 1 if is_last_packet else 0
    c_last = 1 if col_end == total_cols_A else 0

    # 打包包头
    data_type = 0  # 00b -> fp16
    header_bits = pack_header_bits(
        data_type=data_type,
        r_last=r_last,
        c_last=c_last,
        total_cols_encoded=total_cols_encoded,
        nnz_count=nnz_clipped
    )

    # 打包行信息（Row Data）
    row_data_bits = pack_row_data_for_A(
        row_start=row_start,
        num_rows_block=num_rows_block,
        row_nnz_list=row_nnz,
        total_rows_A=total_rows_A
    )

    # 打包列掩码（Column Mask），共 num_cols_block 个，每个 16bit
    col_mask_bits: List[int] = []
    for mask in col_masks:
        col_mask_bits.extend(int_to_bits_le(mask, 16))

    # 打包非零值序列（Non-Zero Values），A 按行优先
    value_bits: List[int] = []
    for r in range(num_rows_block):
        for c in range(num_cols_block):
            v = block[r, c]
            if v != 0:
                value_bits.extend(float16_to_bits_le(np.float16(v)))

    # 拼接整个包的 bit 流
    packet_bits = header_bits + row_data_bits + col_mask_bits + value_bits

    # 包尾补 0 到 512bit 整数倍（高位补 0，即在 bit 序列末尾补）
    remainder = len(packet_bits) % 512
    if remainder != 0:
        pad_len = 512 - remainder
        packet_bits.extend([0] * pad_len)

    return packet_bits


# =========================
# 单个数据包打包：B
# =========================

def build_packet_bits_B(
    B: np.ndarray,
    row_start: int,
    row_end: int,
    col_start: int,
    col_end: int,
    total_rows_B: int,
    total_cols_B: int,
    is_last_packet: bool
) -> List[int]:
    """
    构造矩阵 B 的一个数据包的 bit 流（LSB-first），并补齐到 512bit 的整数倍。

    分块尺寸：最多 4096 行 × 16 列
    对应字段含义：
      - total_cols: 当前块的行数（K 方向），编码为 rows-1
      - Row Data 中的 row_idx 表示 B 的列索引（0-based）
      - RLast: 若这是 B 的最后一个数据包则置 1
      - CLast: 若该包包含 B 的最后一行（row_end == total_rows_B）则置 1
    """
    block = B[row_start:row_end, col_start:col_end]  # shape: (num_rows_block, num_cols_block)
    num_rows_block, num_cols_block = block.shape

    # 每列非零统计（Row Data 使用“列信息”）
    col_nnz = np.count_nonzero(block, axis=0).astype(int).tolist()

    # 总非零数
    nnz_total = int(np.count_nonzero(block))
    nnz_clipped = min(nnz_total, 0xFFFF)

    # 行掩码：对当前块中每一行产生 16bit 掩码，bit c 表示块内第 c 列是否非零
    row_masks: List[int] = []
    for r in range(num_rows_block):
        row_vec = block[r, :]
        mask = 0
        for c in range(num_cols_block):
            if row_vec[c] != 0:
                mask |= (1 << c)  # col c -> bit c
        row_masks.append(mask)

    # total_cols 字段编码：对 B 是“行数-1”
    total_cols_encoded = num_rows_block - 1

    # RLast / CLast 约定：
    # - RLast: 若这是整个 B 的最后一个数据包则置 1
    # - CLast: 若该包包含 B 的最后一行（row_end == total_rows_B）则置 1
    r_last = 1 if is_last_packet else 0
    c_last = 1 if row_end == total_rows_B else 0

    data_type = 0  # 00b -> fp16
    header_bits = pack_header_bits(
        data_type=data_type,
        r_last=r_last,
        c_last=c_last,
        total_cols_encoded=total_cols_encoded,
        nnz_count=nnz_clipped
    )

    # Row Data：此时 row_idx 对应 B 的列索引
    row_data_bits = pack_row_data_for_B(
        col_start=col_start,
        num_cols_block=num_cols_block,
        col_nnz_list=col_nnz,
        total_cols_B=total_cols_B
    )

    # Column Mask：每一行一个 mask（对 B 来说是“行掩码”）
    col_mask_bits: List[int] = []
    for mask in row_masks:
        col_mask_bits.extend(int_to_bits_le(mask, 16))

    # 非零值序列：B 按列优先
    value_bits: List[int] = []
    for c in range(num_cols_block):
        for r in range(num_rows_block):
            v = block[r, c]
            if v != 0:
                value_bits.extend(float16_to_bits_le(np.float16(v)))

    packet_bits = header_bits + row_data_bits + col_mask_bits + value_bits

    remainder = len(packet_bits) % 512
    if remainder != 0:
        pad_len = 512 - remainder
        packet_bits.extend([0] * pad_len)

    return packet_bits


# =========================
# 矩阵整体压缩：A、B
# =========================

def compress_matrix_A_to_packets(A: np.ndarray) -> List[List[int]]:
    """
    将矩阵 A(M×K) 按 16 行 × 最多 4096 列 分块，压缩为多个数据包。
    返回：每个数据包对应一个 bit 列表（LSB-first）。
    """
    M, K = A.shape
    row_block_size = 16
    col_block_size = 4096

    packets: List[List[int]] = []

    # 预判总共有多少个包，用于判断“最后一个包”
    row_blocks = (M + row_block_size - 1) // row_block_size
    col_blocks = (K + col_block_size - 1) // col_block_size
    total_packets = row_blocks * col_blocks

    packet_index = 0

    for row_start in range(0, M, row_block_size):
        row_end = min(row_start + row_block_size, M)
        for col_start in range(0, K, col_block_size):
            col_end = min(col_start + col_block_size, K)
            packet_index += 1
            is_last = (packet_index == total_packets)
            packet_bits = build_packet_bits_A(
                A=A,
                row_start=row_start,
                row_end=row_end,
                col_start=col_start,
                col_end=col_end,
                total_rows_A=M,
                total_cols_A=K,
                is_last_packet=is_last
            )
            packets.append(packet_bits)

    return packets


def compress_matrix_B_to_packets(B: np.ndarray) -> List[List[int]]:
    """
    将矩阵 B(K×N) 按 最多 4096 行 × 16 列 分块，压缩为多个数据包。
    返回：每个数据包对应一个 bit 列表（LSB-first）。
    """
    K, N = B.shape
    row_block_size = 4096
    col_block_size = 16

    packets: List[List[int]] = []

    row_blocks = (K + row_block_size - 1) // row_block_size
    col_blocks = (N + col_block_size - 1) // col_block_size
    total_packets = row_blocks * col_blocks

    packet_index = 0

    for col_start in range(0, N, col_block_size):
        col_end = min(col_start + col_block_size, N)
        for row_start in range(0, K, row_block_size):
            row_end = min(row_start + row_block_size, K)
            packet_index += 1
            is_last = (packet_index == total_packets)
            packet_bits = build_packet_bits_B(
                B=B,
                row_start=row_start,
                row_end=row_end,
                col_start=col_start,
                col_end=col_end,
                total_rows_B=K,
                total_cols_B=N,
                is_last_packet=is_last
            )
            packets.append(packet_bits)

    return packets


# =========================
# 稀疏矩阵生成
# =========================

def generate_random_sparse_matrix(
    rows: int,
    cols: int,
    density: float,
    low: float = -1.0,
    high: float = 1.0,
    seed: int = 0
) -> np.ndarray:
    """
    生成随机稀疏矩阵（fp16）。

    density: 非零比例 (0~1)
    low, high: 非零元素的均匀分布范围
    """
    assert 0.0 <= density <= 1.0
    rng = np.random.default_rng(seed)

    mat = np.zeros((rows, cols), dtype=np.float16)

    # 为每个位置生成一个 [0,1) 的随机数，小于 density 的位置设为非零
    mask = rng.random((rows, cols)) < density
    num_nnz = int(mask.sum())
    if num_nnz > 0:
        values = rng.uniform(low, high, size=num_nnz).astype(np.float16)
        mat[mask] = values

    return mat


# =========================
# 文件输出 & 统计
# =========================

def write_packets_file(packets: List[List[int]], filename: str) -> List[int]:
    """
    将若干数据包（bit 流，LSB-first）拼接，并写入 txt 文件，每行 512bit。
    返回：每个数据包各自占用的 512bit 行数列表。
    """
    # 统计每个包占多少行（因为之前已补齐）
    lines_per_packet = [len(p) // 512 for p in packets]

    # 全部拼接成一个大 bit 流
    all_bits: List[int] = []
    for packet_bits in packets:
        all_bits.extend(packet_bits)

    lines = bits_to_512bit_lines(all_bits)

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

    return lines_per_packet


def compute_lines_per_two_packets(lines_per_packet: List[int]) -> List[int]:
    """
    根据“每个数据包占多少个 512bit 行”，计算“每两个数据包占多少个 512bit 行”。
    若数量为奇数，最后一个单独作为一组。
    """
    result: List[int] = []
    n = len(lines_per_packet)
    i = 0
    while i < n:
        if i + 1 < n:
            result.append(lines_per_packet[i] + lines_per_packet[i + 1])
            i += 2
        else:
            result.append(lines_per_packet[i])
            i += 1
    return result


def write_packet_stats_file(
    A_lines_per_packet: List[int],
    B_lines_per_packet: List[int],
    filename: str = "packet_stats.txt"
):
    """
    输出统计文件：
    第一行：矩阵 A 的每两个数据包占多少个 512bit 行（空格分隔）
    第二行：矩阵 B 的每两个数据包占多少个 512bit 行（空格分隔）
    """
    A_pairs = compute_lines_per_two_packets(A_lines_per_packet)
    B_pairs = compute_lines_per_two_packets(B_lines_per_packet)

    with open(filename, 'w') as f:
        f.write(' '.join(str(x) for x in A_pairs) + '\n')
        f.write(' '.join(str(x) for x in B_pairs) + '\n')


# =========================
# 示例主函数
# =========================

def main(matrix_size,sparsity):
    # ======= 可根据需要修改的参数 =======
    # 矩阵尺寸
    M = matrix_size   # A 的行数
    K = matrix_size   # A 的列数 / B 的行数
    N = matrix_size   # B 的列数

    # 稀疏度（非零比例）
    density_A = 1-sparsity
    density_B = 1-sparsity

    # 随机种子
    seed_A = 1
    seed_B = 2
    # =================================

    print(f"Generating random sparse matrices A({M}x{K}), B({K}x{N}) ...")
    A = generate_random_sparse_matrix(M, K, density_A, seed=seed_A)
    B = generate_random_sparse_matrix(K, N, density_B, seed=seed_B)

    print("Compressing matrix A into packets ...")
    A_packets = compress_matrix_A_to_packets(A)

    print("Compressing matrix B into packets ...")
    B_packets = compress_matrix_B_to_packets(B)

    print("Writing A_packets.txt ...")
    A_lines_per_packet = write_packets_file(A_packets, ".\sparse\matrix_a_packets.mif")

    print("Writing B_packets.txt ...")
    B_lines_per_packet = write_packets_file(B_packets, ".\sparse\matrix_b_packets.mif")

    print("Writing packet_stats.txt ...")
    write_packet_stats_file(A_lines_per_packet, B_lines_per_packet, ".\sparse\packet_stats.txt")

    print("Done.")
    print(f"Matrix A: {len(A_packets)} packets")
    print(f"Matrix B: {len(B_packets)} packets")


if __name__ == "__main__":
    main(matrix_size = 32,sparsity=0.9)
