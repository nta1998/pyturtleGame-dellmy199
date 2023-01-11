FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.write(f"Level:{self.score}",font=("Couriel", 24, "normal"))
    
    def game_over(self):
        self.color("red")
        self.goto(-90,0)
        self.write("GAME OVER",font=("Couriel", 24, "normal"))
    def score_up(self):
        self.clear()
        self.penup()
        self.goto(-280,250)
        self.score += 1
        self.write(f"Level:{self.score}" ,font=("Couriel", 24, "normal"))
    
    
    
    
        
