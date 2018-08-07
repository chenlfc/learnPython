# # 字典，可爱的字典
# # 一个字典实例
import ex39_hashmap

hashmap = ex39_hashmap

# create a mapping of state to abbreviation
# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Potland'
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Potland')

# print out some cities
print('-' * 10)
print("NY State has: %s" % hashmap.get(cities, 'NY'))
print("OR state has: %s" % hashmap.get(cities, 'OR'))
# print("NY State has: ", cities['NY'])
# print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan'))
print("Florida's abbreviation is: %s" % hashmap.get(states, 'Florida'))
# print("Michigan's abbreviation is: ", states['Michigan'])
# print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan')))
print("Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida')))
# print("Michigan has: ", cities[states['Michigan']])
# print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
hashmap.list(states)
# for state, abbrev in states.items():
#     print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
hashmap.list(cities)
# for abbrev, city in cities.items():
#     print("%s has the city %s" % (abbrev, city))

print('-' * 10)
# safely get a abbreviation by state that might not be there
# state = states.get('Taxas')
state = hashmap.get(states, 'Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)
hashmap.set(cities, 'TX', 'Texas')
hashmap.set(cities, 'TX', 'Texas is a new City')
print("The city for the state 'TX' is: %s" % hashmap.get(cities, 'TX', 'Does Not Exist'))
# city = cities.get('TX', 'Does Not Exist')
# print("The city for the state 'TX' is: %s" % city)
print('-' * 10)
hashmap.list(cities)
hashmap.delete(cities, 'TX')
print('-' * 10)
hashmap.list(cities)