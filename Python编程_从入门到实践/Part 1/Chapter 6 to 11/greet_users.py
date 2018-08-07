# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('greet_users.py'.upper())

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

username = ['hannah', 'ty', 'margot']
greet_users(username)
