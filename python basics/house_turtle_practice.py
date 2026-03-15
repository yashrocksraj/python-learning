import turtle
import math
distance = math.sqrt(60*60/2)
wn = turtle.Screen()
house = turtle.Turtle()
house.color("green")
house.pensize(8)
house.speed(0)
for i in range(4):
    house.forward(60)
    house.left(90)
house.left(90)
house.forward(60) 
house.right(45)
house.forward(distance)
house.right(90)   
house.forward(distance)
house.right(45)
house.forward(60)
# small gate inside house
house.right(90)
house.forward(20)
house.pensize(5)
house.color("black")
house.right(90)
house.forward(30)
house.left(90)
house.forward(20)
house.left(90)
house.forward(30)
house.hideturtle()


wn.exitonclick()
