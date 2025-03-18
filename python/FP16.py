import numpy as np

# Convert the number  to FP16
fp16_number = np.float16(88.0)

# Gets the byte representation of FP16

fp16_bytes = fp16_number.byteswap().tobytes()  

# Convert bytes to binary strings
fp16_binary = ''.join(f'{byte:08b}' for byte in fp16_bytes)

# Convert bytes to hexadecimal
fp16_hex = fp16_bytes.hex()

print(f"FP16 Binary representation: {fp16_binary}")
print(f"FP16 Hexadecimal representation: 0x{fp16_hex.upper()}")