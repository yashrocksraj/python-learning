# Problem 1
# Write a while loop that is initialized at 0 and stops at 15.
# If the counter is an even number,append the counter to a list called eve_nums 
count = 0 
eve_nums = []
while count <= 15:
    if count % 2 == 0:
        eve_nums.append(count)
    count += 1
print(eve_nums)        
