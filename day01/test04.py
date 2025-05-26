'''
    python中的数据类型
    1、Number（数字类型）
        1.int（整型）
        2.float（小数型）
        3.bool（True、False是非类）
    2、String（字符串类型）
    3、Tuple（元组）
    4、List（列表）
    5、Set（集合）
    6、Dictionary（字典）
    7、定义变量格式：
        变量名 = 变量值

    python语言中定义变量是，不需要指定变量的数据类型，python会自动根据变量值自动确定变量类型
    例：
    JAVA语言： int num = 999
    python语言： num = 999
'''
#1、整形数据 int（integer）
num=999
'''
print(f'num={num}')输出固定格式。f -> format 格式化，特点是再单引号中能书写{}，大括号可以写“变量名”。
如果没有f这个符号，单引号中的{}就没有作用，会把单引号和单引号中的内容全部识别为String类型,写了f可以把{}中变量名的值输出
'''
#print()是python中的输出函数，可以用于再控制台中查看输出结果
#查看变量的类型：type(变量名)
print(f'num = {num},type(num)={type(num)}')#输出结果为：num = 999,type(num)=<class 'int'>  class为类型 int为整型（变量num是一个int整型数据）
#定义一个字符串类型
name='玛丽亚'
