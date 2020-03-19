from pwn import *
import random
from binascii import hexlify, unhexlify

BLOCK_SIZE = 128
BLOCK_SIZE_BYTES_HEX = BLOCK_SIZE//4

def remote_encrypt(m):
    m = hex(m)[2:].rjust(BLOCK_SIZE_BYTES_HEX, '0').encode()
    r.readuntil("stuff: ")
    r.sendline(m)
    r.readuntil("you go: 0x")
    c = r.readuntil("\n")[:-1].rjust(BLOCK_SIZE_BYTES_HEX, b'0')
    return int(c, 16)

# 00000000000000000000000000000000
r = remote("35.228.52.143", 7777)
#r = process("./chall.py")

r.readuntil("Flag: ")
cflag = r.readuntil("\n")[:-1]
print(cflag)

base_m1 = random.randint(0, (1 << BLOCK_SIZE) - 1)
base_m2 = random.randint(0, (1 << BLOCK_SIZE) - 1)

base_c1 = remote_encrypt(base_m1)
base_c2 = remote_encrypt(base_m2)

matrix = []
for i in range(BLOCK_SIZE):
    m1 = base_m1 ^ (1 << i)
    m2 = base_m2 ^ (1 << i)
    c1 = remote_encrypt(m1) ^ base_c1
    c2 = remote_encrypt(m2) ^ base_c2
    assert c1 == c2
    matrix.append(c1)

# now we just have to find the modular inverse matrix
def transpose(m):
    length = len(m)
    mt = []
    for i in range(length):
        temp = 0
        for j in range(length):
            val = (m[j] >> i) & 1
            temp |= (val << j)
        mt.append(temp)
    return mt

def identity(n):
    return [(1 << i) for i in range(n)]

def print_matrix(m):
    print("\n".join([bin(x)[2:].rjust(len(m), '0') for x in m]))
    print()

def find_inverse_matrix(m):
    length = len(m)
    inv = identity(length)
    for col in range(length):
        # find first row with 1
        row = -1
        for j in range(col, length):
            if (m[j] >> col) & 1:
                row = j
                break
        if row == -1:
            print("Can't find row with 1")
            print_matrix(m)
            raise Exception("BAD STUFF, matrix doesn't have inverse")

        # swap rows
        m[row], m[col] = m[col], m[row]
        inv[row], inv[col] = inv[col], inv[row]

        for j in range(length):
            if j == col:
                continue
            if (m[j] >> col) & 1:
                m[j] ^= m[col]
                inv[j] ^= inv[col]

    assert identity(length) == m, "Guassian elimination is incorrect"
    return inv

def matmul(a, b):
    length = len(a)
    b = transpose(b)
    c = []
    for i in range(length):
        temp = 0
        for j in range(length):
            av = a[i]
            bv = b[j]
            res = 0
            for k in range(length):
                res ^= ((av >> k) & 1) * ((bv >> k) & 1)
            temp |= (res << j)
        c.append(temp)
    return c

def matvecmul(m, v):
    length = len(m)
    res = 0
    mt = transpose(m)
    for i in range(length):
        if (v >> i) & 1:
            res ^= mt[i]
    return res

matrix = transpose(matrix)
inv_matrix = find_inverse_matrix(matrix[:])

assert matmul(matrix, identity(BLOCK_SIZE)) == matrix, "Bad matmul implementation"
assert matmul(matrix, inv_matrix) == identity(BLOCK_SIZE), "Bad inverse matrix (or matmul implementation is bad)"

base = remote_encrypt(0)

mtest = random.randint(0, (1 << BLOCK_SIZE) - 1)
ctest = remote_encrypt(mtest)
cc = matvecmul(inv_matrix, ctest ^ base)
assert cc == mtest, "Bad matvecmul"
r.close()

# multiply the matrix inv_matrix with the vectors in cflag to get the flag.
flag = b""
for i in range(0, len(cflag), BLOCK_SIZE_BYTES_HEX):
    c = int(cflag[i:i + BLOCK_SIZE_BYTES_HEX], 16)
    m = matvecmul(inv_matrix, c ^ base)
    flag += binascii.unhexlify(hex(m)[2:].rjust(BLOCK_SIZE_BYTES_HEX, '0'))

print(flag)
