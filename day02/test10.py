'''
比较运算符，比较运算符的结果是一个布尔值 bool，True（是、对）、False（错、否）
    >
    <
    >=
    <=
    ==  等于需要写两个等于号，写一个等于号是赋值运算符
    !=
编码规则中，运算符前后都要有空格
'''

num1 = 10
num2 = 20
result = num1 == num2  # num1是否等于num2
print(f'result: {result}')  # False

result = num1 != num2  # num1是否不等于num2
print(f'result: {result}')  # True

'''
    逻辑运算符 and（并且）、or（或者）、not（不是）
    and：需要全部满足
    or：只要有一个满足即可
    not：取反，类似判断运算符中的 != 不等于
'''

#需求：判断一个人是否是男性，并且年龄大于等于18岁
gender = input('请输入性别：')
age = int(input('请输入年龄：'))

# 判断 and
result = gender == '男' and age >= 18 #and逻辑运算符，全真为真，一假即假
print(f'result: {result}')

# 需求：判断一个人是否是男性，或者年龄大于等于18岁
gender = input('请输入性别：')
age = int(input('请输入年龄：'))

# 判断 or
result = gender == '男' or age >= 18 #or逻辑运算符，全假为假，一真即真
print(f'result: {result}')

#判断 not
#结果取反
num1 = 10
num2 = 20
result = not(num1 == num2) #将判断放到not中，True变False，False变True
print(f'result: {result}') #True
