from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.snake_body = []
        self.make_snake()
        self.head = self.snake_body[0]

    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.add_length(position)

    def add_length(self, position):
        new_square = Turtle(shape='square')
        new_square.color(self.color)
        new_square.penup()
        new_square.goto(position)
        self.snake_body.append(new_square)

    def snake_reset(self):
        for segment in self.snake_body:
            segment.goto(2000, 2000)
        self.snake_body.clear()
        self.make_snake()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_length(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def snake_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
