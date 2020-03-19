#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char byebye[] = {"echo \"these notebook challs really suck huh, wait why do we system() this\""};

struct notepad *books[8];

struct note {
    char text[64];
    char date[8];
};

struct notepad {
    struct note* notes[8];
    char name[8];
};

void add_notepad() {
    unsigned int idx;
    puts("which slot? (0-7)");
    scanf("%u", &idx);

    if (idx > 7) {
        puts("aja baja");
        return;
    }
    books[idx] = malloc(sizeof(struct notepad));
    puts("name:");
    read(0, &books[idx]->name[0], 8);
}

void add_note() {
    unsigned int idx_notepad;
    puts("which notepad? (0-7)");
    scanf("%u", &idx_notepad);

    if (idx_notepad > 7) {
        puts("aja baja");
        return;
    }

    struct notepad *np = books[idx_notepad];

    unsigned int idx_note;
    puts("which note? (0-7)");
    scanf("%u", &idx_note);
   
    if (idx_note > 7) {
        puts("aja baja");
        return;
    }

    np->notes[idx_note] = malloc(sizeof(struct note));

    puts("text:");
    read(0, &np->notes[idx_note]->text[0], 64);
    puts("date:");
    read(0, &np->notes[idx_note]->date[0], 8);

}

void edit_note() {
    unsigned int idx_notepad;
    puts("which notepad? (0-7)");
    scanf("%u", &idx_notepad);

    if (idx_notepad > 7) {
        puts("aja baja");
        return;
    }

    struct notepad *np = books[idx_notepad];

    if (np == 0)
        return;

    unsigned int idx_note;
    puts("which note? (0-7)");
    scanf("%u", &idx_note);
   
    if (idx_note > 7) {
        puts("aja baja");
        return;
    }

    if (np->notes[idx_note] == 0)
        return;

    puts("text:");
    read(0, &np->notes[idx_note]->text[0], 64);
    puts("date:");
    read(0, &np->notes[idx_note]->date[0], 8);

}

void view_note() {
    unsigned int idx_notepad;
    puts("which notepad? (0-7)");
    scanf("%u", &idx_notepad);

    if (idx_notepad > 7) {
        puts("aja baja");
        return;
    }

    struct notepad *np = books[idx_notepad];
    if (np == 0)
        return;

    unsigned int idx_note;
    puts("which note? (0-7)");
    scanf("%u", &idx_note);
   
    if (idx_note > 7) {
        puts("aja baja");
        return;
    }

    if (np->notes[idx_note] == 0)
        return;

    printf("Text %s", np->notes[idx_note]->text);
    printf("Date %s", np->notes[idx_note]->date);

}

void delete_note() {
     unsigned int idx_notepad;
    puts("which notepad? (0-7)");
    scanf("%u", &idx_notepad);

    if (idx_notepad > 7) {
        puts("aja baja");
        return;
    }

    struct notepad *np = books[idx_notepad];

    unsigned int idx_note;
    puts("which note? (0-7)");
    scanf("%u", &idx_note);
   
    if (idx_note > 7) {
        puts("aja baja");
        return;
    }
    free(np->notes[idx_note]);
}

void delete_notepad() {
    unsigned int idx;
    puts("which slot? (0-7)");
    scanf("%u", &idx);

    if (idx > 7) {
        puts("aja baja");
        return;
    }
    free(books[idx]);
}

void list_notepads() {
    puts("=======List=======");
    for (int i = 0; i < 8; i++) {
        if (books[i] != 0)
            printf("* Name: %s", books[i]->name);
    }
    puts("==================");
}

void menu() {
    puts("==================");
    puts("W - Add notepad");
    puts("A - Delete notepad");
    puts("S - Add note");
    puts("D - Delete note");
    puts("L - List notes");
    puts("E - Edit note");
    puts("V - View note");
    puts("! - Quit");
    puts("=================>");
}


int main() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    
    for (;;) {
        menu();
        char c[8] = {0};
        read(0, &c, 8);

        switch (c[0]) {
            case 'W':
                add_notepad();
            break;
            case 'A':
                delete_notepad();
            break;
            case 'S':
                add_note();
            break;
            case 'D':
                delete_note();
            break;
            case 'L':
                list_notepads();
            break;
            case 'E':
                edit_note();
            break;
            case 'V':
                view_note();
            break;

            case '!':
                goto done;
            break;
        }
    }

done:
    system(byebye);
    return 0;
}
