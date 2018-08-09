# -*- coding: utf-8 -*-
# create by o.c. 2018/8/8
# file name : rw_visual.py
# description : 绘制随机漫步图

import matplotlib.pyplot as plt
import pygal

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断模拟随机漫步
# while True:

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk(200)
rw.fill_walk()

# 设置绘图窗口的尺寸
plt.figure(dpi=150, figsize=(6, 4), facecolor='#B7CE74')

point_number = list(range(rw.num_points))

plt.plot(rw.x_values, rw.y_values, lineWidth=1)

# plt.scatter(
#     rw.x_values,
#     rw.y_values,
#     c=point_number,
#     cmap=plt.cm.Purples,
#     edgecolors='none',
#     s=1)

# 突出起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(
    rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

# keep_running = input("Make another wald? (y/n): ")
# if keep_running == 'n':
#     break

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Random Walk"

hist.add('x_value', rw.x_values)
hist.add('y_value', rw.y_values)

x_list_label = []
for x in range(9):
    x_list_label.append(str(x))

hist.x_labels = x_list_label
hist.x_title = "Choise List"

hist.render_to_file('./random_walk/random_walk.svg')
