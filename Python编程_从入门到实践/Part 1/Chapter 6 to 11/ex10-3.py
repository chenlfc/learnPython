# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/25
from _for_ex import pt_title

pt_title('EX 10 - 3')
# EX 10-3
filename = './/_txts//guest.txt'

user_name = input("Please enter your name: ")
with open(filename,'a') as file_object:
    file_object.write(user_name + "\n")
