# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/19
from _for_ex import pt_title

pt_title('banned_user.py')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
