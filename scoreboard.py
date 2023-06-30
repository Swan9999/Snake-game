from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "bold"))

    def game0ver(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 30 , "bold"))

    def increased(self):
        self.score += 1
        self.clear()
        self.update_score()