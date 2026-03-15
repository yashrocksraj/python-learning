import turtle
wn = turtle.Screen()
wn.bgcolor("black")
yash = turtle.Turtle()
yash.pensize(7)
yash.color("red")
yash.speed(5)
print(yash.speed())
# yash.down()
yash.shape("turtle")
# yash.begin_poly()
for i in range(5):
    yash.forward(60)
    yash.stamp()
    yash.left(72)
# yash.end_poly() 
# pentagon = yash.get_poly   
# print(pentagon)
wn.exitonclick()  


