// main.c
#include <X11/Xlib.h>
#include "clipboard_handler.h"
#include "data_store.h"
#include "keyboard_handler.h"

int main() {
    Display* display = init_clipboard();
    init_store();

    process_keyboard_input(display);

    return 0;
}

