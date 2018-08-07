# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/25
from _for_ex import pt_title

pt_title('EX 10 - 1')
# EX 10-1
filename = 'E:/learnPython/Python编程_从入门到实践/learning_python.txt'
with open(filename) as file_object:
    print(file_object.readlines())
    print()
    file_object.seek(0)
    for line in file_object.readlines():
        print(line, end='')
    print()
    file_object.seek(0)
    lines = file_object.readlines()

for line in lines:
    print(line, end='')
