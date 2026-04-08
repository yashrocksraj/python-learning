# Problem 1
# Sort the following dictionary based on the keys so that they are sorted a to z.
# Assign the resulting value to the variable sorted_keys.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
sorted_keys = sorted(dictionary)
print(sorted_keys)

# Problem 2
# Sort the following dictionary’s keys based on the value from highest to lowest. 
# Assign the resulting value to the variable sorted_values.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
sorted_values = sorted(dictionary,key=lambda x:dictionary[x],reverse=True)
print(sorted_values)
