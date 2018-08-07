# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title

pt_title('EX 10 - 8')
# EX 10-8
path = './/_txts//'
cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

try:
    with open(path + cats_file) as cats_fobject:
        cats = cats_fobject.readlines()
    with open(path + dogs_file) as dogs_fobject:
        dogs = dogs_fobject.readlines()
except FileNotFoundError:
    pass
    # print("\n---ERROR!!! The file not found!!! ---\n")
else:
    for cat in cats:
        cat = cat.replace('\n', '')
        print("The cat name is " + cat.upper() + ".")
    print("\n---\n")
    for dog in dogs:
        dog = dog.replace('\n', '')
        print("The dog name is " + dog.upper() + ".")
