# 函数的返回值
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

mywhat = divide(iq, 2)
mywhat = multiply(weight, mywhat)
mywhat = subtract(height, mywhat)
mywhat = add(age, mywhat)

print("This is my: ", mywhat, "I Can do it by computer!")

newwhat = divide(34, 100)
newwhat = add(24, newwhat)
newwhat = subtract(newwhat, 1023)

print(" 24 + 34 / 100 - 1023 = %r " % newwhat)


def my_formula(a, b, c, d):
    print("This function running is : %d + %d / %d - %d" % (
        a, b, c, d
    ))
    return a + b / c - d


print("Now test my_formula function!")
print(my_formula(24, 34, 100, 1023))
