# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/25
from _for_ex import pt_title

pt_title('division.py'.upper())

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ValueError:
        print("ERROR please enter some number!!!")
    except ZeroDivisionError:
        print("ERROR you can't divide by 0!")
    else:
        print(answer)
