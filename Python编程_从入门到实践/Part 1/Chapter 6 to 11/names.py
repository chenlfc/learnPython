# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title
from name_function import get_formatted_name

pt_title('names.py'.upper())

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
