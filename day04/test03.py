'''

'''
#定义一个计数变量
count = 0
for i in range(10): #外层循环1次
    for j in range(10): #内层就会循环所以次数
        #循环嵌套
        count += 1
#循环结束后思考count等于多少
print(count)#for i 循环依次 for j 就循环十次，for i循环了10，for j 就一共循环了100此