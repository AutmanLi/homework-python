#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: autmanli
@license: Apache Licence
@file: class_unique.py
@time: 2018/10/12 15:47
"""

# 快速排序，L：数组；left：左边的下标；right：右边的下标
def quick_sort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quick_sort(array, left, q - 1)
        quick_sort(array, q + 1, right)


def partition(array, left, right):
    x = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

L=[8,20,93,81,29,83,10,12,40]
quick_sort(L,0,len(L)-1)

print(L)

