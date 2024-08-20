from turtle import Turtle, Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")
screen.tracer(0)

# set up the dividing line
line = Turtle()
line.penup()
line.ht()
line.teleport(20, 315)
line.color("white")
line.setheading(270)
while line.ycor() > -315:
    line.penup()
    line.forward(10)
    line.pendown()
    line.forward(30)

# initializing paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# getting the paddles to move up and down
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# getting a ball
ball = Ball()

# getting a scoreboard
scoreboard_l = Scoreboard(-100, 200)
scoreboard_r = Scoreboard(100, 200)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.bounce_y()

    # check for bouncing off paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()

    # check for collision with walls
    if ball.check_l_collision():
        scoreboard_l.update_score()
    if ball.check_r_collision():
        scoreboard_r.update_score()













screen.exitonclick()
