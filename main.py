# coding: utf-8

import os
from core.daily_activity import *

def daily_case():
    print("开始执行日常活动")
    print("Starting......")

    base_other.sign_on()
    base_other.get_mail()
    base_other.mine_money()
    quick_shop()
    enter_room()
    main_switch()
    base_other.swap_away()
    defend_area()
    enter_challenge()

    print("ending......")

def mid_case():
    print("开始执行非日常活动")
    print("Starting......")

    base_other.sign_on()
    quick_shop(True, 0)
    enter_room(False)
    main_switch()
    defend_area(False)

    print("ending......")

def main():
    IS_ENTER = input("是否进入游戏（1/0）")
    IS_DAILY = input("执行何种操作:\n 1.日常活动 \n 2.补充活动\n 3.其他活动\n 4.进行测试\n")
    if int(IS_DAILY) == 3:
        IS_OTHER = input("执行何种活动:\n 1.喵酱大扫荡 \n 2.二次驻守\n 3.羁绊大抽奖\n 4.小二，给我来许多建经验房\n 5.积分赛一轮\n ")
        if int(IS_OTHER) == 3:
            Lotto_Time = input("请输入抽奖次数：")
    IS_SHUTDOWN = input("任务执行完毕是否关机（1/0）")
    if int(IS_ENTER) == 1:
        tab_alt()
    else:
        start_game()
        main_switch()
    if int(IS_DAILY) == 1:
        daily_case()
    elif int(IS_DAILY) == 2:
        mid_case()
    elif int(IS_DAILY) == 3:
        if int(IS_OTHER) == 1:
            quick_shop(False, 5)
        elif int(IS_OTHER) == 2:
            defend_area(False)
        elif int(IS_OTHER) == 3:
            base_other.ten_lotto(int(Lotto_Time))
        elif int(IS_OTHER) == 4:
            enter_campus()
        elif int(IS_OTHER) == 5:
            base_challenge.challenge_point(1)
        else:
            print("暂无此功能！")
    elif int(IS_DAILY) == 4:
        test()
    else:
        print("暂无此功能！")
    if int(IS_SHUTDOWN) == 1:
        os.system("shutdown -s -t 0")


def test():
    #quick_shop(True, 0)
    #base_other.ten_lotto(22)
    #base_other.swap_away()
    enter_campus()


if __name__ == '__main__':
    main()