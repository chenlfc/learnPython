# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/22
# from _for_ex import pt_title

# pt_title('pizza.py'.upper())

# 存储所点披萨的信息
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# # 概述所点的披萨
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
#       "with the following toppings:")


# for topping in pizza['toppings']:
#     print("\t" + topping)
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
