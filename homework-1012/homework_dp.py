# -*- coding: UTF-8 -*-

'''
project:homework_dp
description:算法第三次作业-动态规划作业
author:autmanli
'''

# 动态规划求解最大公共序列
def maxLongSubse(strA,strB):
    result_list=[[0 for _ in range(len(strA)+1)] for _ in range(len(strB)+1)]
    print(result_list)
    for i in range(1,len(strB)+1):
        for j in range(1,len(strA)+1):
            if strA[j-1] == strB[i-1]:
                result_list[i][j]=result_list[i - 1][j - 1] + 1
            else:
                result_list[i][j] = max([result_list[i - 1][j], result_list[i][j - 1]])

    print(result_list)
    x,y=len(strA),len(strB)
    Lcs=""
    while x>0 and y>0:
        if strA[x - 1] == strB[y - 1] and (result_list[y][x] == result_list[y - 1][x - 1] + 1):
            # 表示该字符是公共字符
            Lcs = strA[x - 1] + Lcs
            y, x = y - 1, x - 1
            continue
        if result_list[y][x] == result_list[y][x - 1]:
            y, x = y, x - 1
            continue
        if result_list[y][x] == result_list[y - 1][x]:
            y, x = y - 1, x
            continue

    x, y = len(strA), len(strB)
    Lcs2 = ""
    while x > 0 and y > 0:
        if strA[x - 1] == strB[y - 1] and (result_list[y][x] == result_list[y - 1][x - 1] + 1):
            # 表示该字符是公共字符
            Lcs2 = strA[x - 1] + Lcs2
            y, x = y - 1, x - 1
            continue
        if result_list[y][x] == result_list[y - 1][x]:
            y, x = y - 1, x
            continue
        if result_list[y][x] == result_list[y][x - 1]:
            y, x = y, x - 1
            continue

    # 数组的最大值即最大公共子序列的长度
    print("最长公共子序列长度为 :", result_list[len(strB)][len(strA)])
    if Lcs!=Lcs2:
        print("最长公共子序列为:", Lcs,"和",Lcs2)
    else:
        print("最长公共子序列为:", Lcs)

'''
添加一个字符的方法
char：添加的字符
str：添加字符的字符串
pos:添加字符的位置
'''
def add_char(char,str,pos):
    newStr=str[0:pos]
    newStr+=char
    for i in range(pos,len(str)):
        newStr+=str[i]
    print(newStr)

'''
移除字符的方法
str:需要移除字符的字符串
pos:移除字符的位置
'''
def remove_char(str,pos):
    newStr=str[0:pos]
    for i in range(pos+1,len(str)):
        newStr+=str[i]
    print(newStr)

'''
改变字符的方法
charN:char now
str:需要改变的字符串
pos:改变字符的位置
'''
def change_char(charN,str,pos):
    newStr=str[0:pos]
    newStr+=charN
    newStr+=str[pos+1:]
    print(newStr)

'''
将字符串A同步到字符串B的最小步数
其实只需要计算出最大公共子序列，然后将序列不同的位置进行删除、添加和修改
'''
def sync_str(strA,strB):
    pass

a='egergersdf'
b='esfrg'
maxLongSubse(a,b)

# add_char('a',b,2)
# remove_char(b,2)
# change_char('c',b,2)