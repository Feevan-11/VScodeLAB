# -*- coding: utf-8 -*-
"""
构建规则：
- 输入：./mif/{MAC_NAME}.mif   （每行 512 位二进制字符串）
- 输出：
  1) ./mif/{MAC_NAME}_headers_hex.txt  —— 组装之前输出所有帧头的16进制，每个word一行，帧与帧之间空行分隔
  2) ./mif/{MAC_NAME}_with_mac.mif     —— 新的MIF，每帧：1行帧头(512位) + N行数据(每行512位)
"""

import os
from typing import List, Tuple, Optional

# ===================== 基础工具函数 =====================

def ensure_binary_512(s: str) -> str:
    """检查并标准化一行512位的二进制字符串（仅允许0/1），返回去除空白后的字符串。"""
    s = s.strip()
    if len(s) != 512:
        raise ValueError(f"输入MIF存在非512位行：长度={len(s)} 内容(截断)={s[:64]}...")
    if any(c not in ("0", "1") for c in s):
        raise ValueError(f"输入MIF包含非二进制字符：{s[:64]}...")
    return s

def u32(x: int) -> int:
    """限制为32-bit无符号"""
    return x & 0xFFFFFFFF

# ===================== 题主给出的帧头生成函数 =====================

def make_mac_head(mac_flag: int, mac_da: int, stye: int, data_da: int, data_bbt: int) -> List[int]:
    """生成 16×32bit 的 MAC 头部（前 5 项有效，其余补 0）。"""
    words = [0] * 16
    words[0] = u32(mac_flag)
    words[1] = u32(mac_da)
    words[2] = u32(stye)
    words[3] = u32(0x88B5)
    words[4] = u32(data_da)
    words[5] = u32(data_bbt)
    return words

def header_words_to_bin_line(words: List[int]) -> str:
    """
    将16个32-bit word 组装为一行512位二进制字符串：
    规则：word15 在左，word0 在右（即 word15 是最高位段，word0 是最低位段）
    """
    if len(words) != 16:
        raise ValueError("头部words长度必须为16。")
    parts = []
    for i in range(15, -1, -1):
        parts.append(f"{u32(words[i]):032b}")
    return "".join(parts)

def header_words_to_hex_lines(words: List[int]) -> List[str]:
    """
    将前6个32-bit word 转为16进制字符串（8位大写，不带0x），每个word一行，从word0到word5。
    """
    return [f"{u32(w):08X}" for w in words[:6]]

# ===================== 新增：自动分段函数（带补全） =====================

def auto_segment_with_padding(total_lines: int, max_lines_per_frame: int) -> List[Tuple[int, int]]:
    """
    根据最大行数自动分段，返回每个分段的(有效行数, 补0行数)。
    
    参数:
        total_lines: MIF文件总行数
        max_lines_per_frame: 每帧最大数据行数
    
    返回:
        分段列表，每个元素为(有效行数, 补0行数)
        如100行，max=30，返回[(30,0), (30,0), (30,0), (10,20)]
    """
    if max_lines_per_frame <= 0:
        raise ValueError("最大行数必须大于0")
    
    if total_lines <= 0:
        return []
    
    segments = []
    remaining = total_lines
    
    while remaining > 0:
        if remaining >= max_lines_per_frame:
            segments.append((max_lines_per_frame, 0))  # 完整帧，不需要补0
            remaining -= max_lines_per_frame
        else:
            padding_lines = max_lines_per_frame - remaining
            segments.append((remaining, padding_lines))  # 不完整帧，需要补0
            remaining = 0
    
    return segments

# ===================== 主流程 =====================

def read_mif_lines(mif_path: str) -> List[str]:
    """读取MIF文件，返回每行的512位二进制字符串列表。"""
    if not os.path.isfile(mif_path):
        raise FileNotFoundError(f"未找到输入MIF文件：{mif_path}")
    lines = []
    with open(mif_path, "r", encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            lines.append(ensure_binary_512(raw))
    if not lines:
        raise ValueError("输入MIF为空。")
    return lines

def segment_indices_with_padding(total: int, seg_list: List[Tuple[int, int]]) -> List[Tuple[int, int, int]]:
    """
    根据分段列表生成 (start, end, padding_lines) 下标区间。
    返回: (有效数据起始下标, 有效数据结束下标, 补0行数)
    """
    res = []
    start = 0
    for valid_lines, padding_lines in seg_list:
        end = start + valid_lines
        if end > total:
            raise ValueError(f"分段索引超出范围：start={start}, end={end}, total={total}")
        res.append((start, end, padding_lines))
        start = end
    return res

def build_outputs(
    mif_lines: List[str],
    seg_list: List[Tuple[int, int]],  # 现在每个元素是(有效行数, 补0行数)
    flag: int,
    mac_da: int,
    stye: int,
    base_addr: int,
    data_bbt_fixed: int = None
):
    """
    核心：为每个分段生成帧头，并输出：
      - headers_hex_lines: List[str] （包含所有帧头的十六进制行，帧与帧之间用空行分隔）
      - new_mif_lines: List[str]     （包含帧头行+对应数据分段行+补0行）

    地址与数据量（字节数）关系：
      data_bytes = 有效行数 * 64  （补0行不计入数据量）
      第一帧 DATA_DA = base_addr
      第二帧 DATA_DA = base_addr + 第一帧 data_bytes
      ...
    data_bbt 默认使用 data_bytes；若传入 data_bbt_fixed 则使用固定值。
    """
    idx_ranges = segment_indices_with_padding(len(mif_lines), seg_list)

    headers_hex_lines: List[str] = []
    new_mif_lines: List[str] = []

    cur_addr = base_addr
    for fi, (s, e, padding_lines) in enumerate(idx_ranges):
        valid_lines = e - s  # 有效数据行数
        data_bytes = valid_lines * 64  # 每行64B，只计算有效数据
        data_da = cur_addr
        data_bbt = data_bbt_fixed if data_bbt_fixed is not None else data_bytes

        # 生成帧头 words
        words = make_mac_head(mac_flag=flag, mac_da=mac_da, stye=stye,
                              data_da=data_da, data_bbt=data_bbt)

        # 写入十六进制头（每个word一行）
        headers_hex_lines.extend(header_words_to_hex_lines(words))
        headers_hex_lines.append("")  # 帧与帧之间空行分隔

        # 组装成512位二进制帧头行，并写入到新MIF
        header_bin_line = header_words_to_bin_line(words)
        new_mif_lines.append(header_bin_line)

        # 写入该分段原始数据（有效数据）
        new_mif_lines.extend(mif_lines[s:e])
        
        # 补全全0行（如果需要）
        if padding_lines > 0:
            zero_line = "0" * 512
            for _ in range(padding_lines):
                new_mif_lines.append(zero_line)

        # 更新下一帧基地址：按"有效数据量"累加（补0行不增加地址）
        cur_addr += data_bytes

    # 去除最后一个空行（若存在）
    if headers_hex_lines and headers_hex_lines[-1] == "":
        headers_hex_lines.pop()

    return headers_hex_lines, new_mif_lines


def main_auto(
        flag=0xCCA41704,
        MAC_DA=0xAABBCCDD,
        STYE=0x00000001,
        MAC_NAME="MAC",
        MAX_LINES_PER_FRAME=30,
        BASE_ADDR=0x10000000
        ):
    
    MAC_NAME = MAC_NAME

    SEGMENTS = None
    MAX_LINES_PER_FRAME = MAX_LINES_PER_FRAME

    BASE_ADDR = BASE_ADDR

    flag = flag
    MAC_DA = MAC_DA
    STYE = STYE

    DATA_BBT_FIXED = None

    script_dir = os.path.dirname(os.path.abspath(__file__))
    MIF_DIR = os.path.join(script_dir, "mif")
    MIF_TEST_DIR = os.path.join(script_dir, "mif_test")
    TXT_DIR = os.path.join(script_dir, "txt")
    mif_file = os.path.join(MIF_DIR, f"{MAC_NAME}.mif")

    mif_lines = read_mif_lines(mif_file)
    total_lines = len(mif_lines)
    
    if SEGMENTS is None:
        if MAX_LINES_PER_FRAME is None:
            raise ValueError("必须指定SEGMENTS或MAX_LINES_PER_FRAME")
        segments_to_use = auto_segment_with_padding(total_lines, MAX_LINES_PER_FRAME)
        print(f"[INFO] 自动分段（带补全）：总行数{total_lines}，最大{MAX_LINES_PER_FRAME}行/帧 -> {segments_to_use}")
    else:
        # 如果手动指定SEGMENTS，需要转换为新的格式（假设不需要补0）
        segments_to_use = [(seg, 0) for seg in SEGMENTS]
        print(f"[INFO] 手动分段：{segments_to_use}")

    headers_hex_lines, new_mif_lines = build_outputs(
        mif_lines=mif_lines,
        seg_list=segments_to_use,
        flag=flag,
        mac_da=MAC_DA,
        stye=STYE,
        base_addr=BASE_ADDR,
        data_bbt_fixed=DATA_BBT_FIXED
    )

    headers_txt_path = os.path.join(TXT_DIR, f"headers.txt")
    with open(headers_txt_path, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("\n".join(headers_hex_lines))
        f.write("\n")

    # segments.txt 现在记录有效行数（用于DATA_BBT计算）
    segments_txt_path = os.path.join(TXT_DIR, f"segments.txt")
    with open(segments_txt_path, "a", encoding="utf-8") as f:
        lines = [f"{valid_lines} " for valid_lines, _ in segments_to_use]
        f.writelines(lines)
        f.write("\n")
    print(f"[OK] 头部16进制已写出：{headers_txt_path}")

    out_mif_path = os.path.join(MIF_TEST_DIR, f"{MAC_NAME}_with_headers.mif")
    with open(out_mif_path, "w", encoding="utf-8") as f:
        for line in new_mif_lines:
            f.write(line + "\n")
    print(f"[OK] 新MIF已写出：{out_mif_path}")
    
    # 统计信息
    total_frames = len(segments_to_use)
    total_valid_lines = sum(valid_lines for valid_lines, _ in segments_to_use)
    total_padding_lines = sum(padding_lines for _, padding_lines in segments_to_use)
    print(f"[INFO] 总帧数：{total_frames}")
    print(f"[INFO] 有效数据行：{total_valid_lines}，补0行：{total_padding_lines}")
    print(f"[INFO] 新MIF总行数：{len(new_mif_lines)}（{total_frames}帧头 + {total_valid_lines}有效数据 + {total_padding_lines}补0）")


# 示例使用
if __name__ == "__main__":
    # 示例1：MIF只有10行，MAX_LINES_PER_FRAME=100
    # 结果：1帧，帧头 + 10行有效数据 + 90行补0，DATA_BBT=10×64=640字节
    
    # 示例2：MIF有256行，MAX_LINES_PER_FRAME=100  
    # 结果：3帧，前2帧各100行有效数据，第3帧56行有效数据+44行补0
    # DATA_BBT：第1帧=6400，第2帧=6400，第3帧=56×64=3584
    
    main_auto(
        MAC_NAME="test",
        MAX_LINES_PER_FRAME=100,
        BASE_ADDR=0x10000000
    )