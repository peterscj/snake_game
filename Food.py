from turtle import Turtle
import random

class Food(Turtle):
    """
    Food class which inherits the Turtle class. Creates the food
    pieces for the snake and places them in random spots on the screen
    following collisions with the head of the snake.
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Generate new food at random location, to be used after there is
        a collision with the snake.
        :return:
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)