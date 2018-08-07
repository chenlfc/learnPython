# create by o.c. 2018/7/19
# 4-3
for value in range(1, 21):
    print(value)

# 4-4
values = [value for value in range(1, 101)]
print(values)

# 4-5
print("MAX digits in values is ", max(values))
print("MIN digits in values is ", min(values))
print("SUM digits in values is ", sum(values))

# 4-6
odd_numbers = [value for value in range(1, 21, 2)]
for odd_number in odd_numbers:
    print(odd_number)

# 4-7
numbers = []
for value in range(3, 31):
    if value % 3 == 0:
        numbers.append(value)

for number in numbers:
    print(number)
print(numbers)

# 4-8 and 4-9
cubes = [value ** 3 for value in range(1, 11)]
# for value in range(1, 11):
#     cubes.append(value ** 3)

for cube in cubes:
    print(cube)
