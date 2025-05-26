'''
课堂联系：某超市T恤单价是56.5元，裤子的单价是89.8元
凤姐买了三件T恤，5条裤子，请写程序计算凤姐一共应该给多少钱？
如果老板生日打88折，凤姐需要付多少钱
'''
#T恤原价
TShirt = float(input('请输入T恤单价：'))
#裤子原价
kz = float(input('请输入裤子单价：'))
#用户输入买了多少T恤
PayTShirt = int(input('请输入买几件T恤：'))
#用户输入买了多少裤子
PayKz = int(input('请输入买几条裤子：'))
#计算不打折情况的总价（衣服数量*裤子单价+裤子数量*裤子单价）
money = PayTShirt*TShirt+PayKz*kz
#输出原价总价
print(f'你一共需要支付{money}元')
#打多少折扣
discount = 0.88
#计算打折后的T恤价格
dzTShirt = TShirt*discount
#计算打折后的裤子价格
dzKZ = kz*discount
#计算打折后的总价
dzMoney = money*discount
#输出打折后的总价
print(f'88折后，你一共需要支付{dzMoney}元')