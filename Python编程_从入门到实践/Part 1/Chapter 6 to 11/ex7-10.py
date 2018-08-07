# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('EX 7 - 10')

places = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    where = input(
        "If you could visit one place in the world, where would you go? ")
    places[name] = where

    respond = input("Would you like to let another person respond? (yes/ no) ")
    if respond.lower() in ['n', 'no']:
        polling_active = False

print("\n--- Poll Results ---")
for name, where in places.items():
    print(name.title() + "'s dream vacation destination is " + where.title() +
          ".")
