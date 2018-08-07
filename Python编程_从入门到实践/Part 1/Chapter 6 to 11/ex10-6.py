# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title

pt_title('EX 10 - 6')
# EX 10-6

while True:
    try:
        print("\nPlease enter two number to plus: ")
        print("(enter 'q' to quit)")
        first_n = input("First number: ")
        if first_n.lower() == 'q':
            break
        second_n = input("Second number: ")
        if second_n.lower() == 'q':
            break
        plus_n = int(first_n) + int(second_n)
    except ValueError:
        print("ERROR Value ERROR!!!")
    else:
        print(str(first_n) + " + " + str(second_n) + " = " + str(plus_n))
