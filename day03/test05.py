'''
    if嵌套练习
    题目：一家商店，会员购买商品
    会员消费金额大于等于200，则打8折，大于等于100，打9折
    非会员购买商品，大于等于200打9.5折，不满200不打折
'''
vip = input('请问您是否本店会员 y/n：')
money = float(input('请输入金额：'))

if vip == 'y' or vip == 'Y':
    # 会员进这里
    if money >=200:
        #会员消费满200了
        print(f'八折后您需要支付{money*0.8}元')
    elif money >= 100:
        #会员消费满100
        print(f'九折后您需要支付{money*0.9}元')
    else:
        #会员消费不满折扣条件
        print(f'您不满折扣要求需要支付{money}元')
else:
    #非会员进这里
    if money >=200:
        #非会员消费满200打98折
        print(f'九五折后您需要支付{money*0.98}元')
    else:
        #非会员消费不满200不打折
        print(f'您不满足折扣要求需要支付{money}元')