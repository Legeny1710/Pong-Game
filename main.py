from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score_board import  ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

screen.tracer(0)

game_over = Turtle()
game_over.color("white")
game_over.penup()
game_over.hideturtle()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


pong_ball = Ball()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_paddle_up)
screen.onkey(key="Down", fun=r_paddle.move_paddle_down)

screen.onkey(key="w", fun=l_paddle.move_paddle_up)
screen.onkey(key="s", fun=l_paddle.move_paddle_down)



is_game_on = True
while is_game_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    if pong_ball.distance(r_paddle) < 60 and pong_ball.xcor() > 340:
        pong_ball.bounce_x()

    if pong_ball.distance(l_paddle) < 60 and pong_ball.xcor() < -340:
        pong_ball.bounce_x()

    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreBoard.l_point()

    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreBoard.r_point()

    if scoreBoard.r_score == 5 or scoreBoard.l_score == 5:
        is_game_on = False
        game_over.goto(0, 0)
        game_over.write("Game is Over!", align="center", font=("Courier", 60, "normal"))
        if scoreBoard.r_score == 5:
            game_over.goto(0, 100)
            game_over.write("Player on the RIGHT wins!", align="center", font=("Courier", 30, "normal"))
        elif scoreBoard.l_score == 5:
            game_over.goto(0, 100)
            game_over.write("Player on the LEFT wins!", align="center", font=("Courier", 30, "normal"))





screen.exitonclick()
