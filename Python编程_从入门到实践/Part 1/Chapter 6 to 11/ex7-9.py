# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('EX 7 - 9')
sandwich_orders = ['培根', '五香熏牛肉', '鸡蛋', '火腿', '五香熏牛肉', '芝士', '五香熏牛肉']

finished_sandwiches = []

print("\n鉴于熟食店的五香熏牛肉已经卖完，本店的五香熏牛肉三明治也将下架。\n...")
while '五香熏牛肉' in sandwich_orders:
    sandwich_orders.remove('五香熏牛肉')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()    
    finished_sandwiches.append(sandwich_order)
    print("我正在制作你的" + sandwich_order + "三明治。")

print("\n--- Finished Sandwiches ---")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche + "三明治已经制作完成。")
