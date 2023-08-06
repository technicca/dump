// clipboard_handler.c

#include <X11/Xlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdlib.h>



#define CLIPBOARD_SELECTION_NAME "CLIPBOARD"

Display *display;
Window window;
Atom XA_CLIPBOARD, XA_UTF8_STRING;
bool clipboard_updated;

Display* init_clipboard(){
    display = XOpenDisplay(NULL);
    if (display == NULL) {
        fprintf(stderr, "Unable to open display. Exiting.\n");
        exit(1);
    }
    window = XCreateSimpleWindow(display, DefaultRootWindow(display), 0, 0, 1, 1, 0, BlackPixel(display, 0), BlackPixel(display, 0));
    XA_CLIPBOARD = XInternAtom(display, CLIPBOARD_SELECTION_NAME, False);
    XA_UTF8_STRING = XInternAtom(display, "UTF8_STRING", False);

    XSetSelectionOwner(display, XA_CLIPBOARD, window, CurrentTime);
    XFlush(display);

    clipboard_updated = false;

    return display;
}

void read_clipboard()
{
    Atom ret_type;
    int ret_format;
    unsigned long len, bytes_left, dummy;
    unsigned char *data;
    int result;

    XGetWindowProperty(display, DefaultRootWindow(display), XA_CLIPBOARD, 0, 0, False, AnyPropertyType, &ret_type, &ret_format, &len, &bytes_left, &data);
    if(bytes_left > 0)
    {
        result = XGetWindowProperty(display, DefaultRootWindow(display), XA_CLIPBOARD, 0, bytes_left, False, XA_UTF8_STRING, &ret_type, &ret_format, &len, &dummy, &data);
        if(result == Success){
            printf("Clipboard data: %s\n", data);
        }
    }
}

void write_clipboard(char* data)
{
    XChangeProperty(display, DefaultRootWindow(display), XA_CLIPBOARD, XA_UTF8_STRING, 8, PropModeReplace, (const unsigned char*)data, strlen(data));
}