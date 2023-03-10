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
    for segment in snake:
        segment.forward(20)


# TODO: Add time library to control how quickly snake is moving, update how the screen is updating

screen.exitonclick()