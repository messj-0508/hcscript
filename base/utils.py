# coding: utf-8

import time
import autopy
import win32api
import win32con

# 切换主程序
def tab_alt():
    win32api.keybd_event(18, 0, 0, 0)  # alt键位码是18
    win32api.keybd_event(9, 0, 0, 0)  # tab键位码是9
    time.sleep(0.5)
    win32api.keybd_event(13, 0, 0, 0)  # enter键位码是13

    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)

# 鼠标基础事件：移动点击
def mousemove_click(x, y, t = 2):
    autopy.mouse.smooth_move(x, y)
    autopy.mouse.click()
    time.sleep(t)

# 鼠标基础事件：左键点击拉动一段距离
def mouseclick_move(x,y, tx, ty, t = 2):
    autopy.mouse.smooth_move(x, y)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, True) # 按下左键
    autopy.mouse.smooth_move(tx, ty)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, False) # 松开左键
    time.sleep(t)

# 刷新事件：喵咪商店
def refresh():
    mousemove_click(1187,965,2)
    mousemove_click(950,600,2)

# 返回事件:离开宿舍；离开商店；退出挑战项目；
def leave_room(t = 1.5):
    mousemove_click(700, 1000, t)

# 返回事件:退出地图；
def return_up(t = 1.5):
    mousemove_click(690, 880, t)

# 点击事件：任意按钮
def any_press(t = 1):
    mousemove_click(915,970,t)

# 点击事件：点击游戏Front和Behind页面的切换开关
def main_switch():
    mousemove_click(1170,1000,2)
    any_press()

# 点击事件：进入校园
def enter_campus():
    mousemove_click(940, 1000, 4)
    any_press()

