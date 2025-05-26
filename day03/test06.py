'''
更具图像完成分支流程模拟
'''

Money = 99.5  # 银行卡余额
getMoney = int(input(f'请输入取款金额，当前余额剩余{Money}\n'))
if Money >= getMoney:
    Money -= getMoney
    print(f'请取走您的{getMoney}，剩余余额{Money}')
else:
    print('余额不足')
choice = (input('是否需要退卡？（Y/N)'))

if choice == 'y' or choice == 'Y':
    print('请取走您的卡片')
else:
    print('选择了N')
