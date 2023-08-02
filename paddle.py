from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, cord):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=0.8)
        self.color("white")
        self.penup()
        self.goto(cord)

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


