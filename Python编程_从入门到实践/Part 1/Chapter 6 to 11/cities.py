# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/23
from _for_ex import pt_title

pt_title('cities.py'.upper())

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city.lower() == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
