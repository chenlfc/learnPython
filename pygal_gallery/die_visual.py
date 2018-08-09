# -*- coding: utf-8 -*-
# create by o.c. 2018/8/8
# file name : die_visual.py
# description : 掷骰子

import pygal
import matplotlib.pyplot as plt

from die import Die

# 创建一个D6和一个D10
die_1 = Die(6)
die_2 = Die(8)

# 掷几次骰子，并将结果存储在一个列表中
results = []
x_value = []
y_value = []
for roll_num in range(100):
    x_value.append(die_1.roll())
    y_value.append(die_2.roll())
    result = x_value[-1] + y_value[-1]
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequencie = results.count(value)  # list.count(value) 用于返回值出现的次数
    frequencies.append(frequencie)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D8 and D8 1,000,000 times."
x_list = []
for x_l in range(2, 16 + 1):
    x_list.append(str(x_l))

hist.x_labels = x_list
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('./pygal_gallery/svg_files/die_visual.svg')

# plt.plot(x_value, y_value, c='red', lineWidth=0.5)

plt.scatter(x_value, y_value, s=20)
plt.show()