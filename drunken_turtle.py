import turtle
import random

turtle.shape('turtle')
while(True):
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(100,100))
    turtle.stamp()

