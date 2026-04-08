# Problem 1
# Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted
lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst,reverse=True)
print(lst_sorted)

# Problem 2
# Sort the list by using second letter without using lamba fucntion
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def second_let(a):
    return a[1]
sorted_by_second_let = sorted(ex_lst,key = second_let)
print(sorted_by_second_let)

# Problem 3
# Write a function called last_char that takes a string as input, and returns only its last character. 
# Use this function to sort the list nums by the last digit of each number, from highest to lowest, 
# and save this as a new list called nums_sorted.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(a):
    return a[len(a)-1]

nums_sorted = sorted(nums , reverse=True, key=last_char)
print(nums_sorted)

# Problem 4 
# Rewrite above program using lambda function.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda =sorted(nums , reverse=True, key=lambda x : x[len(x)-1])
print(nums_sorted)