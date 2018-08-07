# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/23
from _for_ex import pt_title

pt_title('even_or_odd.py'.upper())

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
