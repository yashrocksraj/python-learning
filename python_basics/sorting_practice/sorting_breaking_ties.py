# Problem 1
# Reverse fruits name alphabaticaly

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

# Problem 2
# Sort weather for different cities 
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp'])) 

# Problem 3
# Sort states on the basis of the length of the first city name.
# states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
#           "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
#           "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}
# print(sorted(states,key=lambda state:len(states[state][0])))

# Problem 4
# Sort above States on the basis of cities with more names with letter "S".
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}
def count_cities_S(cities_list):
    city_count = 0
    for city in cities_list:
        if city[0] == 'S':
            city_count += 1 
    return city_count
city_sorted_s = sorted(states,key=lambda state :count_cities_S(states[state]) ) 
print(city_sorted_s)   

