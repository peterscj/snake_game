## Snake Game

from turtle import Screen, Turtle
import time
from snake import Snake
from Food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(5)


# Initalize class instances
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

# Key Bindings
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
    snake.head.forward(20)

    # Create new food if there is a collision between
    # snake and food. Then update scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()


screen.exitonclick()