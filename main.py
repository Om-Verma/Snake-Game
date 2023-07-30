from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor((0, 0, 0))
screen.title("Snake Game")
screen.tracer(0)
screen.update()
game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # starts to listen to keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    snake.move()
    time.sleep(0.08)
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    # detect collision with wall

    if abs(snake.head.xcor())>290 or abs(snake.head.ycor())>290:
        game_on=False
        scoreboard.game_over()
        screen.exitonclick()

    #detect collision with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment)<10:
            game_on = False
            scoreboard.game_over()
            screen.exitonclick()