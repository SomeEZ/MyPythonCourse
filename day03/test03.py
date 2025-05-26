'''
    三与运算符：就是if...else....双分支结构的简化缩写
    简化是有局限性的
    
    格式：
        结果1 if 条件 else 结果2
    结果1：条件成立时返回的结果
    结果2：条件不成立时返回的结果
'''

num1 = int(input('请输入第一个整数：'))
num2 = int(input('请输入第二个整数：'))
num3 = int(input('请输入第三个整数：'))
'''
使用三目运算实现两两判断
语法格式：结果1 if 判断条件 else 结果2
如果判断结果为True返回结果1的数据，如果判断结果为False返回结果2的数据
将三目运算的结果赋值给变量second_max
'''
second_max = num1 if num1>num2 else num2
max = second_max if second_max > num3 else num3
print(f'最大的数是{max}')