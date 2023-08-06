import curses
import random
import string
import pyperclip

ASCII_ART = """
░█▀█░█▀█░█▀▀░█▀▀░█▀▄░█░█░█▀▄
░█▀▀░█▀█░▀▀█░▀▀█░█▀▄░█░█░█░█
░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀░ 
"""

def print_ok_button(window):
    window.attron(curses.color_pair(2))  # New color pair for OK button
    window.border()
    window.addstr(1, 2, "OK")  # Display OK button
    window.refresh()

def create_ok_button_and_wait(stdscr, options):
    # Create the OK button window
    ok_button = curses.newwin(3, 6, len(options) + ASCII_ART.count('\n') + 3, 0)
    print_ok_button(ok_button)  # Display the OK button
    ok_button.getch()  # Wait for user confirmation

    # Clear the output message and the OK button
    stdscr.move(len(options)+1, 0)  # Move cursor to beginning of output message line
    stdscr.clrtobot()  # Clear to bottom of screen
    stdscr.refresh()

def print_menu(stdscr, options, current_row):
    stdscr.addstr(0, 0, ASCII_ART)
    for idx, option in enumerate(options, start=1):
        y = idx + ASCII_ART.count('\n')  # Adjust for ASCII art height
        stdscr.move(y, 0)  # Move cursor to beginning of line
        stdscr.clrtoeol()  # Clear to end of line
        if idx - 1 == current_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, 0, option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, 0, option)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    current_row = 0

    # Define the options
    options = ["8 characters", "16 characters", "24 characters", "Test option", "Exit"]

    # Color pairs
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Color pair for OK button

    # Print the menu
    print_menu(stdscr, options, current_row)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if options[current_row] == "Exit":
                break
            elif options[current_row] == "Test option":
                test_option_menu(stdscr)
                print_menu(stdscr, options, current_row)  # Refresh main menu after returning from test menu
            else:
                length = [8, 16, 24][current_row]
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
                pyperclip.copy(random_string)
                stdout_msg = f"You selected {options[current_row]}. Random string copied to clipboard: {random_string}"
                
                # Adjust for ASCII art height & menu items.
                stdscr.addstr(len(options) + ASCII_ART.count('\n') + 2, 0, stdout_msg)

                stdscr.refresh()
                create_ok_button_and_wait(stdscr, options)

        print_menu(stdscr, options, current_row)

def test_option_menu(stdscr):
    options = ["Option 1 - Random Number", "Option 2 - Random Letter", "Back to previous menu"]
    current_row = 0

    while True:
        stdscr.erase()  # Clear screen and output before displaying the menu options

        # Print the menu options
        print_menu(stdscr, options, current_row)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if options[current_row] == "Back to previous menu":
                break
            elif options[current_row] == "Option 1 - Random Number":
                random_number = random.randint(1, 100)
                stdscr.addstr(len(options) + ASCII_ART.count('\n') + 2, 0, "Generated random number: {}".format(random_number))
                stdscr.refresh()

                create_ok_button_and_wait(stdscr, options)

            elif options[current_row] == "Option 2 - Random Letter":
                random_letter = random.choice(string.ascii_letters)
                stdscr.addstr(len(options) + ASCII_ART.count('\n') + 2, 0, "Generated random letter: {}".format(random_letter))
                stdscr.refresh()

                create_ok_button_and_wait(stdscr, options)

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)