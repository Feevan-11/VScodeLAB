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

def make_mac_head(mac_da: int, mac_sa: int, stye: int, data_da: int, data_bbt: int) -> List[int]:
    """生成 16×32bit 的 MAC 头部（前 5 项有效，其余补 0）。"""
    words = [0] * 16
    words[0] = u32(mac_da)
    words[1] = u32(mac_sa)
    words[2] = u32(stye)
    words[3] = u32(data_da)
    words[4] = u32(data_bbt)
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

# ===================== 新增：自动分段函数 =====================

def auto_segment(total_lines: int, max_lines_per_frame: int) -> List[int]:
    """
    根据最大行数自动分段。
    
    参数:
        total_lines: MIF文件总行数
        max_lines_per_frame: 每帧最大数据行数
    
    返回:
        分段列表，如100行，max=30，返回[30, 30, 30, 10]
    """
    if max_lines_per_frame <= 0:
        raise ValueError("最大行数必须大于0")
    
    if total_lines <= 0:
        return []
    
    segments = []
    remaining = total_lines
    
    while remaining > 0:
        if remaining >= max_lines_per_frame:
            segments.append(max_lines_per_frame)
            remaining -= max_lines_per_frame
        else:
            segments.append(remaining)
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

def segment_indices(total: int, seg_list: List[int]) -> List[Tuple[int, int]]:
    """
    根据分段列表生成 (start, end) 下标区间（左闭右开），用于切片。
    要求：sum(seg_list) == total
    """
    if sum(seg_list) != total:
        raise ValueError(f"分段列表之和({sum(seg_list)})不等于输入MIF总行数({total})。")
    res = []
    start = 0
    for n in seg_list:
        end = start + n
        res.append((start, end))
        start = end
    return res

def build_outputs(
    mif_lines: List[str],
    seg_list: List[int],
    mac_da: int,
    mac_sa: int,
    stye: int,
    base_addr: int,
    data_bbt_fixed: int = None
):
    """
    核心：为每个分段生成帧头，并输出：
      - headers_hex_lines: List[str] （包含所有帧头的十六进制行，帧与帧之间用空行分隔）
      - new_mif_lines: List[str]     （包含帧头行+对应数据分段行）

    地址与数据量（字节数）关系：
      data_bytes = 段内行数 * 64
      第一帧 DATA_DA = base_addr
      第二帧 DATA_DA = base_addr + 第一帧 data_bytes
      ...
    data_bbt 默认使用 data_bytes；若传入 data_bbt_fixed 则使用固定值。
    """
    idx_ranges = segment_indices(len(mif_lines), seg_list)

    headers_hex_lines: List[str] = []
    new_mif_lines: List[str] = []

    cur_addr = base_addr
    for fi, (s, e) in enumerate(idx_ranges):
        lines_in_frame = e - s
        data_bytes = lines_in_frame * 64  # 每行64B
        data_da = cur_addr
        data_bbt = data_bbt_fixed if data_bbt_fixed is not None else data_bytes

        # 生成帧头 words
        words = make_mac_head(mac_da=mac_da, mac_sa=mac_sa, stye=stye,
                              data_da=data_da, data_bbt=data_bbt)

        # 写入十六进制头（每个word一行）
        headers_hex_lines.extend(header_words_to_hex_lines(words))
        headers_hex_lines.append("")  # 帧与帧之间空行分隔

        # 组装成512位二进制帧头行，并写入到新MIF
        header_bin_line = header_words_to_bin_line(words)
        new_mif_lines.append(header_bin_line)

        # 写入该分段原始数据
        new_mif_lines.extend(mif_lines[s:e])

        # 更新下一帧基地址：按"实际数据量"累加
        cur_addr += data_bytes

    # 去除最后一个空行（若存在）
    if headers_hex_lines and headers_hex_lines[-1] == "":
        headers_hex_lines.pop()

    return headers_hex_lines, new_mif_lines

def main():
    # ===================== 参数集中配置区域 =====================
    # MIF 名称（输入文件：./mif/{MAC_NAME}.mif）
    MAC_NAME = "MAC"

    # 分段方式选择（二选一）：
    # 方式1：手动指定分段列表
    SEGMENTS = [10, 10, 20, 20, 20, 20]  # 手动分段
    
    # 方式2：自动分段（设置最大行数，SEGMENTS设为None）
    #SEGMENTS = None
    MAX_LINES_PER_FRAME = 30  # 每帧最大数据行数，当SEGMENTS为None时生效

    BASE_ADDR = 0x10000000

    MAC_DA = 0x11223344   
    MAC_SA = 0xAABBCCDD   
    STYE   = 0x00000001   

    DATA_BBT_FIXED = None

    script_dir = os.path.dirname(os.path.abspath(__file__))
    MIF_DIR = os.path.join(script_dir, "mif")
    TXT_DIR = os.path.join(script_dir, "txt")
    mif_file = os.path.join(MIF_DIR, f"{MAC_NAME}.mif")

    mif_lines = read_mif_lines(mif_file)
    total_lines = len(mif_lines)
    
    # 分段逻辑：优先使用自动分段
    if SEGMENTS is None:
        if MAX_LINES_PER_FRAME is None:
            raise ValueError("必须指定SEGMENTS或MAX_LINES_PER_FRAME")
        segments_to_use = auto_segment(total_lines, MAX_LINES_PER_FRAME)
        print(f"[INFO] 自动分段：总行数{total_lines}，最大{MAX_LINES_PER_FRAME}行/帧 -> {segments_to_use}")
    else:
        segments_to_use = SEGMENTS
        print(f"[INFO] 手动分段：{segments_to_use}")

    headers_hex_lines, new_mif_lines = build_outputs(
        mif_lines=mif_lines,
        seg_list=segments_to_use,
        mac_da=MAC_DA,
        mac_sa=MAC_SA,
        stye=STYE,
        base_addr=BASE_ADDR,
        data_bbt_fixed=DATA_BBT_FIXED,
        BASE_ADDR = 0x10000000
    )

    headers_txt_path = os.path.join(TXT_DIR, f"{MAC_NAME}_headers_hex.txt")
    with open(headers_txt_path, "w", encoding="utf-8") as f:
        f.write("\n")
        f.write("\n".join(headers_hex_lines))
        f.write("\n")
    print(f"[OK] 头部16进制已写出：{headers_txt_path}")

    out_mif_path = os.path.join(MIF_DIR, f"{MAC_NAME}_with_headers.mif")
    with open(out_mif_path, "w", encoding="utf-8") as f:
        for line in new_mif_lines:
            f.write(line + "\n")
    print(f"[OK] 新MIF已写出：{out_mif_path}")
    print(f"[INFO] 总帧数：{len(segments_to_use)}，总行数：{len(new_mif_lines)}")

def main_auto(
        MAC_DA = 0x11223344,
        MAC_SA = 0xAABBCCDD,
        STYE   = 0x00000001,
        MAC_NAME = "MAC",
        MAX_LINES_PER_FRAME = 30,
        BASE_ADDR = 0x10000000
        ):
    
    MAC_NAME = MAC_NAME

    
    SEGMENTS = None
    MAX_LINES_PER_FRAME = MAX_LINES_PER_FRAME  

    BASE_ADDR = BASE_ADDR

    MAC_DA = MAC_DA   
    MAC_SA = MAC_SA   
    STYE   = STYE   

    DATA_BBT_FIXED = None

    script_dir = os.path.dirname(os.path.abspath(__file__))
    MIF_DIR = os.path.join(script_dir, "mif")
    TXT_DIR = os.path.join(script_dir, "txt")
    mif_file = os.path.join(MIF_DIR, f"{MAC_NAME}.mif")

    mif_lines = read_mif_lines(mif_file)
    total_lines = len(mif_lines)
    
    if SEGMENTS is None:
        if MAX_LINES_PER_FRAME is None:
            raise ValueError("必须指定SEGMENTS或MAX_LINES_PER_FRAME")
        segments_to_use = auto_segment(total_lines, MAX_LINES_PER_FRAME)
        print(f"[INFO] 自动分段：总行数{total_lines}，最大{MAX_LINES_PER_FRAME}行/帧 -> {segments_to_use}")
    else:
        segments_to_use = SEGMENTS
        print(f"[INFO] 手动分段：{segments_to_use}")

    headers_hex_lines, new_mif_lines = build_outputs(
        mif_lines=mif_lines,
        seg_list=segments_to_use,
        mac_da=MAC_DA,
        mac_sa=MAC_SA,
        stye=STYE,
        base_addr=BASE_ADDR,
        data_bbt_fixed=DATA_BBT_FIXED
    )

    headers_txt_path = os.path.join(TXT_DIR, f"headers.txt")
    with open(headers_txt_path, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("\n".join(headers_hex_lines))
        f.write("\n")

    segments_txt_path = os.path.join(TXT_DIR, f"segments.txt")
    with open(segments_txt_path, "a", encoding="utf-8") as f:
        lines = [str(segment + 1) + " " for segment in segments_to_use]
        f.writelines(lines)
        f.write("\n")
    print(f"[OK] 头部16进制已写出：{headers_txt_path}")

    out_mif_path = os.path.join(MIF_DIR, f"{MAC_NAME}_with_headers.mif")
    with open(out_mif_path, "w", encoding="utf-8") as f:
        for line in new_mif_lines:
            f.write(line + "\n")
    print(f"[OK] 新MIF已写出：{out_mif_path}")
    print(f"[INFO] 总帧数：{len(segments_to_use)}，总行数：{len(new_mif_lines)}")


if __name__ == "__main__":
    main()