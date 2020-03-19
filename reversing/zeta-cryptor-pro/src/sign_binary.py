#!/usr/bin/env python3

import hashlib
import struct
import sys
import nacl.signing

"""
>>> placeholder_hash = secrets.token_bytes(64)
>>> placeholder_sig = secrets.token_bytes(64)
>>> placeholder_pub = secrets.token_bytes(32)
>>> placeholder_pub_license = secrets.token_bytes(32)
>>> ', '.join('%#04x' % x for x in placeholder_hash)
'0xd3, 0x28, 0x20, 0x72, 0xc5, 0x6d, 0xed, 0x94, 0xad, 0x60, 0x4a, 0x0b, 0x31, 0xec, 0x39, 0x4c, 0x65, 0x7a, 0x27, 0x9c, 0xdd, 0x55, 0xed, 0x3e, 0x6d, 0x92, 0xa6, 0x0c, 0x69, 0x0b, 0x71, 0xdb, 0xb6, 0x73, 0x81, 0xc1, 0x86, 0x9b, 0x44, 0xa0, 0xcd, 0x19, 0x5b, 0x29, 0x3c, 0x09, 0x9d, 0x4d, 0xdd, 0x54, 0x5e, 0x88, 0x8f, 0x14, 0x38, 0x80, 0xbb, 0xe7, 0x15, 0x27, 0x5b, 0x0a, 0x23, 0x8d'
>>> ', '.join('%#04x' % x for x in placeholder_sig)
'0xa2, 0x28, 0x51, 0x80, 0x8e, 0x59, 0xf3, 0x2a, 0xb7, 0x09, 0x8b, 0x4d, 0xdb, 0x25, 0xf6, 0xbd, 0x4d, 0x7d, 0xbd, 0xfd, 0xa7, 0xd3, 0x5e, 0xc7, 0x92, 0xff, 0x24, 0xdc, 0x0f, 0xff, 0x78, 0xc0, 0x35, 0x91, 0xb5, 0x52, 0xe7, 0xc3, 0x0a, 0xec, 0x7f, 0x3b, 0x40, 0x17, 0x69, 0x22, 0xef, 0xdb, 0x57, 0xc2, 0x52, 0x65, 0x98, 0xd6, 0xbe, 0xb7, 0xd6, 0x31, 0xb7, 0x39, 0xca, 0x08, 0x6c, 0x7e'
>>> ', '.join('%#04x' % x for x in placeholder_pub)
'0xb8, 0x5c, 0x16, 0xc3, 0x5d, 0x1f, 0x43, 0x15, 0xf4, 0x67, 0x31, 0xe0, 0x5f, 0x89, 0x29, 0xa3, 0x1d, 0x60, 0x92, 0x32, 0xd6, 0xc7, 0xf9, 0xd3, 0xc8, 0xb0, 0xc9, 0x99, 0x2c, 0x21, 0xd9, 0xc7'
>>> ', '.join('%#04x' % x for x in placeholder_pub_license)
'0x19, 0x56, 0x3f, 0x7a, 0xd6, 0xf5, 0x8b, 0xc6, 0xe7, 0x75, 0x2a, 0x90, 0xa4, 0x4a, 0x0d, 0x52, 0x0f, 0xd1, 0x6f, 0x0f, 0xfc, 0xfb, 0x87, 0x39, 0x03, 0x0b, 0x47, 0xcc, 0x94, 0xf9, 0x6c, 0xb8'
>>> placeholder_hash.hex()
'd3282072c56ded94ad604a0b31ec394c657a279cdd55ed3e6d92a60c690b71dbb67381c1869b44a0cd195b293c099d4ddd545e888f143880bbe715275b0a238d'
>>> placeholder_sig.hex()
'a22851808e59f32ab7098b4ddb25f6bd4d7dbdfda7d35ec792ff24dc0fff78c03591b552e7c30aec7f3b40176922efdb57c2526598d6beb7d631b739ca086c7e'
>>> placeholder_pub.hex()
'b85c16c35d1f4315f46731e05f8929a31d609232d6c7f9d3c8b0c9992c21d9c7'
>>> placeholder_pub_license.hex()
'19563f7ad6f58bc6e7752a90a44a0d520fd16f0ffcfb8739030b47cc94f96cb8'
"""
placeholder_hash = bytes.fromhex("d3282072c56ded94ad604a0b31ec394c657a279cdd55ed3e6d92a60c690b71dbb67381c1869b44a0cd195b293c099d4ddd545e888f143880bbe715275b0a238d")
placeholder_sig = bytes.fromhex("a22851808e59f32ab7098b4ddb25f6bd4d7dbdfda7d35ec792ff24dc0fff78c03591b552e7c30aec7f3b40176922efdb57c2526598d6beb7d631b739ca086c7e")
placeholder_pubkey = bytes.fromhex("b85c16c35d1f4315f46731e05f8929a31d609232d6c7f9d3c8b0c9992c21d9c7")
placeholder_pubkey_license = bytes.fromhex("19563f7ad6f58bc6e7752a90a44a0d520fd16f0ffcfb8739030b47cc94f96cb8")

def get_text_file_data(f):
    f.seek(0x38) # Num program headers offset
    num_program_headers = struct.unpack('<H', f.read(2))[0]
    f.seek(0x40) # Program headers table offset
    for program_header_idx in range(num_program_headers):
        f.seek(0x40 + 0x38*program_header_idx)
        program_header = f.read(0x38)
        _, p_flags, _, _, p_paddr, p_filez, _, _ = struct.unpack('<2I6Q', program_header)
        if p_flags == 0x5:
            f.seek(p_paddr)
            return f.read(p_filez)
    return False

with open('challenge_unsigned', 'rb') as fin:
    text_data = get_text_file_data(fin)
    fin.seek(0)
    elf_data = fin.read()
    placeholder_hash_offset = elf_data.find(placeholder_hash)
    placeholder_sig_offset = elf_data.find(placeholder_sig)
    placeholder_pubkey_offset = elf_data.find(placeholder_pubkey)
    placeholder_pubkey_license_offset = elf_data.find(placeholder_pubkey_license)

if not text_data:
    print('Could not find text segment')
    sys.exit(-1)

if placeholder_hash_offset == -1 or placeholder_pubkey_offset == -1 or placeholder_sig_offset == -1 or placeholder_pubkey_license_offset == -1:
    print('Could not find placeholders')
    sys.exit(-2)

# Generate demo license
license_signing_key = nacl.signing.SigningKey.generate()
demo_license = b'Demo user'.ljust(32, b'\x00') + struct.pack('<I', 10)
demo_license_signature = license_signing_key.sign(demo_license)
with open('license.dat', 'wb') as fout:
    fout.write(demo_license_signature)
pubkey_license = bytes(license_signing_key.verify_key)

print('License pubkey: %s' % pubkey_license.hex())

text_data_hash = hashlib.sha512(text_data).digest()
print('Text hash: %s' % text_data_hash.hex())

elf_signing_key = nacl.signing.SigningKey.generate()
signed_hash = elf_signing_key.sign(text_data_hash)
pubkey = bytes(elf_signing_key.verify_key)
print('Signed hash (%d): %s' % (len(signed_hash), signed_hash.hex()))

elf_data_len = len(elf_data)
#elf_data = elf_data[:placeholder_hash_offset] + text_data_hash + elf_data[placeholder_hash_offset+len(text_data_hash):]
elf_data = elf_data[:placeholder_hash_offset] + signed_hash + elf_data[placeholder_hash_offset+len(signed_hash):]
elf_data = elf_data[:placeholder_pubkey_offset] + pubkey + elf_data[placeholder_pubkey_offset+len(pubkey):]
elf_data = elf_data[:placeholder_pubkey_license_offset] + pubkey_license + elf_data[placeholder_pubkey_license_offset+len(pubkey_license):]
assert len(elf_data) == elf_data_len

with open('challenge_signed', 'wb') as fout:
    fout.write(elf_data)

print('Signing done')
