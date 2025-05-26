'''
思考题，将下面每一个的输出结果写在旁边
'''

n = 10

n += 1
print(f'n: {n}')    #11

n -=5
print(f'n: {n}')    #6

n *= 5
print(f'n: {n}')    #30

n /=5
print(f'n: {n}')    #6.0（除法把n变成了浮点数）

n %=5
print(f'n: {n}')    #1.0