# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/22
from _for_ex import pt_title

pt_title('EX 6 - 4')
key_of_dict = {
    'for': 'for循环，是一个最常用的循环语句',
    'if': 'if条件判断语句，用于判断并执行不同的分支',
    'class': 'class用于声明类的关键字',
    'print': 'print用于向屏幕输出信息',
    'and': 'and条件判断语句，逻辑和',
    'set': 'set()用于找出字典的值中的独一无二的元素并返回一个集合',
    'sorted': 'sorted()用于排序字典中的键或者值并返回一个集合',
    'items': 'items()是字典中所有项的集合',
    'keys': 'keys()是字典的键集合',
    'values': 'values()是字典的值集合',
}
for k, des in key_of_dict.items():
    print(k + ":\t" + des)

pt_title('EX 6 - 5')
river_dict = {
    'nile': 'egypt',
    'changjiang': 'china',
    'huanghe': 'china',
}
for river, loc in river_dict.items():
    print("The " + river.title() + " runs through " + loc.title() + ".")
print("\nThe rivers is:")
for river in sorted(river_dict.keys()):
    print(river.title())
print("\nThe location is:")
for loc in set(river_dict.values()):
    print(loc.title())

pt_title("EX 6 - 6")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
inquiry_names = ['serah', 'tom', 'jake', 'phil', 'jen']
for inquiry_name in inquiry_names:
    print(inquiry_name.title())
    if inquiry_name in favorite_languages.keys():
        print("\tThank you for inquiry!")
