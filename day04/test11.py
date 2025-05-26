'''
    循环控制语句 continue
    结束本次循环，继续下次循环
'''

for i in range(10):
    #需求：当i==5时不要输出5
    if i==5:
        continue
    print(i, end='\t')