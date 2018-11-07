# -*- coding:utf-8 -*-

# content of api.py

__bills_list = [2, 3, 4, 5]

def amount_of_bills():
    """
    返回钞票的种类数目
    """
    print("钞票总类: " + str(len(__bills_list)))
    return len(__bills_list)


def num_of_bill(n):
    """
    返回第n种钞票的面值，n应从0开始，默认面值越来越大
    """
    if n > (len(__bills_list) - 1) or n < 0:
        print("num_of_bill()传入参数 %d 有误，返回0" % n)
        return 0
    else:
        return __bills_list[n]


change = 10 #找零的总金额

