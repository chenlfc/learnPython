# create by o.c. 2018/7/20
from _for_ex import pt_title

pt_title('EX 4 - 13')


def pt_foods(foods):
    print('西西自助餐厅菜单\n' + '-' * 50)
    for food in foods:
        print(food.title())


foods = ('mutton', 'beef', 'green vegetables', 'shrimp', 'fish')
pt_foods(foods)
foods = ('mutton', 'beef', 'green vegetables', 'tomato', 'doufu')
print("\n修改后的菜单")
pt_foods(foods)
