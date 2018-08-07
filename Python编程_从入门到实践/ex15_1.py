# -*- coding: utf-8 -*-
# create by o.c. 2018/8/7
# file name : ex15_1.py
# description : 绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值。

import matplotlib.pyplot as plt

# VALUE_X = [1, 2, 3, 4, 5]
# VALUE_Y_CUBE = [x**3 for x in VALUE_X]

# plt.plot(VALUE_X, VALUE_Y_CUBE)

# plt.show()
# 设置窗体背景色
fig = plt.figure()
rect = fig.patch
rect.set_facecolor('darkslategray')

VALUE_X = list(range(1, 5001))
VALUE_Y_CUBE = [x**3 for x in VALUE_X]

plt.scatter(VALUE_X, VALUE_Y_CUBE, c=VALUE_Y_CUBE, cmap=plt.cm.Greens, s=30)
plt.axis([0, 5000, 0, 125000000000])

plt.title("Cube Numbers", fontsize=24, color='#afeeee')
plt.xlabel("Value", fontsize=14, color='#ffaaee')
plt.ylabel("Cube of Value", fontsize=14, color='#ffaaee')

plt.tick_params(axis='both', which='major', labelsize=14)
# plt.set_facecolor('lightgoldenrodyellow')
plt.show()
