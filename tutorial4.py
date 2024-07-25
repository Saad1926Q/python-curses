import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_GREEN)
    curses.init_pair(2,curses.COLOR_MAGENTA,curses.COLOR_CYAN)
    BLUE_AND_GREEN=curses.color_pair(1)
    MAGENTA_AND_CYAN=curses.color_pair(2)

    stdscr.nodelay(True)

    x,y=0,0
    while True:
        try:
            key=stdscr.getkey()
        except:
            key=None
        if key == "KEY_LEFT":
            x-=1
        elif key =="KEY_RIGHT":
            x+=1
        elif key =="KEY_UP":
            y-=1
        elif key =="KEY_DOWN":
            y+=1
        
        stdscr.clear()
        stdscr.addstr(y,x,"0")
        stdscr.refresh()

wrapper(main)