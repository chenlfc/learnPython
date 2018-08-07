# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title
import json

pt_title('number_reader.py'.upper())

filename = './/_jsons//numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
