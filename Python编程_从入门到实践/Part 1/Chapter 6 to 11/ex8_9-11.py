# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('EX 8 - 9')


def show_magicians(magicians):
    print("\n--- The list of magicians ---".upper())
    for magician in magicians:
        print(magician.title())


magicians = ['jake', 'tom', 'mary', 'lemon', 'frank']
show_magicians(magicians)

pt_title('EX 8 - 10')


def make_great(magicians, great_magicians):
    while magicians:
        great_magician = "the Great " + magicians.pop()
        great_magicians.append(great_magician)


great_magicians = []
make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)