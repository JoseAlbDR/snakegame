from turtle import *

ALIGNEMT = "center"
FONT = ("Verdana", 15, "normal")


def read_high_score():
    with open("data.txt", "r") as highest_r:
        return int(highest_r.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_high_score()
        # self.goto(300, 550)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.print_score()

    def add_score(self):
        self.clear()
        self.increase_score()
        self.print_score()

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.print_score()

    def increase_score(self):
        self.score += 1

    def print_score(self):
        self.write(f"Score: {self.score}\tHigh Score:{self.high_score}", align=ALIGNEMT, font=("Verdana", 15, "normal"))

    def write_high_score(self):
        with open("data.txt", "w") as highest_w:
            highest_w.write(str(self.high_score))
