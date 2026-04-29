# Problem 1
# Below, we have provided a list of lists that contain information about people. 
# Write code to create a new list that contains every person’s last name, and save that list as last_names.
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []
for entertainer in info:
    last_names.append(entertainer[1])
print(last_names)    

# Problem 2
# Below, we have provided a list of lists named L. 
# Use nested iteration to save every string containing “b” into a new list named b_strings.
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings =[]
for lst in L:
    for word in lst:
        if 'b' in word:
            b_strings.append(word)
print(b_strings)            
