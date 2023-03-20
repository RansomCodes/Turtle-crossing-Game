from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(-280,250)
        self.level=0
        self.level_up()
    
    def level_up(self):
        self.clear()
        self.level+=1
        self.write(f"Level: {self.level}",font=FONT)
    
    def game_over(self):
        self.goto(-100,0)
        self.write("GAME OVER!!",font=FONT)
