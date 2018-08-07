# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/22
from _for_ex import pt_title

pt_title('EX 6 - 1')
people = {
    'fist_name': 'frank',
    'last_name': 'li',
    'age': 24,
    'city': 'Shanghai',
}
print(people)

pt_title('EX 6 - 2')
like_number = {
    'lisa': 13,
    'sarua': 4,
    'jake': 88,
    'tom': 22,
    'frank': 11,
}
for name, number in like_number.items():
    print(name.title() + " like number is " + str(number) + ".")

pt_title('EX 6 - 3')
key_of_dict = {
    'for': 'for循环，是一个最常用的循环语句',
    'if': 'if条件判断语句，用于判断并执行不同的分支',
    'class': 'class用于声明类的关键字',
    'print': 'print用于向屏幕输出信息',
    'and': 'and条件判断语句，逻辑和',
}
for k,des in key_of_dict.items():
    print(k + ":\t" + des)
