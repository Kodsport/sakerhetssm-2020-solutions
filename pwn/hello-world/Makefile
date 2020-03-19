
CFLAGS := -fno-stack-protector -no-pie

all: overflow

overflow: main.c
	gcc $(CFLAGS) $< -o $@

clean:
	rm overflow

