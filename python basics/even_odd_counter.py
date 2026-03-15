nums = [12, 5, 7, 20, 33, 42]
odd_count = 0
even_count = 0

for value in nums:
    if(value%2==0):
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("even no count:",even_count)
print("odd no count:",odd_count)            