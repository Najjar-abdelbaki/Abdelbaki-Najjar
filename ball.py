from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.ball_speed = 0.1


    def move(self):
            x = self.xcor() + self.x
            y = self.ycor() + self.y
            self.goto(x, y)


    def balance_y(self):
        self.y *= -1
        #self.move()

    def balance_x(self):
        self.x *= -1
        self.ball_speed *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.balance_x()
        self.ball_speed = 0.1
