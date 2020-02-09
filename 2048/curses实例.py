#-*- coding: UTF-8 -*-

import curses

stdscr = curses.initscr()

def display_info(str, x, y, colorpair = 2):
    '''使用指定的colorpair显示文字'''
    global stdscr # 全局变量
    stdscr.addstr(y, x, str, curses.color_pair(colorpair))
    stdscr.refresh()

def get_ch_and_continue():
    '''演示press any key to continue'''
    global stdscr
    # 设置nodelay，为0时会变成阻塞式等待
    stdscr.nodelay(0)
    # 输入字符
    ch = stdscr.getch()
    # 重置nodelay,使得控制台可以以非阻塞的方式接受控制台输入，超时1秒
    stdscr.nodelay(1)
    return True

def set_win():
    '''控制台设置'''
    global stdscr
    # 使用颜色首先调用的方法
    curses.start_color()
    # 文字和背景设置
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # 关闭屏幕回显
    curses.noecho()
    # 输入时不需要回车
    curses.cbreak()
    #设置nodelay，使得控制台可以以非阻塞的方式接受控制台输入，超时1秒
    stdscr.nodelay(1)

def unset_win():
    '''控制台重置'''
    global stdscr
    #恢复控制台默认设置（若不恢复，会导致即使程序结束退出了，控制台仍然是没有回显的）
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    #结束窗口
    curses.endwin()

if __name__ == "__main__":
    try:
        set_win()
        display_info('hello, curses!', 0, 5)
        display_info('press any key to continue...', 0, 10)
        get_ch_and_continue()
    except Exception as e:
        raise e
    finally:
        unset_win()