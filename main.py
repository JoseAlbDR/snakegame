import time
from snake import *
from food import *
from scoreboard import *
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 280:
        score.reset()
        time.sleep(0.5)
        snake.reset()

    # Detect collision with tail

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            time.sleep(0.5)
            snake.reset()

screen.exitonclick()
