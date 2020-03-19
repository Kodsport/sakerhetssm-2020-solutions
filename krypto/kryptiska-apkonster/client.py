#!/usr/bin/env python3

from lib import send, read, dh_g, dh_mod, format_key, encrypt, decrypt, int_from_bytes, int_to_bytes
from Crypto.Cipher import AES
from random import randint

from secret import password

def key_exchange():
	secret = randint(2**1000, 2**1001);
	gx = pow(dh_g, secret, dh_mod)
	send(int_to_bytes(gx))
	gy = int_from_bytes(read())
	key = pow(gy, secret, dh_mod)
	return key

def main():
	generated_key = key_exchange()
	key = format_key(generated_key)
	enc_pass = encrypt(password, key)
	send(enc_pass)
	enc = read()
	flag = decrypt(enc, key)

if __name__ == "__main__":
	main()
