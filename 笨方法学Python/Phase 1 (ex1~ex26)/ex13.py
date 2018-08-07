# 参数，解包，变量
# 将Python的功能模块加入自己的脚本的方法
from sys import argv

#script, first, second, third =argv

# print("The script is called: ", script)
# print("Your first variable is: ", first)
# print("Your second variable is: ", second)
# print("Your third variable is: ", third)
for arg in argv:
    print("Your variable is: ", arg, end = ' ')
    print("Index is: ",argv.index(arg))

