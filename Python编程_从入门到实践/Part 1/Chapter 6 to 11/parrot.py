# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/23
from _for_ex import pt_title

pt_title('parrot.py'.upper())

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# name = input("Please enter your name: ")
# print("Hello, " + name.title() + "!")

# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print("Hello, " + name.title() + "!")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
active = True
while active:
    message = input(prompt)
    if message.lower() != 'quit':
        print(message.title())
    else:
        active = False
