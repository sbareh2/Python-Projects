import turtle
from turtle import Turtle, Screen
import random
colors = ['green', 'black', 'red', 'blue', 'pink', 'purple', 'yellow']

tim = Turtle()
tim.speed('fastest')
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for n in range (100):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 5)





screen = Screen()
screen.exitonclick()
