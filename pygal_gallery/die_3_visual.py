# -*- coding: utf-8 -*-
# create by o.c. 2018/8/8
# file name : die_3_visual.py
# description : 同时掷3个骰子，计算结果并可视化展示

import pygal

from die import Die

# 创建指定数量个D6
dies = []
die_num_sides = 32
for n_d in range(30):
    dies.append(Die(die_num_sides))

# 掷几次骰子，并将结果存储在一个列表中
max_num_result = 1000000
results = []
for roll_num in range(max_num_result):
    result = 0
    for die in dies:
        result += die.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = 0
for die in dies:
    max_result += die.num_sides

for value in range(dies.__len__(), max_result + 1):
    # 获取指定数字出现的次数
    frequencie = results.count(value)
    # 将结果存到分析列表中
    frequencies.append(frequencie)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling " + str(dies.__len__()) + " D" + str(
    die_num_sides) + " " + str(max_num_result) + " times."
x_list = []
for x_l in range(dies.__len__(), max_result + 1):
    x_list.append(str(x_l))

hist.x_labels = x_list
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D" + str(die_num_sides) + " * " + str(dies.__len__()), frequencies)

hist.render_to_file('./pygal_gallery/svg_files/die_n_visual.svg')
