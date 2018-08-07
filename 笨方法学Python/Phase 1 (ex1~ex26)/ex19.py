# 函数和变量

# # 定义一个包含2个参数的函数
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     # 输出以第一个参数为内容的一段提示
#     print("You have %d cheeses!" % cheese_count)
#     # 输出以第二个参数为内容的一段提示
#     print("You have %d boxes of crackers!" % boxes_of_crackers)
#     print("Man that's enough for a party!")  # 输出提示
#     print("Get a blanket.\n")  # 输出提示


# # 输出一段提示
# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 20)  # 调用函数，参数为2个整数
# # 输出一段提示
# print("OR, we can use variables from our script:")
# amount_of_cheese = 10  # 定义一个变量
# amount_of_crackers = 50  # 定义另一个变量
# # 调用函数，将变量用作参数传递给函数
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# # 输出一段提示
# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)  # 调用函数，直接传递算式结果
# # 输出一段提示
# print("And we can combine the two, variables and math:")
# # 调用函数传递计算后的参数
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
from sys import argv


def my_function(name, old):
    print("Hi %s , you're %d years old." % (name, old))


# # 1、直接给值参数
# my_function("Jack", 32)
# # 2、给变量赋值后，将变量用作参数
# name = "Stven"
# old = 24
# my_function(name, old)
# # 3、参数变量计算后，作为参数
# my_function(name + "A", old + 30)
# # 4、在传递参数的位置直接用计算的方式
# my_function("Oven" + "Chen", 2018 - 1977)
# # 5、提示用户输入参数值
# my_function(input("Your name is : "), int(input("How old are you ? ")))
# # 6、提示用户输入参数并进行计算后传递
# my_function(input("Your name is :") + ".D.",
#             int(input("How old are you? ")) + 10)
# # 7、将用户输入的值存入变量后，作为参数
# new_name = input("The name is: ")
# new_old = int(input("Old is: "))
# my_function(new_name, new_old)
# # 8、接包argv赋予变量后，作为参数
# file_name, argv_name, argv_old = argv
# my_function(argv_name, int(argv_old))
# # 9、直接将argv的值作为参数
# my_function(argv[1], int(argv[2]))
# 10、从文件读入文本，作为参数
my_file = open("ex19_sample.txt", encoding="utf-8")
my_arg = my_file.readlines()
my_name = my_arg[0]
my_old = int(my_arg[1])
my_function(my_name.replace("\n", "", -1), my_old)
my_file.close()
