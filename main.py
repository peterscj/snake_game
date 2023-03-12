## Snake Game

"""
Welcome to the snake game! When started, the player controls a "snake"
and the objective is to eat as much "food" as you can WITHOUT hitting the
walls or any part of the body of the snake. As you successfully consume food,
the snake's body will lengthen, thereby increasing the difficulty of not
hitting the body.

The main file stores game text, with the snake body, food pieces, and
score tracking maintained as classes in separate files. Visuals used from
the Turtle library.

"""

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

    # Update score, snake length, and new food piece after each time the snake eats something
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collisions with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()

    # Detect if snake collides with tail, slicing excludes the head
    # from triggering automatic game over
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 15:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()