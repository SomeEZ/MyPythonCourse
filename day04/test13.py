'''
    字符串在程序开发中非常常用的
    字符串有一种特殊的机制：内存中的驻留机制
    驻留机制：相同的字符串，在程序运行期间，其内存中仅存储一份

    说明：如何查看对象的内存地址
    id(变量)查看变量的内存地址
'''

s1='python'
s2='python'
s3='python'
#三个字符串都对应了同一个内存地址
print(f's1 = {s1},id(s1)={id(s1)}')
print(f's1 = {s2},id(s2)={id(s2)}')
print(f's1 = {s3},id(s3)={id(s3)}')

s1='helo world'
#开辟新的内存地址，存入了hello world，更改了s1的地址，没有改变s2和s3的
print(f's1 = {s1},id(s1)={id(s1)}')
print(f's1 = {s2},id(s2)={id(s2)}')
print(f's1 = {s3},id(s3)={id(s3)}')