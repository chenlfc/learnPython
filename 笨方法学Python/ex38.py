# 列表操作

'''
将语句拆分为列表 split
将列表合并为语句 join
'''

# class Thing(object):
#     def test(self, hi):
#         print(hi)

# a = Thing()
# a.test("Hello")

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song',
              'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()  # 取出列表中的最后一个元素
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool!
print('#'.join(stuff[3:5]))  # super stellar!
