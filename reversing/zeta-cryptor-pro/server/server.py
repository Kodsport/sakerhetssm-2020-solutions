#!/usr/bin/env python3

import os
import random
import secrets
import string
import struct
import subprocess
import sys
import tempfile

import nacl.secret

DEBUG = False
MAX_PATCH_LEN = 512
FLAG = 'SSM{c0py_pr0t3ction_p4tch1ng_perfect1i0n}'

def decrypt_message_ascii(ciphertext, key):
    try:
        box = nacl.secret.SecretBox(key)
        plaintext = box.decrypt(ciphertext)
        return plaintext.decode('ascii')
    except Exception as e:
        print(e)
        return False

def debug_print(str):
    if DEBUG:
        print(str)

def run_jail(elf_data):
    with tempfile.TemporaryDirectory() as tmpdir:
        binary_path = os.path.join(tmpdir, 'zeta-cryptor-pro')
        with open(binary_path, 'wb') as elf_binary:
            elf_binary.write(elf_data)
        os.chmod(binary_path, 700)

        for _ in range(random.randint(30,40)):
            # Start jail
            nsjail_args = ['nsjail', '-Mo', '--cwd', '/', '--rlimit_as', '128', '--rlimit_cpu', '5', '--rlimit_core', '0', '--rlimit_fsize', '1', '--rlimit_nofile', '32', '--rlimit_stack', '4', '--user', '99999', '--group', '99999', '-R', '/lib/x86_64-linux-gnu', '-R', '/lib64', '-R', '/usr/lib', '-R', '%s/license.dat:/license.dat' % os.getcwd(), '-R', '%s:/bin/zeta-cryptor-pro' % binary_path, '-R', '/dev/urandom', '--keep_caps', '--', '/bin/zeta-cryptor-pro']
            debug_print('Running: ' + ' '.join(nsjail_args))
            jail_proc = subprocess.Popen(nsjail_args, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Generate input and interact with process
            key = secrets.token_bytes(32)
            message = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(30, 70)))
            debug_print('Message: %s' % message)
            debug_print('Key: %s' % key.hex())
            process_input = key.hex() + '\n' + message + '\n'
            proc_output, proc_error = jail_proc.communicate(process_input.encode('ascii'))
            debug_print(proc_output)
            debug_print(proc_error)

            # Verify correctness
            expected_prefix1 = b'\nPlease input the hex encoded key:\nPlease input the message to encrypt:\n'
            expected_prefix2 = b'Encryption: '
            prefix1_offset = proc_output.find(expected_prefix1)
            prefix2_offset = proc_output.find(expected_prefix2)
            if prefix1_offset == -1 or prefix2_offset == -1:
                debug_print('Expected prefixes not found')
                return False
            encrypted_message_hex_bytes = proc_output[prefix2_offset+len(expected_prefix2):-1]
            debug_print('Encrypted data: %s' % encrypted_message_hex_bytes)
            if not all(x in string.hexdigits.encode('ascii') for x in encrypted_message_hex_bytes):
                debug_print('Non-hex digits found')
                return False
            if len(encrypted_message_hex_bytes) % 2 != 0:
                debug_print('Odd length hex string found')
                return False
            encrypted_message_hex = encrypted_message_hex_bytes.decode('ascii')
            encrypted_message = bytes.fromhex(encrypted_message_hex)
            debug_print('Encrypted message: %s' % encrypted_message_hex)
            decrypted_message = decrypt_message_ascii(encrypted_message, key)
            if not decrypted_message:
                debug_print('Failed to decrypt message')
                return False
            debug_print('Decrypted message: %s' % decrypted_message)
            if decrypted_message != message:
                debug_print('Decrypted message did not match')
                return False

        return True


print("""
Hello!

Have you heard about this new awesome message ecnryption tool?
It's called ZetaCryptorPro and is supposed to provide the heaviest of military grade encryption(tm).
I have downloaded the demo version but I don't want to pay $1337 for a license to unlock the full version.
Maybe you could help me crack the program and bypass the the license check?

Please tell me what bytes to modify in the binary by sending a hex-encoded list of elements formatted like this:
[2 bytes offset][1 byte value]

For example, if you would like me to overwrite the 10th byte with 0x44 and the 1337th byte with 0xCC send me:
0A00443905CC

I will then apply these patches and run the binary to make sure it works.
If it works properly, I will pay you for your efforts. Deal?
""")

patch = input('Please give me the patch: ')
patch = patch.strip()

if not all(x in string.hexdigits for x in patch):
    print('That is not a valid hex string! It must contain only valid hex digits. Goodbye!')
    sys.exit(1)

if len(patch) % 2 != 0:
    print('That is not a valid hex string! It must be of even length. Goodbye!')
    sys.exit(1)

patch = bytes.fromhex(patch)

if len(patch) % 3 != 0:
    print('That is not a valid patch! It must be a multiple of three bytes long. Goodbye!')
    sys.exit(1)

if len(patch)//3 > MAX_PATCH_LEN:
    print('Whoah! Chillax! That patch is a bit too large. Please keep it lean. Goodbye!')
    sys.exit(1)

with open('zeta-cryptor-pro', 'rb') as fin:
    patched_binary = fin.read()
binary_original_length = len(patched_binary)

while len(patch) > 0:
    patch_offset, patch_value, patch = *struct.unpack('<HB', patch[:3]), patch[3:]
    if patch_offset >= len(patched_binary):
        print('Whoah! That offset is outside the binary. Make sure the patch is valid before bothering me. Goodbye!')
        sys.exit(1)
    patched_binary = patched_binary[:patch_offset] + bytes([patch_value]) + patched_binary[patch_offset+1:]
assert binary_original_length == len(patched_binary)

print('Ok, cool. I will apply this patch and try the program with a few test cases to make sure it works properly.')
try:
    valid_patch = run_jail(patched_binary)
except Exception as e:
    debug_print(e)
    valid_patch = False

if valid_patch:
    print('Nice! It worked. I said I was going to pay you. Unfortunately, I spent my last money on rare first edition comic books but here is flag instead. I hope that is ok: %s' % FLAG)
else:
    print('Hey! This patch is garbage. The program does not work like intended at all. Please validate your patch before bothering me. Goodbye!')
