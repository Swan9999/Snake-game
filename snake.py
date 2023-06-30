from dataclasses import dataclass
from turtle import Turtle
starting_positions = [(0,0), (-20, 0), (-40, 0)]
constant_movement = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in starting_positions:
            self.add_segment(segment)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            news_x = self.segments[seg_num - 1].xcor()
            news_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(news_x, news_y)
        self.segments[0].forward(constant_movement)

    def up(self):
        if self.head.heading() != "Down":
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != "Up":
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != "Right":
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != "Left":
            self.head.setheading(right)

    def add_segment(self, segment):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(segment)
        self.segments.append(new_segment)

    def new_snake(self):
        self.add_segment(self.segments[-1].position())


