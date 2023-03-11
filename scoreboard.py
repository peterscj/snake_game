from turtle import Turtle

STYLE = ('Arial', 30, 'bold')
ALIGN = "center"
X_COR = 0
Y_COR = 200
SCORE = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(X_COR,Y_COR)
        self.score = SCORE
        self.text = f"Scoreboard: {self.score}"
        self.increase_score()

    def increase_score(self):
        self.write(self.text,align=ALIGN,font=STYLE)
    def update_score(self):
        self.score +=1
        self.text = self.text.rstrip(self.text[-1])
        self.text += str(self.score)
        self.clear()
        self.increase_score()

