# Problem 1
# Find the largest element in the array

arr = [4,7,2,9,5]
largest_num =arr[0]
for num in arr:
    if num > largest_num:
        largest_num = num
print(largest_num)        
#------------------------#
# Problem 2
# Find the Smallest element in the array

arr = [8,3,6,1,9]
smallest_num = arr[0]
for num in arr:
    if num < smallest_num:
        smallest_num = num
print(smallest_num)        
#------------------------#
# Problem 3
# Find the sum of all elements in the array

arr = [1,2,3,4,5]
total_sum = 0
for num in arr:
    total_sum += num
print(total_sum)    
#------------------------#
# Problem 4
# Count how many even numbers exist in the array

arr = [1,2,3,4,6,7,8]
even_no_count = 0
for num in arr:
    if num%2 == 0:
        even_no_count += 1
print(even_no_count) 
#------------------------#       