# create by o.c. 2018/7/20
from _for_ex import pt_title

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# 4-10
pt_title('EX 4 - 10')

print("The full items in the list are:")
print(my_foods)
print("\nThe first three items in the list are:")
print(my_foods[:3])
print("\nThe items from the middle of the list are:")
print(my_foods[1:4])
print("\nThe last three items in the list are:")
print(my_foods[-3:])

# 4-11
pt_title('EX 4 - 11')

pizzas = ['seafood pizza 海鲜披萨', 'cheese pizza 芝士披萨']
friend_pizzas = pizzas[:]
pizzas.append('iron plate pizza 铁盘披萨')
friend_pizzas.append('assorted pizza 什锦披萨')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12
pt_title('EX 4 - 12')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())
