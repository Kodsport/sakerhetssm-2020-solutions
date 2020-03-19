#!/usr/bin/env python3

from lib import send, read, dh_g, dh_mod, format_key, encrypt, decrypt, int_from_bytes, int_to_bytes
from Crypto.Cipher import AES
from random import randint

from secret import flag, password

def key_exchange():
	secret = randint(2**1000, 2**1001);
	gx = int_from_bytes(read())
	gy = pow(dh_g, secret, dh_mod)
	send(int_to_bytes(gy))
	key = pow(gx, secret, dh_mod)
	return key

def main():
	generated_key = key_exchange()
	key = format_key(generated_key)
	enc_pass = read()
	dec_pass = decrypt(enc_pass, key)
	if dec_pass != password:
		print("wrong password, terminating")
		return 
	enc = encrypt(flag, key)
	send(enc)

if __name__ == "__main__":
	main()