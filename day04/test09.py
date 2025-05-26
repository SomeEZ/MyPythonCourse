'''
    个人联系。使用for循环打印一个九九乘法表
'''

for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={j*i}', end='\t')
    print()