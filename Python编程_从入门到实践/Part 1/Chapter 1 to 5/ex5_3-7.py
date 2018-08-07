# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/20
from _for_ex import pt_title

# EX 5-3
pt_title('EX 5 - 3')
def in_color(color):
    print("\nThe alien you killed was " + color + ".")
    if color == 'green':
        print("You append 5 points.")
    else:
        print("You haven't points.")

alien_color = 'green'
in_color(alien_color)
alien_color = 'red'
in_color(alien_color)

# EX 5-4
pt_title('EX 5 - 4')
alien_color = 'yellow'
print("\nThe alien you killed was " + alien_color + ".")
if alien_color == 'green':
    print("You append 5 points.")
else:
    print("You append 10 points.")
