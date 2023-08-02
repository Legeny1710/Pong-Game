from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=0.8)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)



def move_paddle_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def move_paddle_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)



screen.listen()
screen.onkey(key="Up", fun=move_paddle_up)
screen.onkey(key="Down", fun=move_paddle_down)



is_game_on = True
while is_game_on:
    screen.update()










screen.exitonclick()
