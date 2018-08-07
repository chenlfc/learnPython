# 循环和列表

# hairs = ['brown', 'blond', 'red']
# eyes = ['brown', 'blue', 'green']
# weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'paricots']
change = [1, 'pennices', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# 第一种使用列表的for循环
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
# 我们只能通过使用%r来输出混合列表的内容，因为不知道列表的内容
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
# 在这里可以将[]直接更换为range()函数，
# 不过这里改变了elements的类型，
# 这里的elements变成了函数range(0, 16, 2)的别名
elements = range(0, 16, 2)

# then use the range function to do 0 to 5 counts
for i in elements:
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    # elements.append(i)
