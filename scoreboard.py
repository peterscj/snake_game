from turtle import Turtle

STYLE = ('Courier', 22, 'bold')
ALIGN = "center"
X_COR = 0
Y_COR = 270
SCORE = 0

class Scoreboard(Turtle):
    """
    New class to generate visual scoreboard and keep track of consumption.
    Inherits all properties of the tuurtle class
    """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(X_COR,Y_COR)
        self.score = SCORE
        self.increase_score()

    def increase_score(self):
        """
        Generates scoreboard output
        """
        self.write(f"Scoreboard: {self.score}",align=ALIGN,font=STYLE)
    def update_score(self):
        """
        Add 1 to score and clear text in scoreboard title
        """
        self.score +=1
        self.clear()
        self.increase_score()

    def game_over(self):
        """
        Displays game over text if losing condition met
        """
        self.goto(0,15)
        self.write("GAME OVER",align=ALIGN,font=STYLE)