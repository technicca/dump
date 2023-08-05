import curses

def main(stdscr):
    # Making the terminal cursor invisible
    curses.curs_set(0)
    
    options = ["Option 1", "Option 2", "Option 3"]
    selected = [False, False, False]
    cursor = 0

    while True:
        stdscr.clear()

        for i, option in enumerate(options):
            prefix = "> " if i == cursor else "  "
            selection_status = "*" if selected[i] else " "
            line = "{}({}) {}".format(prefix, selection_status, option)
            stdscr.addstr(i, 0, line)
        
        stdscr.refresh()
        
        # Move the terminal cursor to the end of the options list
        stdscr.move(len(options), 0)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            cursor = (cursor - 1) % len(options)
        elif key == curses.KEY_DOWN:
            cursor = (cursor + 1) % len(options)
        elif key == ord("\n"):
            selected_options = ", ".join(option for i, option in enumerate(options) if selected[i])
            stdscr.addstr(len(options)+1, 0, "You selected: " + selected_options)
            stdscr.refresh()
            stdscr.getch()
            break
        elif key == ord(" "):
            selected[cursor] = not selected[cursor]

if __name__ == "__main__":
    curses.wrapper(main)
