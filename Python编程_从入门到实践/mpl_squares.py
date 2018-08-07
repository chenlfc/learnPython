# -*- coding: utf-8 -*-
# create by o.c. 2018/8/7
# file name : mpl_squares.py
# description : 绘制简单的折线图

import matplotlib.pyplot as plt

INPUT_VALUES = [1, 2, 3, 4, 5]
SQUARES = [1, 4, 9, 16, 25]
plt.plot(INPUT_VALUES, SQUARES, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
