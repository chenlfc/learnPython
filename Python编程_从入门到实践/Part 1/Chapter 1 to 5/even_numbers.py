# create by o.c. 2018/7/19
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# squares.py
squares = [((value ** 2) // 3) for value in range(1, 21)]
# for value in range(1, 11):
#     # square = value ** 2
#     squares.append(value ** 2)

print(squares)
squares.reverse()
print(squares)

print("MIN digits in squares is: ", min(squares))
print("MAX digits in squares is: ", max(squares))
print("SUM digits as squares is: ", sum(squares))
