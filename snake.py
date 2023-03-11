from turtle import Screen, Turtle
class Snake:
    def __init__(self, name):
        self.name = name

    def new_snake_part(self, segment):
        self.segment = segment
        self.segment = Turtle(shape="square")
        self.segment.color("black")
        self.segment.goto(-20,-20)

    # def get_intial_snake(self):
    #     new_start = 0
    #     self.color("white")
    #     segments = list()
    #     for i in range(3):
    #         snake_piece = new_snake_part()
    #         snake_piece.penup()
    #         screen.tracer(5)
    #         snake_piece.setposition(new_start, 0)
    #         new_start = snake_piece.xcor() - 20
    #         segments.append(snake_piece)
    #     return segments

screen = Screen()
screen.setup(width=600, height=600)
t = Snake("cole")
t.new_snake_part(1)
screen.exitonclick()