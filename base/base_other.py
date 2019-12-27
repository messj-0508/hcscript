# coding: utf-8

from base.utils import *
from core.config import cfg

# 组件功能：点击进入游戏按钮
def enter_game():
    mousemove_click(950,500,1)
    mousemove_click(950,1000,20)
    any_press()

# 组件功能：购买一次刷新的全部商品
def one_shop():
    for row in range(4):
        for column in range(3):
            mousemove_click(780 + column*170,200 + row*240,0.25)
            mousemove_click(920,750,1)
            mousemove_click(920,750,1)

# 组件功能：收取一次软妹币
def get_rmb():
    mousemove_click(712, 672, 0.75)
    any_press()

# 组件功能：赠送一次礼物
def give_gift():
    mousemove_click(1150, 920, 1)
    mousemove_click(1000, 1000, 0.5)
    mousemove_click(1000, 1000, 0.5)
    mousemove_click(1000, 1000, 0.5)

# 组件功能：赠送一次礼物
def get_exp():
    for t in range(4):
        if t != 0:
            mousemove_click(690, 600, 2)
        for i in range(4):
            mousemove_click(935, 143 + i*240, 1)
            any_press()
            mousemove_click(935, 143 + i*240, 1)
            mousemove_click(1085, 635, 1)
            mousemove_click(925, 765, 1)
    leave_room(1)

# 日常功能：挖矿N次
def mine_money():
    mousemove_click(980, 50, 2)
    for i in range(cfg.FRONT.MINE_TIME):
        mousemove_click(920, 830, 0.75)
    any_press()
    any_press()

# 日常功能：签到1次
def sign_on():
    mousemove_click(678, 180, 4)
    any_press()
    any_press()

# 日常功能：查收邮件
def get_mail():
    mousemove_click(678, 240, 2)
    mousemove_click(950, 940, 2)
    any_press()
    any_press()

# 日常功能：完成一次快速挂机
def swap_away():
    mousemove_click(690,660, 1)
    mousemove_click(800,900, 1)
    mousemove_click(930,630, 1)
    any_press()
    any_press()
    any_press()


# 日常功能：羁绊十抽
def ten_lotto(time = 10):
    mousemove_click(1130, 730, 4)
    mouseclick_move(1130, 780,930,780,2)
    mousemove_click(1130, 780, 1)
    for i in range(time):
        mousemove_click(1075, 870, 2.5)
        mousemove_click(1040, 950, 1)

# 日常功能：训练室
def execute_train():
    mousemove_click(790, 230, 2)
    get_exp()