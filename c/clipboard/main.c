// main.c


#include <X11/Xlib.h>
#include "clipboard_handler.h"
#include "data_store.h"
#include "keyboard_handler.h"
#include <stdlib.h>
#include <stdio.h>

int main() {
    Display* display = init_clipboard();
    if (display == NULL) {
        fprintf(stderr, "Unable to initialize clipboard. Exiting.\n");
        return 1;
    }
    init_store();

    process_keyboard_input(display);

    return 0;
}
