# Problem 1
# Reverse array using Two pointers

def reverse_arr(arr:list[int]):
    left = 0
    right = len(arr) -1
    while left < right:
        arr[left] , arr[right]  = arr[right],arr[left]
        left += 1
        right -= 1
    return arr  
  
lst=[1,2,3,4,5]
print(reverse_arr(lst))
#---------------#--------------#

# Problem 2
# Check whether array is Palindrome or not

def palindrome(nums:list[int]):
    left = 0
    right= len(nums) - 1
    while left < right:
        if nums[left] != nums[right]:
           return False
        left += 1
        right -= 1
    return True

arr1 = [1,2,3,2,1]
print(palindrome(arr1))
#---------------#--------------#

# Problem 3
# Check for Pair Sum
def pair_sum(nums:list[int],target:int):
    left = 0
    right = len(nums)-1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return nums[left],nums[right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return None
lst1 = [1,2,3,4,6]
result = pair_sum(lst1,6) 
if result:
    print("Pair found:",result)
else:
    print("No Pair found")    
#---------------#--------------#

           
      
