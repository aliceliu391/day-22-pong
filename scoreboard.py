from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(x, y)
        self.write(arg=f"{self.score}", align="left", font=('Courier', 80, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", align="left", font=('Courier', 80, 'normal'))
