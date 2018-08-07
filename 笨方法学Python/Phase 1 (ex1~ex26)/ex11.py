# 提问
# print("How old are you?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weigh?", end=' ')
# weigh = input()

# print("So, you're %r old, %r tall and %r heavy." % (
#     age, height, weigh
# ))

my_age = int(input("你几岁了? "))
my_height = int(input("你有多高(cm)? "))
my_weigh = int(input("你有多重(kg)? "))

print("好的，你的年龄是%r岁、身高是%r(cm)、体重是%r(kg)。" % (
    my_age, my_height, my_weigh
))
