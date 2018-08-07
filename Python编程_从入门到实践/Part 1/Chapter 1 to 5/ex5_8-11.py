# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/20
from _for_ex import pt_title

pt_title('EX 5 - 8 & 9')
# EX 5-8
users = ['jack', 'stven', 'mary', 'admin', 'oliver']
# users = [] # for ex 5-9
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user.title() +
                  ", would you like to see a status report?")
        else:
            print("Hello " + user.title() +
                  ", thank you for logging in again.")
else:
    print("We need to find some users!")

# EX 5 - 9
pt_title('EX 5 - 10')
current_users = ['jack', 'stven', 'mary', 'admin', 'oliver', 'lee', 'wesley']
new_users = ['mary', 'oliver', 'wesley', 'frank', 'wesley', 'lemon']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("The username " + new_user.title() +
              " already exists and cannot be created.")
    else:
        print("The new username " + new_user.title() + " are created!")
