import random
from turtle import Turtle, Screen
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#draw overlapping shapes
def draw_shape(numsides):
    angle = 360 / numsides
    for _ in range(numsides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
##triangle
#for i in range (3):
#    tim.forward(100)
#    tim.right(120)

#square
#tim.color('blue')
#for i in range (4):
#    tim.forward(100)
#    tim.right(90)
#
##pentagon
#tim.color('red')
#for i in range (5):
#    tim.forward(100)
#    tim.right(72)

#hexagon
#tim.color('yellow')
#for i in range (6):
#    tim.forward(100)
#    tim.right(60)
#
##heptagon
#tim.color('cyan')
#for i in range (7):
#    tim.forward(100)
#    tim.right(51.5)
##octagon
#tim.color('magenta')
#for i in range (8):
#    tim.forward(100)
#    tim.right(45)
##nonagon
#tim.color('olive')
#for i in range (10):
#    tim.forward(100)
#    tim.right(40)

