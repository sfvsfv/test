# coding=gbk
"""
作者：川川
@时间  : 2022/3/28 2:25
"""
# import random
# choices=["Rock","Paper","Scissors"] #石头剪刀布
# computer=random.choice(choices)
#
# cpu_score = 0
# player_score = 0
#
# # player=False
#
# while True:
#     player = input("Rock,Paperor,Scissors?").capitalize()
#
#     if player == computer:
#         print("平局!")
#     elif player == "石头":
#         if computer == "布":
#             print("你输了!", "电脑的", computer, "比得过", player)
#             cpu_score += 1
#         else:
#             print("你赢了!", "玩家的", player, "比得过", computer)
#             player_score += 1
#     elif player == "布":
#         if computer == "剪刀":
#             print("你输了!", "电脑的", computer, "比得过", player)
#             cpu_score += 1
#         else:
#             print("你赢了!", "玩家的", player, "比得过", computer)
#             player_score += 1
#     elif player == "剪刀":
#         if computer == "石头":
#             print("你输了...", "电脑的", computer, "比得过", player)
#             cpu_score += 1
#         else:
#             print("你赢了!", "玩家的", player, "比得过", computer)
#             player_score += 1

import math

a = float(input("请输入a的值:"))
b = float(input("请输入b的值:"))
c = float(input("请输入c的值:"))
m = b ** 2 - 4 * a * c

if (m < 0):
    print("无解")
else:
    e = math.sqrt(m)
    x1 = ((-b + e) / (2*a))
    x2 = ((-b - e) / (2*a))
    print('x1=', x1, 'x2=', x2)
