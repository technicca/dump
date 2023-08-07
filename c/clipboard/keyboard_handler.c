// keyboard_handler.c

#include <X11/Xlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> // Include this for free function
#include "keyboard_handler.h"
#include "clipboard_handler.h"
#include "data_store.h"

static bool ctrl_down = false;
static bool c_down = false;
static bool v_down = false;

void process_keyboard_input(Display* display) {
    XEvent event;
    KeyCode ctrl_code = XKeysymToKeycode(display, XStringToKeysym("Control_L"));
    KeyCode c_code = XKeysymToKeycode(display, XStringToKeysym("c"));
    KeyCode v_code = XKeysymToKeycode(display, XStringToKeysym("v"));

    // Grab the keyboard once at the start
    XGrabKeyboard(display, RootWindow(display, DefaultScreen(display)), True, GrabModeAsync, GrabModeAsync, CurrentTime);

    while (1)
    {
        if (XPending(display) > 0)
        {
            XNextEvent(display, &event);

            switch (event.type)
            {
                case KeyPress:
                    if (event.xkey.keycode == ctrl_code)
                    {
                        ctrl_down = true;
                    }
                    else if (event.xkey.keycode == c_code)
                    {
                        c_down = true;
                    }
                    else if (event.xkey.keycode == v_code)
                    {
                        v_down = true;
                    }
                    else // Assume the pressed key is a number key
                    {
                        char number = XLookupKeysym(&event.xkey, 0);
                        if (ctrl_down && c_down) // copy
                        {
                            int slot = number - '0';
                            printf("Copying to slot %d\n", slot);
                            char* clipboard_data = read_clipboard();
                            if(clipboard_data != NULL) {    // Check if clipboard_data is not NULL
                                save_data(slot, clipboard_data);

                                // Free up the dynamically allocated memory
                                free(clipboard_data);
                                clipboard_data = NULL; // Ensure pointer isn't dangling
                            }
                        }
                        else if (ctrl_down && v_down) // paste
                        {
                            int slot = number - '0';
                            printf("Pasting from slot %d\n", slot);
                            char* data = get_data(slot);
                            write_clipboard(data);
                        }
                    }

                    break;

                case KeyRelease:
                    if (event.xkey.keycode == ctrl_code)
                    {
                        ctrl_down = false;
                    }
                    else if (event.xkey.keycode == c_code)
                    {
                        c_down = false;
                    }
                    else if (event.xkey.keycode == v_code)
                    {
                        v_down = false;
                    }
                    break;

                default:
                    break;
            }
        }
    }

    // Ungrab the keyboard once at the end
    XUngrabKeyboard(display, CurrentTime);
}
