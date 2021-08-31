from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def get_highscore(self):
        with open("data.txt") as file:
            contents = file.read()
            return(int(contents))

    def set_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 16, "normal"))

        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.set_highscore()

        self.score = 0
        self.update_scoreboard()