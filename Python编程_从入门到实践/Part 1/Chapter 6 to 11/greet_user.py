# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title
import json

pt_title('greet_user.py'.upper())
filename = './/_jsons//username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username.title() + "!")
