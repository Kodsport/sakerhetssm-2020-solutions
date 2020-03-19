
filler = "HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.\n"
flag = "SSM{Vem_tyckte_NBSP_i_filnamn_var_en_bra_ide}\r" + filler
fake = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\r" + filler


def write_file(name, data):
    print(repr(name.encode()))
    with open(name.encode(), "wb") as f:
        f.write(data)


filename = u"the_flag_is_here"
# \u00a0
for i in range(len(filename) + 1):
    if i == 4:
        write_file(filename[:i] + u"\u00a0" + filename[i:], flag.encode())
    else:
        write_file(filename[:i] + u"\u00a0" + filename[i:], fake.encode())
        