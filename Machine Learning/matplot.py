#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: autmanli
@license: Apache Licence 
@file: matplot.py
@time: 2018/10/14 14:40
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([3,5,7,6,2,6,10,15])
plt.plot(x,y,'r')# 折线 1 x 2 y 3 color
plt.plot(x,y,'g',lw=10)# 4 line w
# 折线 饼状 柱状
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([13,25,17,36,21,16,10,15])
plt.bar(x,y,0.2,alpha=1,color='b')# 5 color 4 透明度 3 0.9
plt.show()

#从-1-----1之间等间隔采66个数.也就是说所画出来的图形是66个点连接得来的
#注意：如果点数过小的话会导致画出来二次函数图像不平滑
x = np.linspace(-1, 1,66)
# 绘制y=2x+1函数的图像
y = 2 * x + 1
plt.plot(x, y)
plt.show()

# 绘制x^2函数的图像
y = x**2
plt.plot(x, y)
plt.show()


