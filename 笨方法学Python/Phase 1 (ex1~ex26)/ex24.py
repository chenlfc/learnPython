# 更多的练习
print("Let's practice everything.")
print("让我们来实践学习过的内容。")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")
print("你将要知道使用的转义符，换行符和制表符。")

poem = """
\tThe lovely world\t\t\t\t可爱的世界
with logic so firmly planted\t\t\t\t如此坚定的逻辑
cannot discern\t\t\t\t\t\t不能辩驳 \n the needs of love\t\t\t\t\t爱的需要
nor comprehend passion from intuition\t\t\t也不理解来自直觉的激情
and requires an explanation\t\t\t\t需要一个解释
\n\t\t where there is none.\t\t\t没有人的地方
"""

print("-" * 14)
print(poem)
print("-" * 14)

five = 10 - 2 + 3 - 6
print("This should be five（这里应该输出5）: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500 # 软心豆粒糖
    jars = jelly_beans / 1000 # 广口瓶
    crates = jars / 100 # 板条箱
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of（设置了一个起始值）: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))
print("我们有%d个豆子，需要用%d个罐子及%d个板条箱来装他们。" % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way（我们也可以这么做）:")
print("We'd have %d beans, %d jars, %d crates" % secret_formula(start_point))
