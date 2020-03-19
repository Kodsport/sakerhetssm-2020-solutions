CFLAGS := -fno-stack-protector -no-pie

all: echo

echo: echo.c
	gcc $(CFLAGS) $< -o $@
	cp echo docker-pwn/files/chall
	cp flag.txt docker-pwn/files/flag.txt

clean:
	rm echo
