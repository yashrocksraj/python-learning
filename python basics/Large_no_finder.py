user_input = input("Enter nos separated by space:")
nums = user_input.split()
numbers=[]
for value in nums:
    numbers.append(int(value))

large = numbers[0]
for i in numbers:
    if i > large:
        large = i
print("largest no:",large)        


   