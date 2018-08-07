# while 循环
# while 循环会一直执行循环，知道它对应的表达式为假时才会停下来
def my_while(j, step=1):
    i = 0
    numbers = []
    print("-" * 40)
    while i < j:
        print("At the top i is %d" % i)
        numbers.append(i)
        i += step
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)
        print(">" * 20)
    print("-" * 40)
    print("The numbers: ")
    for num in numbers:
        print(num)


def my_for(j, step=1):
    numbers = []

    print("=" * 40)
    for i in range(0, j, step):
        print("At the top i is %d" % i)
        numbers.append(i)
        i += step
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)
        print("+" * 20)
    print("=" * 40)
    print("The numbers: ")

    for num in numbers:
        print(num)


my_while(15, 2)
my_for(15, 2)
