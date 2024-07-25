import curses
from curses import wrapper
import time
from curses.textpad import Textbox,rectangle

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_GREEN)
    curses.init_pair(2,curses.COLOR_MAGENTA,curses.COLOR_CYAN)
    BLUE_AND_GREEN=curses.color_pair(1)
    MAGENTA_AND_CYAN=curses.color_pair(2)


    win=curses.newwin(3,18,2,2)
    box=Textbox(win)
    rectangle(stdscr,1,1,5,20)

    stdscr.refresh()

    box.edit()

    stdscr.getch()

wrapper(main)