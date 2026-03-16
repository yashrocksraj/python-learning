# Problem 1
# Find Second largest no.
arr = [4,7,2,9,5]
largest_num = arr[0]
second_largest_num = float('-inf')
for num in arr:
    if(num > largest_num ):
        second_largest_num = largest_num
        largest_num = num
    elif (num > second_largest_num and num != largest_num):
        second_largest_num = num
print("second largest num :",second_largest_num)            