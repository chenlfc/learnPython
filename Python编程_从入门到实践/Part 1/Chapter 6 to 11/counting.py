# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/23
from _for_ex import pt_title

pt_title('counting.py'.upper())

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

current_number = 0
while current_number < 100:
    current_number += 1
    if current_number % 10 == 0:
        print()
    if current_number % 2 == 0:
        continue
    print(current_number, end='\t')
print()
