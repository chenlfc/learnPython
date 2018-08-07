# 那是什么？
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I]m \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

n = 1
while n < 100000:
    for i in ["/", "-", "|", "\\", "|"]:        
        print("%s\r" % i + "%d" % ((n * 0.001) + 1) + "%", end="")
    n = n + 1
    if (n % 100)==0:
        print(chr(9608) * (n//5000), end='')
        # print(chr(9608) * (n//100), end='')
print(' \r')
