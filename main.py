from turtle import Screen
import time
from snake import Snake
from food import Fruit
from scoreboard import Score
# TODO Make the Screen to be looked reasonable

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Fruit()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food()
        snake.new_snake()
        score.increased()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game0ver()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game0ver()


# TODO Think about this alogritm


screen.listen()
screen.exitonclick()