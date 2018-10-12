#!/usr/bin/env python
# encoding: utf-8

import math
"""
@version: ??
@author: autmanli
@license: Apache Licence 
@file: sushu.py
@time: 2018/10/12 13:29
"""

# 验证该数是不是素数，只需要验证该数能够整除从2到他的平方根即可
def check_sushu(num):
        sqrt=math.floor(math.sqrt(num))+1
        for i in range(2,sqrt):
            if num % i == 0:
                return False
        return True

#filter用法，过滤掉数组中返回值为false的项
sushu_arr=filter(check_sushu,range(1,1000000))

print(list(sushu_arr))