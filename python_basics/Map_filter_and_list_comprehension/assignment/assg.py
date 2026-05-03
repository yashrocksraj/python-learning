# Ques 1.
# Write code that uses map to assign to the variable map_testing all the elements from lst_check, 
# prepending the string "Fruit: " to the beginning of each element. 
# Note: be sure to use list to convert the result from map into a list.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = list(map(lambda fruit:"Fruit: " + fruit,lst_check))
print(map_testing)

assert 'Fruit: plums' in map_testing
assert 'Fruit: kiwi' in map_testing

# Ques 2.
# Below, we have provided a list of strings called countries. 
# Use filter to produce a list called b_countries that only contains the strings from countries that begin with 'B'. 
# Note: be sure to use list to convert the result from filter into a list.

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = list(filter(lambda country : 'B' == country[0],countries))
print(b_countries)

# Ques 3.
# Below, we have provided a list of tuples that contain the names of Game of Thrones characters. 
# The first item in each tuple is their last (family) name. The second item is their first (given) name. 
# Using a list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_name = [name[1] for name in people]
print(first_name)

# Ques 4.
# Use a list comprehension to create a list called lst2 that "doubles" each element in the list, lst. 
# Use * 2 to "double" numbers (5 * 2 == 10), strings ("xyz" * 2 == "xyzxyz"), and lists (['a', 'b'] * 2 == ['a', 'b', 'a', 'b']).
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [item*2 for item in lst ]
print(lst2)

# Ques 4.
# Below, we have provided a list of tuples that contain students' names and their final grades in PYTHON 101. 
# Using a list comprehension, create a new list passed that contains the names of students 
# who passed the class (had a final grade of 70 or greater). 
# passed should be a list of strings (names without final grades) in the same order as students.
students = [('Tamara', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [(name) for name,grade in students if grade >= 70]
print(passed)

# Ques 5.
# Write code using zip and filter so that these lists (l1 and l2) are combined into one big list of pairs 
# and assigned to the variable opposites if both elements of the pair are longer than 3 characters. 
# Note: be sure to use list to convert the result into a list.
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = list(filter(lambda x : (len(x[0])>3 and len(x[1])>3),zip(l1,l2)))
print(opposites)

# Ques 5.
# Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. 
# From this list, create a new list called endangered that contains the names of species whose populations are below 2500.
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = list(zip(species,population))   # Replace "None" with an expression that makes pop_info a list of tuples (each first item is a species string and each second item is a number, for that species' population)
endangered = [(specie) for (specie,pop) in pop_info if pop < 2500] # Replace "None" with an expression that makes `endangered` a list of strings (species whose population is below 2500)
print(pop_info)
print(endangered)
