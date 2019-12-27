# coding: utf-8

from base import base_defend, base_challenge, base_other
from base.utils import *

def quick_shop(NO_REFRESH_SHOP = True, REFRESH_NUM = 5):
    mousemove_click(1150,860,3)
    mousemove_click(975,1000,2)
    if NO_REFRESH_SHOP:
        base_other.one_shop()
    for i in range(REFRESH_NUM):
        refresh()
        base_other.one_shop()
    leave_room()

def enter_room(IS_GIFT = True):
    mousemove_click(820, 1000, 4)
    mousemove_click(950, 150, 2)
    rmb_times = 24
    while(rmb_times):
        base_other.get_rmb()
        rmb_times -= 1
        if IS_GIFT:
            base_other.give_gift()
        mousemove_click(1180, 535, 1)
    leave_room()
    any_press()

def defend_area(IS_FIRST_TIME = True):
    mousemove_click(1170, 630, 2)
    for i in range(7):
        mousemove_click(700, 1000, 1)
    if IS_FIRST_TIME:
        base_defend.first_defend()
    else:
        base_defend.second_defend()
    return_up()


def enter_challenge():
    mousemove_click(940, 1000, 2)
    base_challenge.challenge_point()
    base_challenge.challenge_forever()
    base_challenge.challenge_elements()
    base_challenge.challenge_position()
    base_challenge.challenge_items()
    base_challenge.challenge_rank()

def enter_campus():
    mousemove_click(940, 1000, 2)
    base_other.execute_train()

def start_game():
    print("Enter game......")
    tab_alt()
    base_other.enter_game()
