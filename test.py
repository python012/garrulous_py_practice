# -*- coding:utf-8 -*-

# content of test.py

"""
前提有以下api
api.amount_of_bills() 返回钞票的种类数目
api.num_of_bill(int:n) 返回第n种钞票的面值，n从0开始，默认面值越来越大
api.change() 返回需要支付的找零

各种面值的钞票张数充足，需要算出怎么样用最少的钞票数目去找零
"""

import api

def main():
    change = api.change
    amount = api.amount_of_bills()
    index = 0 # 调整数，例如找零金额为4，小于最大钞票金额5，则调整数为1，后面从钞票金额4开始计算

    for i in range(0, amount): # 检查找零的金额，是否比现有钞票金额大
        if change >= api.num_of_bill(amount-1-i):
            index = i
            break
        if i == amount -1:
            print("找零金额比所有钞票金额都要小！")
            return ""

    print("index: " + str(index))

    while True:
        num = {} #找零所用到的钞票总张数情况, 字典, 钞票金额：钞票张数
        rest = 0
        # n = change % api.num_of_bill(amount-1-index) # 找零金额和最大钞票金额做

        

        if change % api.num_of_bill(amount-1-index) == 0: #找零数目可以被最大钞票金额整除，最佳情况
            num["$" + str(api.num_of_bill(amount-1-index))] = change / api.num_of_bill(amount-1-index)
            break
        else: #找零数目不能被最大钞票金额整除
            n =  change / api.num_of_bill(amount-1-index) #最大钞票金额的张数
            num["$" + str(api.num_of_bill(amount-1-index))] = n #把最大金额钞票和张数，放入字典
            rest = change - api.num_of_bill(amount-1-index) * n



        print(num)


if __name__ == "__main__":
    main()
