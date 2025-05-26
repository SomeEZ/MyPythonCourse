'''
字符串，整型，浮点型之间的类型转换
格式：
    1、整型 int(变量)
    2、浮点型 float(变量)
    3、字符串 str(变量)
'''
from importlib import reload

#字符串类型数字
num1 = '10'
num2 = '20'
#result = unm1+num2字符串相加或获得1020，两个字符串相加会得到字符串拼接
result=num1+num2
print(f'result = {result}')
#如果要字符串类型数字以数学相加
n1=int(num1)
n2=int(num2)
result = n1+n2

#float 浮点型
f1 = 66.66
f2 = 88.88
result = f1+f2
print(f'result = {result}')
#先进行浮点转整型   浮点型转换为整型时直接丢弃小数（会导致数据精度丢失）
i1 = int(f1)    #66
i2 = int(f2)    #88
result = i1+i2  #66+88=154
print(f'result = {result}')

#整型转换为浮点
n3 = 10
n4 = 20
f3 = float(n3)
f4 = float(n4)
result = f3+f4
print(f'result = {result}')

#整型和浮点进行运算  只要有浮点型参与运算，为了保证结果精度，结果会为浮点型
n=10
f=6.66
result = n+f
print(f'result = {result}')