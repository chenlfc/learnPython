# 分支和函数
from sys import exit


def ptline():
    print("-" * 60)


def gold_room():
    ptline()
    print("This room is full of gold. How much do you take?")

    choice = input("(Please enter some number for buy...) > ")
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    ptline()
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(
            "(take honey or taunt bear or open door or other...) > ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print(
                "The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got to idea what that means.")


def cthulhu_room():
    ptline()
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("(flee or head or other...) > ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was testy!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    ptline()
    exit(0)


def start():
    ptline()
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("(left or right) > ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
