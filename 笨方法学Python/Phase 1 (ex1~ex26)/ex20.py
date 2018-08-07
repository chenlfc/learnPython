# 函数和文件
from sys import argv  # 从sys包中引入argv功能模块

script, input_file = argv  # 读取参数到变量


# 自定义函数，参数是已经打开的文件。输出文件的所有内容
def print_all(f):
    print(f.read())


# 自定义函数，将参数指定的文件指针移动到最前面
def rewind(f):
    f.seek(0)


# 自定义函数，参数为要输出的行数及已打开的文件
def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')


current_file = open(input_file)  # 定义变量用于存储打开的文件

print("First let's print the whole file:")  # 输出一行提示

print_all(current_file)  # 调用自定义函数，输出文件的所有内容

print("Now let's rewind, kind of like a tape.")  # 输出一行提示

rewind(current_file)  # 调用自定义函数，移动文件指针至起始处

print("Let's print three lines:")  # 输出一行提示

current_line = 1  # 定义变量，存储要输出的行号
# 调用自定义函数，输出指定行号的内容
print_a_line(current_line, current_file)
# 行号递增
# 调用自定义函数，输出指定行号的内容
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
# 行号递增
# 调用自定义函数，输出指定行号的内容
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
# 行号递增
# 调用自定义函数，输出指定行号的内容
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

current_file.seek(0)
for txt in current_file.readlines():
    print(txt)

