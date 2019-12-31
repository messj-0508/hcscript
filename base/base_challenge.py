# coding: utf-8

import random

from base.utils import *

# 战斗准备：物资筹备；元素搜集；职业考核；
def one_fight(t = 100):
    mousemove_click(920, 780, 2)
    mousemove_click(930, 900, 2)
    time.sleep(t)
    any_press()

# 战斗准备：积分赛；
def one_fight_II():
    mousemove_click(930, 800, 1.25)
    mousemove_click(930, 900, 1.25)
    time.sleep(60)
    any_press()

# 挑战事件3-1：物资筹备
def challenge_items():
    mousemove_click(740, 850, 2)
    for num in range(5):
        print("challenge_items : %d"%num)
        mousemove_click(1120, 200, 1)
        one_fight(150)
    any_press()
    leave_room()

# 挑战事件3-2：元素搜集
def challenge_elements():
    mousemove_click(940, 850, 2)
    now = int(time.time() + random.randint(0, 9999))
    now %= 5
    for num in range(3):
        print("challenge_elements : %d"%num)
        mousemove_click(1120, 200 + (now * 155), 1)
        one_fight(95)
    any_press()
    leave_room()

# 挑战事件3-3：职业考核
def challenge_position():
    mousemove_click(1140, 850, 2)
    for num in range(3):
        print("challenge_position : %d"%num)
        mousemove_click(1120, 200 + (num * 155), 1)
        one_fight(90)
    any_press()
    leave_room()

# 挑战事件2-1：极限拟战
def challenge_forever():
    mousemove_click(750, 600, 2)
    mousemove_click(900, 900, 2)
    mousemove_click(930, 900, 2)
    time.sleep(240)
    any_press()

# 挑战事件1-1：积分赛
def challenge_point(times = 2):
    mousemove_click(1000, 200, 2)
    for times in range(times):
        for num in range(3):
            print("challenge_point : %d"%(num+times*6))
            mousemove_click(1100, 595 + (num * 125), 1)
            one_fight_II()

        for num in range(3, 6):
            print("challenge_point : %d"%(num+times*6))
            mouseclick_move(950, 900, 950, 500, 1)
            mousemove_click(1100, 595 + ((num - 3) * 125), 1)
            one_fight_II()
        if times == 0:
            mousemove_click(1150, 1000, 1)
            mousemove_click(930, 630, 1)
    any_press()
    leave_room()

# 挑战事件1-2：抢位赛
def challenge_rank():
    pass