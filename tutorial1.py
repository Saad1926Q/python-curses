import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(20,30,"Hello")  #(0,0) is the top left
    stdscr.addstr(10,20,"Saad")
    stdscr.addstr(10,23,"Overwritten")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)