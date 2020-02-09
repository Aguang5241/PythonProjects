#-*- coding:utf-8 -*-

import curses
# curses包的封装用于实现终端无关的控制台输出以及输入处理。
from random import randrange, choice 
# random.randrange()返回指定递增基数集合中的一个随机数
# random.choice()返回指定递增基数集合中的一个随机数
from collections import defaultdict
# collections.defaultdict([default_factory[,...]]) 返回一个类似字典的对象

# 用户行为
actions = ['Up', 'Down', 'Right', 'Left', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'wsdarqWSDARQ']
# ord('str')返回str的ascii码
actions_dict = dict(zip(letter_codes, actions * 2))
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

# 阻塞＋循环，直到获得用户有效输入才返回对应行为
def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch() # .getch()属于curses包，返回0-255之间的整数
    return actions_dict[char]

# 矩阵转置
def transpose(field):
    return [list(row) for row in zip(*field)]

# 矩阵逆转
def invert(field):
    return [row[::-1] for row in field]

# 初始化
class GameField(object):
    def __init__(self, height = 4, width = 4, win = 2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset() # 棋盘重置
    
    # 重置棋盘
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)] # 列表生成式
        self.spawn() 
        self.spawn()
        # 这里的self.spawn()初始化几次决定游戏开始生成几个随机数

    # 棋盘走一步
    # 通过对矩阵进行转置与逆转，可以直接从左移得到其余三个方向的移动操作
    def move(self, direction):
        
        # 一行向左合并
        def move_row_left(row):
            def tighten(row): # 把零散的单元挤在一起
                new_row = [i for i in row if i != 0] # 先聚集
                new_row += [0 for i in range(len(row) - len(new_row))] # 再补为空
                return new_row

            def merge(row): # 把临近单元合并
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row) # assert断言语句
                return new_row
            # 先挤在一起，再合并，再挤在一起
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field))) # move[]函数名+(参数)
        moves['Up'] = lambda field: transpose(moves['left'](transpose(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False
    
    # 判断输赢
    def is_win(self):
        # any()括号里的元素不全为False, ''或 0 时返回True
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        # 当列表填满或者说元素无法再移动时any()返回False
        return not any(self.move_is_possible(move) for move in actions)

    # 绘制棋盘
    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '\t(R)Restart (E)Exit'
        gameover_string = '\tGame Over'
        win_string = '\tYou Win !'
        # 换行
        def cast(string):
            screen.addstr(string + '\n') # .addstr()属于curses包
        
        # 绘制水平分割线
        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, 'counter'): # 判断draw_hor_separator是否含有counter属性
                draw_hor_separator.counter = 0 
            cast(separator[draw_hor_separator.counter]) 
            draw_hor_separator.counter += 1 
        
        # 绘制纵向分割线 
        def draw_row(row):
            # ^ 按位异或逻辑运算符
            # str.join(sequence)在sequence元素序列中均匀插入str
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()

        cast('Score:' + str(self.score))
        if 0 != self.highscore:
            cast('High Score:' + str(self.highscore))

        for row in self.field:
            draw_hor_separator() # 绘制横向分割线
            draw_row(row) # 绘制纵向分割线

        draw_hor_separator() # 绘制底边

        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)

    # 随机生成2或4
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2 # 90% 的机会出现2，10%的机会出现4
        # 通过choice去随机筛选未被占用的二维数组列表中的位置
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        # 将new_element填入上面筛选出的位置
        self.field[i][j] = new_element

    # 判断能否移动
    def move_is_possible(self, direction):
        # 判断可否向左移动
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i + 1] != 0: # 第一格空，第二格非空
                    return True
                if row[i] != 0 and row[i] == row[i + 1]: # 第一格非空，但是第一格与第二格元素相同
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        # 判断可否向其他方向移动
        check = {}
        check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

# 主逻辑
def main(stdscr):

    def init():
        game_field.reset()
        return 'Game'

    def not_game(state):
        # 画出GAMEOVER或者win界面
        game_field.draw(stdscr)
        # 读取用户输入得到action，判断重启还是结束游戏
        action = get_user_action(stdscr)
        # 默认是当前状态，没有行为就在当前界面循环
        responses = defaultdict(lambda: state)
        # 对应不同行为转换到不同状态
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        # 画出当前棋盘状态
        game_field.draw(stdscr)
        # 读取用户输入得到action
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        } 

    curses.use_default_colors()

    # 设置终结状态最大数
    game_field = GameField(win = 64) # 内部win = 32可以删除，前面已经默认了win = 2048

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)


    
    