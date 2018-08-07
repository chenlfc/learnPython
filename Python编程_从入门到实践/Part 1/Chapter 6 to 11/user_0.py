# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/22
from _for_ex import pt_title

pt_title('user_0.py'.upper())
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
