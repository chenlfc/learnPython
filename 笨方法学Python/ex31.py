# 做出决定
print("You enter a dark room with two doors. Do you go through door #1 or door #2?")
print("当你醒来的时候发现自己在一间伸手不见五指的房间里，只有两扇不知通往哪里的门。你选择进哪扇门？")

door = input("请选择进入哪扇门(输入1 或者 2) > ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("门缓慢地打开了...你发现了一头正在吃奶酪蛋糕的熊。接下去你要怎么做呢？")
    print("1. 拿走蛋糕")
    print("2. 大声尖叫")

    bear = input("请选择输入(1 或者 2) > ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
        print("熊一口把你的脸给咬了下来。你的选择真棒！")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
        print("熊一口把你的腿给咬了下来，津津有味地吃着。你的选择真棒！")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)
        print("好的，你做了个另类的选择%s。把熊吓跑了。" % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    print("你注视着克苏鲁的眼睛就像注视着无尽的深渊。")
    print("1. 蓝莓")
    print("2. 黄色晾衣夹")
    print("3. 明白旋转叫喊的旋律")

    insanity = input("请输入你的选择(1 或者 2 或者 3) > ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of ello. Good job!")
        print("你靠着果冻活了下来。好样的！")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
        print("精神错乱的你把自己的眼睛弄瞎了。呃...这选择真棒！")
else:
    print("You stumble around and fall on a knife and die. Good job!")
    print("你跌跌撞撞，不小心摔倒时被刀给扎死了。这选择...真棒！")
