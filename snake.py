from turtle import Screen, Turtle
import turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0,0) , (-20,0), (-40,0)]
segments = []

for positions in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions)
    segments.append(new_segment)

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)
        
turtle.done()