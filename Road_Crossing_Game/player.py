from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 290


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

