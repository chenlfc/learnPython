# 访问列表元素
from cardinal_num_to_ordinal_num import cardinalToOrdinal


def show_animals(animals, cardinal_number):
    '''根据参数中的cardinal_number（基数）转换成相对应的序数并结合参数中的列表animals输出对于基数、序数的列表值'''
    print("The %s animal is at %d and is a %s" %
          (cardinalToOrdinal(cardinal_number), cardinal_number, animals[cardinal_number]))


animals = ['bear，熊', 'python，巨蟒', 'peacock，孔雀',
           'kangaroo，袋鼠', 'whale，鲸鱼', 'platypus，鸭嘴兽']

i = 0
print("The animals is: ")
for animal in animals:
    print("Animals[%d] is : %s" % (i, animal))
    i += 1

print("The animal at 1.")
show_animals(animals, 1)
print("The third (3rd) animal.")
show_animals(animals, 3 - 1)
print("The animal at 3.")
show_animals(animals, 3)
print("The fifth (5th) animal.")
show_animals(animals, 5 - 1)
print("The animal at 2.")
show_animals(animals, 2)
print("The sixth (6th) animal")
show_animals(animals, 6-1)
print("The animal at 4.")
show_animals(animals, 4)
