from Crypto.Util.number import *
from random import getrandbits
from flag import flag


def ROL(bits, N):
    for _ in range(N):
        bits = ((bits << 1) & (2**length - 1)) | (bits >> (length - 1))
    return bits


flag = bytes_to_long(flag)
#flagを2進数にした時のbit長
length = flag.bit_length()

key = getrandbits(length)
cipher = flag ^ key

for i in range(32):
    key = ROL(key, pow(cipher, 3, length))
    cipher ^= key

print("key =", key)
print("cipher =", cipher)
