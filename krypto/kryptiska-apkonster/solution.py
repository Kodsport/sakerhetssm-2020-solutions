from lib import *
from pwn import *
import binascii

secret = 5

def read_soc(r):
	data = r.recvline()[:-1]
	return binascii.unhexlify(data)

def write_soc(data, r):
	out = binascii.hexlify(data)
	r.sendline(out)

ip = "35.228.52.143"
client_port = 5678
server_port = 8765

client = remote(ip, server_port)
server = remote(ip, client_port)

# establish key with client
gx_client = int_from_bytes(read_soc(client))
gy_client = pow(dh_g, secret, dh_mod)
write_soc(int_to_bytes(gy_client), client)
key_client = format_key(pow(gx_client, secret, dh_mod))

# establish key with server
server_gx = pow(dh_g, secret, dh_mod)
write_soc(int_to_bytes(server_gx), server)
server_gy = int_from_bytes(read_soc(server))
server_key = format_key(pow(server_gy, secret, dh_mod))

#pass password to server
client_pass = read_soc(client)
password = decrypt(client_pass, key_client)
server_pass = encrypt(password, server_key)
write_soc(server_pass, server)

#get flag
enc_flag = read_soc(server)
flag = decrypt(enc_flag, server_key)

print("the flag is:", flag.decode('utf-8'))