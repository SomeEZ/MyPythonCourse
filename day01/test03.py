#快速创建.py文件的快捷键：选择想要创建文件的python包后同时按下Alt+insert

'''
    关键字：再python中有35个单词已被python赋予了特殊含义，无法作为变量名使用
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
     'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
     'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
     'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

     变量命名规则
     1、不能以数字开头
     2、之恩用a-z A-Z 0-9 和下划线_ 其他符号都是非法字符，会导致代码报错，静止使用
     3、python语言严格区分大小写，username不等于UserName
     4、驼峰命名发：
        小驼峰命名法：如userName中user和Name是两个单词，第一个单词全小写，第二个单词首字母大写，更多单词的命名同理
        大驼峰命名法：如UserName中User和Name是两个单词，每个单词首字母都大写
        下划线命名发：如user_name中user和name是两个单词，单词间用_分割
'''
#导入如系统keyword库or模块
import keyword
#控制台打印查看系统库的关键字列表
print(keyword.kwlist)
#打印系统库关键词的总长度
print(len(keyword.kwlist))