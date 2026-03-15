def get_numbers(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print("please enter a valid number")

a = get_numbers("Enter no 1:")
b = get_numbers("Enter no 2:")
c = get_numbers("Enter no 3:")
if(a>b and a>c):
    print("Largest =",a)
elif(b>a and b>c):
    print("Largest =",b)  
else:
    print("Largest =",c)      


