from lib import *
import binascii

secret = 5

# server:
# means read data from the server
def read_data(r):
	data = input(f"{r}: ")
	return binascii.unhexlify(data)

# server: ...data...
# means send this data to the sercer
def write_data(data, r):
	out = binascii.hexlify(data)
	print(f"{r}: {out.decode('utf-8')}")

client = "client"
server = "server"

# establish key with client
gx_client = int_from_bytes(read_data(client))
gy_client = pow(dh_g, secret, dh_mod)
write_data(int_to_bytes(gy_client), client)
key_client = format_key(pow(gx_client, secret, dh_mod))

# establish key with server
server_gx = pow(dh_g, secret, dh_mod)
write_data(int_to_bytes(server_gx), server)
server_gy = int_from_bytes(read_data(server))
server_key = format_key(pow(server_gy, secret, dh_mod))

#pass password to server
client_pass = read_data(client)
password = decrypt(client_pass, key_client)
server_pass = encrypt(password, server_key)
write_data(server_pass, server)

#get flag
enc_flag = read_data(server)
flag = decrypt(enc_flag, server_key)

print(flag)