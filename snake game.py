from turtle import Turtle, Screen
import time  # to add delay in snake movement

#   screen setup
screen = Screen()
screen.setup(height=600, width=600)  # this is for the window size
screen.bgcolor((0, 0, 0))
screen.title("Snake Game")

screen.tracer(0)  # to turn off updating the screen at every step. we will need to update the screen manually now

#   snake setup
segments = []  # after this we have a list of the segment(turtle objects) to play  around with
for _ in range(3):
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.goto(0 - (20 * _), 0)
    segments.append(segment)
screen.update()
game_on = True

# snake movement
while game_on:
    screen.update()  # updating the screen manually so that the moption of segments is smooth
    time.sleep(0.5)  # to add delay(in secs) in snake movement
    for seg_number in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_number - 1].xcor()
        new_y = segments[seg_number - 1].ycor()
        segments[seg_number].goto((new_x, new_y))
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()  # exit the screen on click
