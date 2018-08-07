# -*- coding: utf-8 -*-
# create by o.c. 2018/8/7
# file name : scatter_squares.py
# description : 使用scatter()绘制散点图并设置其样式

import matplotlib.pyplot as plt

X_VALUES = list(range(1, 1001))
Y_VALUES = [x**2 for x in X_VALUES]

plt.scatter(
    X_VALUES, Y_VALUES, c=Y_VALUES, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig('./Python编程_从入门到实践/_images/squares_plot.png', bbox_inches='tight')
