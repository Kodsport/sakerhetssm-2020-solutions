import zlib
from pwn import *

# https://github.com/corkami/pics/blob/master/binary/zip101/zip101.pdf
# https://github.com/corkami/formats/blob/master/archive/ZIP.md

OFF_BY = 1
data_filename = b"flag.txt"
data = b"SSM{tur_att_det_inte_var_en_zip_bomb_i_alla_fall}"
cdata = zlib.compress(data)[2:-4]


filename = "file.zip"
f = open(filename, "wb")


# Local file header
f.write(b"PK\x03\x04")
f.write(p16(10 + OFF_BY)) # version needed to extract
f.write(p16(0 + OFF_BY)) # general purpose bit flag
f.write(p16(8 + OFF_BY)) # compression method
f.write(p16(0 + OFF_BY)) # last mod file time
f.write(p16(0 + OFF_BY)) # last mod file date
f.write(p32(zlib.crc32(data) + OFF_BY)) # crc-32
f.write(p32(len(cdata) + OFF_BY)) # comp_size
f.write(p32(len(data) + OFF_BY)) # uncomp_size
f.write(p16(0 + OFF_BY)) # filename_length
f.write(p16(0 + OFF_BY)) # extra_len sze(extra_field)
f.write(cdata)

start_of_central_directory = f.tell()

# Central directory
f.write(b"PK\x01\x02")
f.write(p16(0 + OFF_BY)) # version
f.write(p16(10 + OFF_BY)) # version needed
f.write(p16(0 + OFF_BY)) # flag
f.write(p16(0 + OFF_BY)) # method
f.write(p16(0 + OFF_BY)) # file_time
f.write(p16(0 + OFF_BY)) # file_date
f.write(p32(zlib.crc32(data) + OFF_BY)) # crc-32
f.write(p32(len(cdata) + OFF_BY)) # comp_size
f.write(p32(len(data) + OFF_BY)) # uncomp_size
f.write(p16(len(data_filename) + OFF_BY)) # filename_length
f.write(p16(0 + OFF_BY)) # extra_len sze(extra_field)
f.write(p16(0 + OFF_BY)) # com_len size(file_comment)
f.write(p16(0 + OFF_BY)) # disk_start
f.write(p16(0 + OFF_BY)) # i_attrib
f.write(p32(0 + OFF_BY)) # e_attriv
f.write(p32(0 + OFF_BY)) # offset to local file header
f.write(data_filename) # filename
# extra_field
# file_comment

# EOCDH
f.write(b"PK\x05\x06")
f.write(p16(0 + OFF_BY)) # number of this disk
f.write(p16(0 + OFF_BY)) # number of the disk with the start of the central directory
f.write(p16(0 + OFF_BY)) # total number of entries in the central directory on this disk
f.write(p16(1 + OFF_BY)) # number of entries in central directory
f.write(p32(46 + len(data_filename) + OFF_BY)) # size of central directory
f.write(p32(start_of_central_directory + OFF_BY)) # offset of start of central directory with respect to the starting disk number - Central directory starting offset in this file
f.write(p16(0 + OFF_BY)) # zip comment length

f.close()

print("Done generating file.zip!")
