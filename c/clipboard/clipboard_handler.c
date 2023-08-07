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

char* read_clipboard()
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
        // Check the result of XGetWindowProperty
        if(result == Success){
            char* clipboard_data = malloc(len + 1);
            memcpy(clipboard_data, data, len);
            clipboard_data[len] = '\0';
            XFree(data);
            return clipboard_data;
        }
    }
    return NULL;    // return NULL if unsuccessful
}

void handle_events(char* clipboard_data) {
    XEvent event;

    while (!clipboard_updated) {
        XNextEvent(display, &event);

        switch (event.type) {
            case SelectionRequest: {
                XSelectionRequestEvent *req = &event.xselectionrequest;

                if (req->target == XA_UTF8_STRING) {
                    XChangeProperty(display, req->requestor, req->property, XA_UTF8_STRING, 8, PropModeReplace, (unsigned char *)clipboard_data, strlen(clipboard_data));
                } else {
                    XChangeProperty(display, req->requestor, req->property, None, 0, PropModeReplace, NULL, 0);
                }

                XSelectionEvent sev = {
                    .type = SelectionNotify,
                    .requestor = req->requestor,
                    .selection = req->selection,
                    .target = req->target,
                    .property = req->property,
                    .time = req->time
                };

                XSendEvent(display, req->requestor, True, NoEventMask, (XEvent *)&sev);
                clipboard_updated = true;
                break;
            }
            default:
                break;
        }
    }
}

void write_clipboard(char* data)
{
    XChangeProperty(display, DefaultRootWindow(display), XA_CLIPBOARD, XA_UTF8_STRING, 8, PropModeReplace, (const unsigned char*)data, strlen(data));
    clipboard_updated = false;
    handle_events(data);
}