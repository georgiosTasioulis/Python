from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
# set screen background colour to black
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# animation is turned off, screen must be updated manually
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()

screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    # manually update the screen in while loop as tracer is 0
    screen.update()

    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # Detect ball crossing right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect ball crossing left wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()
