'''
课后练习题
    题目一、小明的语文、数学、英语成绩，判断三门功课是否全部及格。
        要求：变量要从键盘录入，并定义变量接收用户输入，使用逻辑运算符实现if条件语句判断
    题目二、使用if else 逻辑判断完成从用户输入的三个整型数值中最大的值。
    题目三、更具用户给定的月份数据，显示月份在那个季节？if elif elif else案例
'''

#题目一
'''
#定义三个变量，使用input接受并转型成int
yw = int(input('请输入语文成绩'))
sx = int(input('请输入数学成绩'))
yy = int(input('请输入英语成绩'))
#使用if判断是否每个科目成绩都大于等于60，使用and拼接（and为全部满足才复合条件）
if yw >= 60 and sx >= 60 and yy >= 60:
    #如果满足条件则打印全部及格
    print('小明三门功课全部及格')
else:
    #如果不满足则打印有不及格
    print('小明三门功课有不及格')
'''

#题目二
#定义三个变量，使用input接受并转型成int
'''
num1 = int(input('请输入第一个整数：'))
num2 = int(input('请输入第二个整数：'))
num3 = int(input('请输入第三个整数：'))
#使用if判断和and拼接，用num1分别和num2、num3进行对比判断
if num1 >= num2 and num2 >= num3:
    print(f'{num1}是最大值')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2}是最大值')
else:
    print(f'{num3}是最大值')
'''

#题目三
month = int(input('请输入月份：'))
if month == 3 or month == 4 or month == 5:
    print('春季')
elif month == 6 or month == 7 or month == 8:
    print('夏季')
elif month == 9 or month == 10 or month == 11:
    print('秋季')
elif month == 12 or month == 1 or month ==2:
    print('冬季')