from turtle import *

STARTING_POSITION = ((0, 0), (0, -20), (0, -40))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def move(self):
        # start   # stop # step
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for poss in STARTING_POSITION:
            self.add_segment(poss)

    def add_segment(self, position):
        # Add a new segment to the snake
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.body.append(segment)

    def extend(self):
        poss = (self.body[-1].xcor(), self.body[-1].ycor())
        self.add_segment(poss)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.body:
            seg.hideturtle()
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
