# Problem 1:
# Print numbers from 1 to 20, skip multiples of 3.

x = 1 
while x <= 20:
    if x%3 == 0:
        x+= 1
        continue
    
    
    print(x) 
    x += 1
#-----------------------------------#


# Problem 2:
# Take input into loop if input = 'exit' -> stop ,
# if empty -> skip

while True:
    x = str(input("enter :")).lower()
    if x == '':
        continue
    elif x == 'exit':
        break

print("loop ends")