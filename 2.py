# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/28 2:25
"""
# import random
# choices=["Rock","Paper","Scissors"] #ʯͷ������
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
#         print("ƽ��!")
#     elif player == "ʯͷ":
#         if computer == "��":
#             print("������!", "���Ե�", computer, "�ȵù�", player)
#             cpu_score += 1
#         else:
#             print("��Ӯ��!", "��ҵ�", player, "�ȵù�", computer)
#             player_score += 1
#     elif player == "��":
#         if computer == "����":
#             print("������!", "���Ե�", computer, "�ȵù�", player)
#             cpu_score += 1
#         else:
#             print("��Ӯ��!", "��ҵ�", player, "�ȵù�", computer)
#             player_score += 1
#     elif player == "����":
#         if computer == "ʯͷ":
#             print("������...", "���Ե�", computer, "�ȵù�", player)
#             cpu_score += 1
#         else:
#             print("��Ӯ��!", "��ҵ�", player, "�ȵù�", computer)
#             player_score += 1

import math

a = float(input("������a��ֵ:"))
b = float(input("������b��ֵ:"))
c = float(input("������c��ֵ:"))
m = b ** 2 - 4 * a * c

if (m < 0):
    print("�޽�")
else:
    e = math.sqrt(m)
    x1 = ((-b + e) / (2*a))
    x2 = ((-b - e) / (2*a))
    print('x1=', x1, 'x2=', x2)
