import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Typeracer")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)