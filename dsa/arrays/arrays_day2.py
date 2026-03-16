# Problem 1
# Find Second largest no.
# arr = [4,7,2,9,5]
# largest_num = arr[0]
# second_largest_num = float('-inf')
# for num in arr:
#     if(num > largest_num ):
#         second_largest_num = largest_num
#         largest_num = num
#     elif (num > second_largest_num and num != largest_num):
#         second_largest_num = num
# print("second largest num :",second_largest_num)            
# #------------------------#

# Problem 2
# Reverse an Array
# arr = [1,2,3,4,5]
# rev_arr = []
# for i in range(len(arr)-1,-1,-1):
#     rev_arr.append(arr[i])
# print(rev_arr)    
# #------------------------#

# Problem 3
# Count nums greater than 5

arr = [2,8,3,10,6]
nums_greater_5 = 0
for num in arr:
    if num > 5:
      nums_greater_5 += 1
print(nums_greater_5)   