"""
python语言
项目练习，代码练习
原作者数字华容道改编
"""


import random  # 导入随机模块
from tkinter import *  # 导入图形化界面


def button_click(x, y, game_diff):
    """声明空白按钮行列号和步数的变量为全局变量"""
    global row_of_space
    global col_of_space
    global step_number

    """判断判断点击按钮旁是否为空白按钮，是则交换位置"""
    if abs(x - row_of_space) + abs(y - col_of_space) == 1:  # ==1说明相邻
        step_number = step_number + 1
        label_step_number['text'] = '步数' + str(step_number)

root = Tk()

label_step_number = Label(root, text='步数:' + str(step_number), bg='black', fg='yellow', font=("Arial", 10))