# QS.1 Even Or Odd

# number = 37
# if ( number % 2 == 0):
#     print("Even No")
# else:
#     print("Odd No")    


# QS.2 Q2 — Largest of Two Numbers

# a = 15
# b = 27
# if(a > b):
#     print("A is largest")
# else:
#     print("B is largest")    



# QS.3 — Largest of Three Numbers    

# a = 10
# b = 45
# c = 32

# if(a > b and a>c):
#     print("A is largest")
# elif(b > a and b>c) :
#     print("B is largest")
# else:
#     print("Cis largest")        


# QS.4 — Leap Year Checker

# year = 2024
# if(year % 4 == 0):
#     print("Leap Year")
# else:
#     print("Normal Year")    


# QS.5 — Grade Calculator

# marks = int(input("Marks:"))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")    
# elif marks >= 60:
#     print("Grade C")    
# elif marks >= 45:
#      print("Grade D")    
# elif marks < 40:
#      print("Grade E")        

# QS.6 — Password Strength Check

password = str(input("password:"))
has_upper = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_digit:
    print("Strong Password")
else:
    print("Weak Password")

