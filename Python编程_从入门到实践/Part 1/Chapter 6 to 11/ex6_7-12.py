# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/22
from _for_ex import pt_title

pt_title('EX 6 - 7')
people_0 = {
    'first_name': 'frank',
    'last_name': 'li',
    'age': 24,
    'city': 'Shanghai',
}
people_1 = {
    'first_name': 'jack',
    'last_name': 'huang',
    'age': 28,
    'city': 'beijing',
}
peoples = [people_0, people_1]

for people in peoples:
    full_name = people['first_name'] + ' ' + people['last_name']
    age = people['age']
    city = people['city']
    print(full_name.title() + "'s age is " + str(age) + ", living in " +
          city.title())

pt_title('EX 6 - 8')
pet_tom = {
    'name': 'tom',
    'type': 'dog',
    'host': 'jack',
}
pet_marth = {
    'name': 'marth',
    'type': 'cat',
    'host': 'lee',
}
pets = [pet_tom, pet_marth]
for pet in pets:
    pet_name = pet['name']
    pet_type = pet['type']
    pet_host = pet['host']
    print(pet_host.title() + "'s pet " + pet_name.title() + " is " +
          pet_type.title() + ".")

pt_title('EX 6 - 9')
favorite_places = {
    'tom': ['shanghai', 'beijing', 'wuhan'],
    'lee': ['xinjiang', 'suzhou', 'zhujian'],
    'jack': ['menggu', 'heilongjiang', 'qingdao'],
}
for name, places in favorite_places.items():
    print(name.title() + " like places is:")
    for place in places:
        print("\t" + place.title())

pt_title('EX 6 - 10')
like_number = {
    'lisa': [13, 14, 2, 1],
    'sarua': [4, 3, 1],
    'jake': [11, 22, 33, 44, 55],
    'tom': [4, 8, 7],
    'frank': [11],
}
for name, numbers in like_number.items():
    print(name.title() + " like numbers is:")
    for number in numbers:
        print("\t" + str(number), end='')
    print()

pt_title('EX 6 - 11')
cities = {
    'shanghai': {
        'country': 'china',
        'population': 1.48,
        'fact': 'mo du',
    },
    'beijing': {
        'country': 'china',
        'population': 2.44,
        'fact': 'di du',
    },
    'guangzhou': {
        'country': 'china',
        'population': 1.44,
        'fact': 'xing du',
    },
    'xian': {
        'country': 'china',
        'population': 1.24,
        'fact': 'fei du',
    },
    'nanjing': {
        'country': 'china',
        'population': 2.04,
        'fact': 'jiu du',
    },
}
for city, infos in cities.items():
    print("The city " + city.title() + ":")
    print("\tCountry: " + infos['country'].upper())
    print("\tPopulation: " + str(infos['population']))
    print("\tFact: " + infos['fact'].title())
