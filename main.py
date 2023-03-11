## Snake Game

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

def new_snake_part():
    snake_part = Turtle(shape="square")
    snake_part.color("white")
    return snake_part

def gen_initial_snake():
    new_start=0
    segments = list()
    for i in range(3):
        snake_piece = new_snake_part()
        snake_piece.penup()
        screen.tracer(5)
        snake_piece.setposition(new_start, 0)
        new_start = snake_piece.xcor() - 20
        segments.append(snake_piece)
    return segments

snake = gen_initial_snake()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake)-1, 0,-1):
        # Grab x & y coordinates of previous snake segment and have it current one go there
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num-1].ycor()
        snake[seg_num].goto(new_x, new_y)

    snake[0].forward(20)


screen.exitonclick()