from turtle import Turtle, Screen
import random

colors = ['green', 'black', 'red', 'blue', 'pink', 'purple', 'yellow']
directions = [0,90,180,270]

tim = Turtle()
tim.pensize(10)
tim.speed('fastest')

def random_direction():
    for n in range(100):
        tim.color(random.choice(colors))
        tim.forward(20)
        tim.setheading(random.choice(directions))


random_direction()
screen = Screen()
screen.exitonclick()
