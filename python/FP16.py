import numpy as np

# 将数字 1 转换为 FP16
fp16_number = np.float16(128.0)

# 获取 FP16 的字节表示

fp16_bytes = fp16_number.byteswap().tobytes()  # 确保大端序排列

# 将字节转换为二进制字符串
fp16_binary = ''.join(f'{byte:08b}' for byte in fp16_bytes)

# 将字节转换为十六进制
fp16_hex = fp16_bytes.hex()

print(f"FP16 二进制表示: {fp16_binary}")
print(f"FP16 十六进制表示: 0x{fp16_hex.upper()}")