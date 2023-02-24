import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

    # Detect win
    if player.win():
        player.start()
        cars.speed_up()
        level.level_up()


screen.exitonclick()
