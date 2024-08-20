from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.color("white")
        self.xspeed = 7
        self.yspeed = 7
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.xspeed
        new_y = self.ycor() + self.yspeed

        self.goto(new_x, new_y)

    def bounce_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.yspeed *= -1

    def bounce_x(self):
        self.xspeed *= -1
        self.move_speed *= 0.9

    def check_l_collision(self):
        if self.xcor() > 380:
            self.reset_position()
            return True

    def check_r_collision(self):
        if self.xcor() < -380:
            self.reset_position()
            return True

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()
