## Snake Game

from turtle import Screen, Turtle

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
    for i in range(3):
        snake_piece = new_snake_part()
        snake_piece.setposition(new_start, 0)
        new_start = snake_piece.xcor() - 20
    return snake



screen.exitonclick()