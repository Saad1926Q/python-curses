import curses
from curses import wrapper
import time

def main(stdscr):
    #Add color
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_GREEN)
    curses.init_pair(2,curses.COLOR_MAGENTA,curses.COLOR_CYAN)
    BLUE_AND_GREEN=curses.color_pair(1)
    MAGENTA_AND_CYAN=curses.color_pair(2)

    pad=curses.newpad(100,100) #Height and width of the pad

    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67+j)  # A->67 B->68 etc
            pad.addstr(char,BLUE_AND_GREEN)
    
    for i in range(50):
        pad.refresh(0,i,5,5,25,25)
        time.sleep(0.2)
    stdscr.getch()


wrapper(main)