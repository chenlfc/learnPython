def collatz(number):
    if (number % 2) == 0:
        return number // 2
    else:
        return 3 * number + 1


print('Please enter a number:')
number = 0
while True:
    try:
        if number == 0:
            number = int(input())
        else:
            number = collatz(number)
            print(str(number))
            if number == 1:
                break
    except ValueError:
        print('Please enter a number!')
