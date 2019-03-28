import turtle

# print("Hello, world!")
# name = input("What is your name? ")
# print("Hello, " + name + "!")

turtle.color('green', 'blue')
turtle.begin_fill()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()

turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break

turtle.end_fill()

turtle.done()  # 让窗体驻留
 