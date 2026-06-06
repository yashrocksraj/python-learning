# OOP Practice
# Eg 1.

class Student():
    def __init__(self):
        self.name = "Yash"
        self.age = 28
        self.marks = 97
    def show(self):
        print(self.name)
        print(self.age)
        print(self.marks)

# s1 = Student()
# s1.show()

s2 = Student()
s2.name = "Siya"
s2.age = 24
s2.marks = 89
s2.show()

# Eg 2.
# Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. 
# Create an instance method called limbs that, when called, returns the total number of limbs the animal has. 
# To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. 
# Call the limbs method on the spider instance and save the result to the variable name spidlimbs.
class Animal():
    def __init__(self,arms,legs):
        self.arms = arms
        self.legs = legs
    def limbs(self):
        return(self.arms + self.legs)
spider = Animal(4,4)
spidlimbs = spider.limbs()


