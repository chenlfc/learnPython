# 打印，打印：继续复杂的格式化字符输出练习

# 在做调试的时候尽量使用 %r 而不是 %s， 因为他先是的是变量“原始”的数据值
# 他在打印的时候能够重现他代表的对象

# 定义简化字符串变量，用于接收4个任意变量的带入
formatter = "%r %r %r %r"
# formatter = "%s %s %s %s"

# 带入简化字符串变量，输出4个整数
print(formatter % (1, 2, 3, 4))
# 带入简化字符串变量，输出4个短字符串
print(formatter % ("one", "two", "three", "four"))
# 带入简化字符串变量，输出4个bool值
print(formatter % (True, False, False, True))
# 带入简化字符串变量，输出4个简化字符串变量自己的值
print(formatter % (formatter, formatter, formatter, formatter))
# 带入简化字符串变量，输出4段字符串语句
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
