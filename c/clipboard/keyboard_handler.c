// keyboard_handler.c

#include <X11/Xlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "keyboard_handler.h"
#include "clipboard_handler.h"

static bool ctrl_down = false;
static bool c_down = false;
static bool v_down = false;

// Function to process keyboard input
void process_keyboard_input(Display* display) {
    // Creating an event
    XEvent event;

    // Keycode for "ctrl" key
    KeyCode ctrl_code = XKeysymToKeycode(display, XStringToKeysym("Control_L"));

    // Keycode for "c" key
    KeyCode c_code = XKeysymToKeycode(display, XStringToKeysym("c"));

    // Keycode for "v" key
    KeyCode v_code = XKeysymToKeycode(display, XStringToKeysym("v"));

    // Grabbing keyboard
    XGrabKeyboard(display, RootWindow(display, DefaultScreen(display)), True, GrabModeAsync, GrabModeAsync, CurrentTime);

    while (1)
    {
        // Check to see if we have a pending event.
        if (XPending(display) > 0)
        {
            // Fetch the event from the queue.
            XNextEvent(display, &event);

            switch (event.type)
            {
                case KeyPress:
                    // Handle key press
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
                            // Subtracting `0` from the ASCII value will give us the integer value of the character
                            int slot = number - '0';
                            // Copy
                            printf("Copying to slot %d\n", slot);
                        }
                        else if (ctrl_down && v_down) // paste
                        {
                            // Subtracting `0` from the ASCII value will give us the integer value of the character
                            int slot = number - '0';
                            // Paste
                            printf("Pasting from slot %d\n", slot);
                        }
                    }

                    break;

                case KeyRelease:
                    // Handle key release
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
}
