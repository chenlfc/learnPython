# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/25
from _for_ex import pt_title

pt_title('EX 10 - 2')
# EX 10-2
filename = 'E://learnPython//Python编程_从入门到实践//learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    temps = []
    for line in lines:
        line = line.replace('Python', 'C#')
        line = line.replace('\n', '')
        temps.append(line)

for line in temps:
    print(line)