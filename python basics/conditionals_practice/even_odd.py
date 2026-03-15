num = input("Enter number:")
try: 
    b = int(num)
    if(b%2==0):
     print("even")
    else:
     print("odd")   
except:
  b=-1
  print("Error: please enter no ")      