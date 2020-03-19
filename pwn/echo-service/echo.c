#include <stdio.h>
#include <stdlib.h>

int x,y,z = 0;

void part_one() {
    x = 3;   
}

void part_two(int i) {
    if (i == 0x1337)
        y = 5;
}

void part_three(int i, int j) {
    if (i == 0x1337 && j == 0x1338)
        z = 7;
}

void win() {
    if (x == 3 && y == 5 && z == 7) {
        puts("You win!");
        system("cat flag.txt");
    }
}

int main() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    char buffer[48];
    puts("[!] THE WORLDS MOST SECURE ECHO SERVICE [!]");
    gets(buffer);
    puts(buffer);
    return 0;
}
