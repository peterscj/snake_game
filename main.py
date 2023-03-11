## Snake Game

from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(5)


snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
snake.connect_snake_part(4,0)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake.segments)-1, 0,-1):
        # Grab x & y coordinates of previous snake segment
        # and have it current one go there
        new_x = snake.segments[seg_num-1].xcor()
        new_y = snake.segments[seg_num-1].ycor()
        snake.segments[seg_num].goto(new_x, new_y)
    snake.segments[0].forward(20)


screen.exitonclick()