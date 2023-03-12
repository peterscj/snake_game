from turtle import Screen, Turtle
import time

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = list()
        self.new_snake_part()
        self.head = self.segments[0]

    def new_snake_part(self):
        """
        Creates a new segment of the snake and appends to the list
        for easy tracking
        """
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        self.segments.append(segment)
    def connect_snake_part(self,seg_count,new_start):
        """
        Add new segment to the snake
        :param seg_count:  segments to add
        :param new_start: x-coordinate to generate segment at
        :return: Updates segment list for class instance
        """
        screen = Screen()
        for i in range(seg_count):
            self.new_snake_part()
            self.segments[i].setposition(new_start, 0)
            new_start = self.segments[i].xcor() - 20

    def add_segment(self,position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# screen = Screen()
#
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# t = Snake()
# screen.exitonclick()