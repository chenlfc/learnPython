# create by o.c. 2018/7/19
def print_list(ls):
    """按格式输出列表内容
    
    Arguments:
        ls {[list]} -- 要输出的列表
    """

    for l in ls:
        print(l.upper(), end=' ')
    print()


cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True) # 使用sort对列表的排序时永久性的
print_list(sorted(cars, reverse=True))  # 使用sorted函数对于列表的排序时临时性的
print('-' * 20)
# print(cars)
print_list(cars)

cars.reverse() # 将列表内容反转,再次使用将还原
print_list(cars)
