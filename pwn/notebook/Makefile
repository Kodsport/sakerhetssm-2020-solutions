CFLAGS := -fno-stack-protector -no-pie

all: note

note: note.c
	gcc $(CFLAGS) $< -o $@
	cp note docker-pwn/files/chall
	cp flag.txt docker-pwn/files/flag

clean:
	rm note

