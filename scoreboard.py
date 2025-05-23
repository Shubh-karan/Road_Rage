from turtle import Turtle

FONT = ("Couries" , 24 , "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.update_scoreboard

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}" , align="left" , font=("Arial" , 15, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
