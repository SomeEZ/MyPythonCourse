'''
循环控制语句：break 跳出当前循环

需求：询问你的女朋友到底爱不爱你
如果答案是不爱，那就往死里问，知道女朋友说，爱你位置，然后你说，那我们结婚把，跳出循环
'''

while True:
    choice = input('你到底爱不爱我(y/n)')
    if choice == 'y' or choice == 'Y':
        print('那我们就结婚把')
        break #循环中一旦遇到break就跳出循环

print('循环结束执行后续代码')