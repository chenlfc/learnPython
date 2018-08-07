# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title
import json

pt_title('EX 10 - 11')

# EX 10-11


def save_number():
    """提示用户输入将数字并存储到文件中"""
    filename = './/_jsons//number.json'
    while True:
        try:
            number = input("Please enter your like number: ")
            number = int(number)
        except ValueError:
            print("Error! you must enter a number!")
        else:
            with open(filename, 'w') as f_obj:
                json.dump(number, f_obj)
            return number


def load_number():
    """从文件中读取数字，并输出"""
    filename = './/_jsons//number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def get_number():
    """获取用户喜欢的数字"""
    number = load_number()
    if number == None:
        number = save_number()
    print("I know your favorite number! It's " + str(number) + ".")


get_number()
