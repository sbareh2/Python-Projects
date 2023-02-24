from turtle import Turtle

start = (0, -280)
move_dist = 10
finishline_y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)

    def up(self):
        self.forward(move_dist)

    def start(self):
        self.goto(start)

    def win(self):
        if self.ycor() > finishline_y:
            return True
        else:
            return False



