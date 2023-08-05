#include <stdlib.h>
#include <curses.h>

// gcc c.c -o main -lncurses
#define OPTION_COUNT 3

int main() {
    char* options[OPTION_COUNT] = {"Option 1", "Option 2", "Option 3"};
    int selected[OPTION_COUNT] = {0, 0, 0};
    int cursor = 0;

    initscr();
    raw();
    keypad(stdscr, TRUE);
    noecho();
    curs_set(0);

    while (1) {
        clear();
        for (int i = 0; i < OPTION_COUNT; i++) {
            printw("%s(%c) %s\n", i == cursor ? "> " : "  ", selected[i] ? '*' : ' ', options[i]);
        }
        refresh();

        int key = getch();
        if (key == KEY_UP) {
            cursor = (cursor - 1 + OPTION_COUNT) % OPTION_COUNT;
        } else if (key == KEY_DOWN) {
            cursor = (cursor + 1) % OPTION_COUNT;
        } else if (key == '\n') {
            printw("You selected:");
            for(int i = 0; i < OPTION_COUNT; i++){
                if(selected[i]){
                    printw(" %s,", options[i]);
                }
            }
            printw("\nPress any key to exit...");
            refresh();
            getch();
            break;
        } else if (key == ' ') {
            selected[cursor] = !selected[cursor];
        }
    }

    endwin();

    return 0;
}
