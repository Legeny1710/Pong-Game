from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


pong_ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_paddle_up)
screen.onkey(key="Down", fun=r_paddle.move_paddle_down)

screen.onkey(key="w", fun=l_paddle.move_paddle_up)
screen.onkey(key="s", fun=l_paddle.move_paddle_down)



is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    pong_ball.move()

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    if pong_ball.distance(r_paddle) < 60 and pong_ball.xcor() > 340:
        pong_ball.bounce_x()

    if pong_ball.distance(l_paddle) < 60 and pong_ball.xcor() < -340:
        pong_ball.bounce_x()



screen.exitonclick()
