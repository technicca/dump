Multiple cliboards app for x11

gcc -o clip main.c data_store.c clipboard_handler.c keyboard_handler.c -lX11 -Wall