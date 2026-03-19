
# Problem 1
# Linear search Target = 2

# arr = [4,7,2,9,5]
# target = 2
# for i in arr:
#     if i == target:
#         print(i)
#     else:
#         continue    

# Target 10
# found = False
# target = 10
# arr = [4,7,2,9,5]  
# for i in range(len(arr)):
#     if arr[i]== target:
#         print(i)
#         found = True  
# if not found:
#     print("not found")

# Find first occurence target = 9 , 10
# arr = [4,7,2,9,5]
# target = 9
# found = False
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found at index:",i)
#         found = True
#         break
    
# if not found:
#     print("not found")
#------------------#-------------------#
# Problem 2        
# Find Second Smallest

# arr = [3,7,2,9,5]
# smallest = float('inf') 
# second_smallest = float("inf")
# for num in arr:
#     if num < smallest:
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest and num != smallest:
#         second_smallest = num
# print(second_smallest) 

#------------------#-------------------#

# Problem 3 
# Find second Largest
# arr = [3,7,2,9,5]
# largest = float('-inf') 
# second_largest = float("-inf")
# for num in arr:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num < second_largest and num != largest:
#        second_largestt = num
# print(second_largest)
#------------------#-------------------#

# Problem 4(twist)
# Find Second smallest
arr = [2,2,2] 
smallest = float('inf')
second_smallest = float('inf')
for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
if second_smallest == float('inf'):
    print("No second Smallest")
else:            
  print(second_smallest) 
#------------------#-------------------#


   