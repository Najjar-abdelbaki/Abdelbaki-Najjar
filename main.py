import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

score = Score()


middl = Turtle()
middl.hideturtle()
middl.penup()
middl.color("white")
middl.goto(0, -300)
middl.setheading(90)
while middl.ycor() < 280:
    middl.forward(20)
    middl.penup()
    middl.forward(10)
    middl.pendown()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "s")
screen.onkey(l_paddle.down, "w")


game = True
while game:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.balance_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.balance_x()

    if ball.xcor() > 380 :
        score.left()
        ball.reset_position()

    if ball.xcor() < -380 :
        score.right()
        ball.reset_position()





screen.exitonclick()