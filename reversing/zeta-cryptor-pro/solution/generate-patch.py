#!/usr/bin/env python3

import struct

with open('./zeta-cryptor-pro', 'rb') as fin:
    original_binary = fin.read()

with open('./zeta-cryptor-pro.patched', 'rb') as fin:
    patched_binary = fin.read()

assert len(original_binary) == len(patched_binary)
assert len(original_binary) <= 0xFFFF

patches = []
for offset in range(len(original_binary)):
    if original_binary[offset] != patched_binary[offset]:
        patches.append((offset, patched_binary[offset]))

patch = b''.join(struct.pack('<HB', offset, val) for offset, val in patches)
print('Patch string')
print(patch.hex())

"""
md5sum:
20aed6d4800e23902864851d19ee15b3  ./zeta-cryptor-pro
24dfc000ff85e50afa45f09c9b14bff8  ./zeta-cryptor-pro.patched

Patch: f517eb1c18901d18901e18901f18902018902318eb5718ebf518eb4519ebbc19ebfc19eb6a1aebc01aeb011beb561beb
"""
