import random
from turtle import Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

# Screen listens for events
screen.listen()
screen.onkeypress(player.move_up, "Up")

car = Car()

scoreboard = Scoreboard()

game_on = True

while game_on:

    time.sleep(0.1)
    screen.update()

    # Detect when turtle reaches the upper wall - successful crossing
    if player.ycor() > 300:
        player.reset_position()
        car.level_up()
        scoreboard.increase_level()

    car.create_car()
    car.move_cars()

    # Detect collision with car
    for item in car.all_cars:
        if player.distance(item) < 20:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
