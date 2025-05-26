'''
input 是python语言中系统提供的输入函数
input 是一个阻塞函数，如果用户不输入，程序不会向下执行
格式：
    input(prompt)
    prompt:提示信息，默认值为None不是提示
    返回值：用户输入的内容，全部都是字符串类型
说明：
    由于input输入函数会返回结果，所以需要定义一个函数接受输入的内容
'''
name = input('请输入您的姓名：')
age = input('请输入您的年龄：')
gender = input('请输入您的性别：')  #性别单词gender sex F(Female女性) M(Male男性)
#用户不输入数据，不会执行下方的print函数
print(f'大家好，我叫{name}, 我今年{age}岁，性别{gender}')