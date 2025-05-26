'''
    石头剪刀布小游戏
    1、石头
    2、剪刀
    3、布
'''

import random

computer = random.randint(1, 3)
player = int(input('请输入您的选择\n1、石头\n2、剪刀\n3、布\n'))
if computer == 1:
    print('电脑出的是"石头"')
elif computer == 2:
    print('电脑出的是"剪刀"')
else:
    print('电脑出的是"布"')
if player == 1:
    print('玩家出的是"石头"')
elif player == 2:
    print('玩家出的是"剪刀"')
else:
    print('玩家出的是"布"')
if 0 < player <= 3:
    if player == 1 and computer == 2\
        or player == 2 and computer ==3\
        or player == 3 and computer == 1:
            print('玩家获胜')
    elif player == computer:
        print('平局')
    else:
        print('电脑获胜')
else:
    print('输入有误')