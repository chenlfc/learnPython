# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title
import json

pt_title('number_writer.py'.upper())

numbers = [2, 3, 5, 7, 11, 13]

filename = './/_jsons//numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
