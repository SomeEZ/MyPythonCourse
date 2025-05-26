'''
转义字符：
    \t 水平制表符（类似四个空格）
    \n 换行符号
'''
#换行符
print('a\nb')
#如果要输出\反斜杠，打两个代替一个\
print('\\')
#输入单引号需要在单引号前加\
print('She says: \'I Love You\'')
#或使用双引号包裹字符串
print("She says: 'I Love You'")
#print输出函数默认会自动换行
print('Hello')
print('World')
#在hello后面加,加上end=空字符串
print('Hello', end='')
print('World')
#在end中添加转义符，可以指定添加特定的转义符
print('Hello', end='\t')
print('World')
#print中连续输出多个变量，会自带空客
num1=10
num2=20
print(num1, num2)
#如果想在变量中间没有空格需要使用(f'')
print(f'num1 = {num1}, num2 = {num2}')
#也可以在字符串后面添加.format()填充参数
print('num1 = {0}, num2 = {1}'.format(num1, num2))
#默认第一个参数填充在第一个位置
print('num1 = {}, num2 = {}'.format(num1, num2))