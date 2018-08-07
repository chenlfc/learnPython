# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title
import json

pt_title('EX 10 - 13')


def get_stored_username():
    """如果存储了用户，就获取他"""
    filename = './/_jsons//username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    filename = './/_jsons//username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        are_you = input("Your name is " + username.title() +
                        "?\n(enter 'y' or 'n')")
        if are_you.lower() == 'y':
            print("Welcome back, " + username.title() + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " +
                  username.title() + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username.title() +
              "!")


greet_user()
