#!/usr/bin/env python3

import zlib
import struct

haha = b'\xb4\xa1\xd2\x4d\xea\x22\x10\x2c\xa9\x57\x6e\x4d\xed\xc1\x91\xef\x9a\xfe\x17\x24\xc9\x00\x63\xff\xed\x93\x87\x3d\xf5\x4d\xa5\x0b\x11\xb5\x83\xe7\x63\xa2\x63\xce\xba\xfc\x41\x0a\xb8\xbc\xf1\xd1\x43\xfb\xc9\x79\x12\x4e\x84\xd6\x8d\x33\xaa\xd5\x2b\xac\x12\x0e\xf6\x52\x82\x3d\x22\xd0\xe8\x90\x44\x44\x35\xc6'
oof = b'OOF{th3_p0ison_1t_stingzzzz}'

a = input('Hsssss, tell me why I should not kill you now: ').encode('ascii')
a += b'\x00'*(len(a)%2)
b = [0x13371337]
for c in [a[i:i+2] for i in range(0, len(a), 2)]:
    b.append(zlib.crc32(c, b[-1]))
b=b[1:]
b=struct.pack('<%dI' % len(b), *b)
b=bytes(x^y for x,y in zip(b, oof*len(b)))
if b==haha:
    print("Hssss. Yes, master")
else:
    print("HSSSS! Ahahahaha! Prepare to die!")
