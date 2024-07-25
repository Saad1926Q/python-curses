import curses
from curses import wrapper
import time

def main(stdscr):
    #Add color
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_GREEN)
    curses.init_pair(2,curses.COLOR_MAGENTA,curses.COLOR_CYAN)
    BLUE_AND_GREEN=curses.color_pair(1)
    MAGENTA_AND_CYAN=curses.color_pair(2)
    for i in range(50):
        stdscr.clear()

        color=BLUE_AND_GREEN
        
        if i%2==0:
            color=MAGENTA_AND_CYAN
        
        stdscr.addstr(f"Count:{i}",color)

        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()


wrapper(main)