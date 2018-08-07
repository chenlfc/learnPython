# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/25
from _for_ex import pt_title

# EX 8-12
# 三明治 sandwich 食材 ingredients 描述 describe
pt_title('EX 8 - 12')


def made_sandwich(*ingredients):
    print("\n--- Now making your sandwich ---")
    for ingredinet in ingredients:
        print("- " + ingredinet)


made_sandwich('ham 火腿', 'eggs 鸡蛋', 'sausage 香肠')
made_sandwich('eggs 鸡蛋', 'cheese 芝士')
made_sandwich('bacon 培根', 'eggs 鸡蛋', 'cheese 芝士', 'ham 火腿')

# EX 8-13
pt_title('EX 8 - 13')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


def show_profile(infos):
    print("\n--- now show your informations ---".upper())
    for k, v in infos.items():
        print("." + k.title() + "\t- " + v.title())


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)

my_profile = build_profile(
    'oven', 'chen', location='shanghai china', like='eat')
print(my_profile)
show_profile(user_profile)
show_profile(my_profile)

# EX 8-14
# 描述 describe 制造商 manufacturers 型号 model 品牌 brand 功率 power
pt_title('EX 8 - 14')


def make_car(manufacturer, model, **infos):
    describe = {}
    describe['manufacturer'] = manufacturer
    describe['model'] = model
    for key, value in infos.items():
        describe[key] = value
    return describe


my_car = make_car('梅赛德斯奔驰', 'S8', brand='benz', size='1.8L', color='red')
print(my_car)
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
