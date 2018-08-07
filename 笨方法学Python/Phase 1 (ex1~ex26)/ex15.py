# 读文件
# 从sys包中引入argv功能模块
from sys import argv
# 使用输入参数获取文件名和脚本名称
script, filename = argv
# 定义文件的编码类型
fileEncoding = 'utf-8'
# 使用open命令打开文件
txt = open(filename, encoding=fileEncoding)

# 输出文件名及其内容
print("Here's your file %r: " % filename)
print(txt.read())
# 关闭文件
txt.close()

# 提示输入另一个文件名
#print("Type the filename again: ")
file_again = input("Type the filename again: > ")
# 打开新的文件并输出它的内容
txt_again = open(file_again, encoding=fileEncoding)
print(txt_again.read())
# 关闭文件
txt_again.close()
