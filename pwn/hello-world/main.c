#include <stdio.h>
#include <stdlib.h>

void win() {
    int f = open("flag.txt", 0);
    char buff[1024];
    read(f, buff, 1024);
    puts(buff);
}

int main() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);

    char input[8];

    puts("Hello?");
    gets(input);

    if (!strcmp(input, "World") == 0)
        exit(0);

    puts("Hello, world!");
    return 0;
}
