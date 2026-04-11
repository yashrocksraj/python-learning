nested1 = [['a','b','c'],['d','e'],['f','g','h']]
nested1[0].append('z')
print(nested1)

def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))

# Problem 1
# Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name idx1
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
idx1 = animals[1][0]
print(idx1)

# Problem 2
# Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
plant = data[7][0][0]
print(plant)