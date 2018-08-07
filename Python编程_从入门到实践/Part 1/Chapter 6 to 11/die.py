from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        die = randint(1, self.sides)
        print(str(die))


my_die = Die(8)
my_die.roll_die()


def print_die(p_die):
    i = 0
    print("Die is %d" % p_die.sides)
    print("-" * 20)
    while i < 10:
        i += 1
        print("%d --> " % i, end='')
        p_die.roll_die()
    print("-" * 20)


six_die = Die()
print_die(six_die)
ten_die = Die(10)
print_die(ten_die)
twenty_die = Die(20)
print_die(twenty_die)
