# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/23
from _for_ex import pt_title

# pt_title('EX 7 - 1')
# # EX 7-1
# prompt = "\nCAR RENTAL"
# prompt += "\nWhat kind of car would you like to rent? "

# car = input(prompt)
# print("\nLet me see if I can find you a " + car.title() + ".")

# # EX 7-2
# pt_title('EX 7 - 2')
# prompt = "\n餐厅订位程序"
# prompt += "\n请问有多少人用餐？"

# use = input(prompt)
# use = int(use)

# if use > 8:
#     print("\n对不起，没有这么多人的空桌！")
# else:
#     print("\n好的，已经为您记录。届时请莅临用餐！")

# EX 7-3
pt_title("EX 7 - 3")
prompt = "\nPlease enter a number: "
number = input(prompt)
number = int(number)

if number % 10:
    print("\nThe number is not an integer multiple of 10!")
else:
    print("\nThe number is an integer multiple of 10!")
