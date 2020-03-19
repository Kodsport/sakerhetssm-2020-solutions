import binascii
from Crypto.Cipher import AES

dh_g   = 23184032186474928835728343233718507461105025520303754134254645990275869771439722809850837177378023628629356200456204626348864556735698406351538444929076810155528519058778475747954982445487834513531845962211664014338984517253771726530730322999688391495019169288659391877216188760438195406817244343923404804708313265227378885976534152396149755130178595457240731542702545443459994722215637805561356789626822970031419278749848885691407894567560952716728429945746746604220511008686356768976567607178271839502730194231968019140791618237536164555995972494691247394241634753892516146865813941472935027904967150063926297510544
dh_mod = 49002319417209070957179918100033909009933738402334874644186792013258667054152579189448811367451573086272277787586983247209074250061427377855742542806941506457037291205053427101621819167382087869102496383670863902521646308341457585470741570413625142035237836671783520137040356022158749210748092737320552190812838154883788465818671512837952885835526495240157268217601713461684058218537720846576638918002782422413664913090061700601352418023069745198226434146800033719570738081587992317906747054937770694842980414587633086343435795261710110171069291426678331271803062008314470202236515253763655193513349196652485883466325
encryption_iv = b'AESCBCinitvector'

def send(data):
	out = binascii.hexlify(data)
	print(out.decode("utf-8"))

def read():
	data = input().encode("utf-8")
	return binascii.unhexlify(data)

def format_key(orig_key):
	key = 0
	while orig_key > 0:
		key ^= orig_key & 0xffffffffffffffffffffffffffffffff
		orig_key >>= 128
	return key.to_bytes(16, byteorder="big")

def encrypt(data, key):
	cipher = AES.new(key, AES.MODE_CBC, iv = encryption_iv)
	enc = cipher.encrypt(data)
	return enc

def decrypt(enc, key):
	cipher = AES.new(key, AES.MODE_CBC, iv = encryption_iv)
	data = cipher.decrypt(enc)
	return data

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')