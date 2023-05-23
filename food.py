from turtle import *
from random import randint, choice


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(choice(range(-280, 280, 20)), choice(range(-280, 280, 20)))


g
