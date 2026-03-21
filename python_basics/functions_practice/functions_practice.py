def hello():
    "This is a Function"
    print("hello")
    print("Glad to meet you")


hello()
print("we are there")
hello()

# Function Parameters

def hello2(s): # s - parameter name
    print("Hello " + s)
    print("glad to meet you")
hello2("Yash")  # "Yash" - parameter value
hello2("Siya")  

def hello3(s,n): # this function can take 2 parameter as input
    greeting = "Hello {} ".format(s)
    print(greeting*n)

hello3("Yash",2)
hello3("",1)
hello3("siya",4)
