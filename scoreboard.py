from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self, color, location):
        super().__init__()
        self.penup()
        self.color(color)
        self.hideturtle()
        self.goto(location)
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_reset(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as file:
                file.write(f"{self.score}")
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())

    def update_score(self):
        self.score += 1
        self.show_score()
