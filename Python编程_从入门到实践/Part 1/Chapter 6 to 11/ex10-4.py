# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/25
from _for_ex import pt_title

pt_title('EX 10 - 4')

filename = ".//_txts//guest_book.txt"

with open(filename, 'a') as file_object:
    while True:
        print("\n--- Please enter your name ---")
        print("(enter 'q' to quit) ")
        guest_name = input("> ")
        if guest_name.lower() == 'q':
            break
        else:
            print("\nHello " + guest_name.title() + ".")
            file_object.write(guest_name.title() + "\n")
