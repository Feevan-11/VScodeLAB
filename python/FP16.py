import numpy as np

number = 1.0

# FP16
fp16_val = np.array(number, dtype=np.float16).astype(np.dtype('>f2'))
fp16_bytes = fp16_val.tobytes()
fp16_bin = ''.join(f'{byte:08b}' for byte in fp16_bytes)
fp16_hex = fp16_bytes.hex()

# BF16
fp32_val = np.array(number, dtype=np.float32)
fp32_bytes = fp32_val.astype(np.dtype('>f4')).tobytes()
bf16_bytes = fp32_bytes[:2]  # First 2 bytes of the FP32 representation in big-endian
bf16_bin = ''.join(f'{byte:08b}' for byte in bf16_bytes)
bf16_hex = bf16_bytes.hex()

# FP32
fp32_val = np.array(number, dtype=np.float32).astype(np.dtype('>f4'))
fp32_bytes = fp32_val.tobytes()
fp32_bin = ''.join(f'{byte:08b}' for byte in fp32_bytes)
fp32_hex = fp32_bytes.hex()

# FP64
fp64_val = np.array(number, dtype=np.float64).astype(np.dtype('>f8'))
fp64_bytes = fp64_val.tobytes()
fp64_bin = ''.join(f'{byte:08b}' for byte in fp64_bytes)
fp64_hex = fp64_bytes.hex()

# Print results
print("FP16 Binary representation: " + fp16_bin)
print("FP16 Hexadecimal representation: 0x" + fp16_hex.upper())
print("BF16 Binary representation: " + bf16_bin)
print("BF16 Hexadecimal representation: 0x" + bf16_hex.upper())
print("FP32 Binary representation: " + fp32_bin)
print("FP32 Hexadecimal representation: 0x" + fp32_hex.upper())
print("FP64 Binary representation: " + fp64_bin)
print("FP64 Hexadecimal representation: 0x" + fp64_hex.upper())