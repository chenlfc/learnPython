# 读写文件
# close --关闭文件
# read --读取文件内容
# readline --读取文本文件中的一行
# truncate --清空文件
# write(‘stuff') --将suff写入文件
from sys import argv  # 从sys包中引入argv功能模块

script, filename = argv  # 把外部参数存入变量

print("We're going to erase %r," % filename)
print("If you don't want that, hit (NO).")
print("If you do want that, hit (YES).")

tc = input("?")  # 提示输入

print("Opening the file...")
target = open(filename, 'a', encoding='utf-8')  # 打开文件

if tc == 'YES':
    print("truncating the file. Goodbye!")
    target.truncate()  # 清空文件中的内容

print("Now I'm going to ask you for three lines.")
# 获取三行文本
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")

# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')
# target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
target.write("%s\n%s\n%s\n" % (
    line1, line2, line3
))

print("And finally, we close it.")
target.close()
