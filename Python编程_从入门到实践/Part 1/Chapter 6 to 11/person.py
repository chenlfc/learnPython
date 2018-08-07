# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('person.py'.upper())

def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 22)
print(musician)
