'''
用for循环1到100之间的整数之和

python提供了两种循环实现方式，while和for+range()，如何选择？
1、while循环 一般在不知道循环次数的情况下使用，一般情况都是while True + break跳出循环
2、for + range循环 一般在已知具体循环次数的条件下使用
'''
sum = 0
for i in range(1, 101):
    sum += i
print(f'sum={sum}')
