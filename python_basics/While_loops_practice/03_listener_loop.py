# theSum = 0
# x = -1
# while (x != 0):
#     x = int(input("next number to add up (enter 0 if no more numbers): "))
#     theSum = theSum + x

# print(theSum)

# Problem 2 - keep check on items purchased from the and  print their price/item ,
# total price of all items and average price per items"
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price < 0:
            print("Please enter valid price")
        elif price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()


# Problem 3 validating Input get yes or no message

def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == "Y" or answer == "N" :
            valid_input = True
        return answer
response = get_yes_or_no("Do you like coding ? : (Y)-> Yes or (N)-> NO") 
if response == "Y":
    print("Great You will become a great Programer")   
else:
    print("Start with Basics you will starting like it !!")        




