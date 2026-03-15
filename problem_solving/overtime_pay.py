# WAP FOR pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# PAY program SHOULD BE using try and except so that your program,
# handles non-numeric input gracefully by printing a message and exiting the program.
# write this program again by defining computepay(hours,rate) function

def computepay(hours,rate):
    if (hours <= 40):
            return hours*rate
    else:
          extra = hours-40
          return rate*extra*1.5 + 40*rate
    
hrs = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))

pay = computepay(hrs,r)    
print ("Pay:",pay)
    





    


  

