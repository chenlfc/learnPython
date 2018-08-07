# 字符串和文本
# 给变量赋值一个字符串，并从外部带入一个整数到字符串中
x = "There are %d types of people." % 10
# 定义字符串变量
binary = "binary"
# 定义字符串变量，用以简化输入
do_not = "don't"
# 将2个简化字符串输入的字符串变量带入字符串，并赋予一个新的变量
y = "Those who know %s and those who %s." % (binary, do_not)

# 输出字符串
print(x)
print(y)

# 用%r带入变量的内容并输出字符串
print("I said: %r." % x)
# 用%s带入自u穿的内容并输出字符串
print("I also said: '%s'." % y)

# 定义一个bool变量
hilarious = False
# 定义一个能接受参数的字符串变量
joke_evaluation = "Isn't that joke so funny?! %r"
# 将bool值变量带入能接受参数的字符串变量，并输出
print(joke_evaluation % hilarious)
# 定义两个个简化字符串变量
w = "This is the left side of..."
e = "a string with a right side."
# 将两个简化字符串变量合并输出
print(w+e)
