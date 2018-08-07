# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('EX 7 - 8')
sandwich_orders = ['培根三明治', '鸡蛋三明治', '火腿三明治']

finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print("我正在制作你的" + sandwich_order + "。")

print("\n--- Finished Sandwiches ---")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche + "已经制作完成。")
