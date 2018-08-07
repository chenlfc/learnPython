# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/23
from _for_ex import pt_title

pt_title('pets.py'.upper())

pets = ['goldfish', 'dog', 'cat', 'dog', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(sorted(set(pets)))
