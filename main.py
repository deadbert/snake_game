from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snakearoo')
screen.tracer(0)


snake = Snake('white')
food = Food()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.snake_left, 'Left')
screen.onkey(snake.snake_right, 'Right')
screen.listen()

score_keeper = Scoreboard('white', location=(0, 260))

game_on = True
while game_on:
    score_keeper.show_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # check for collision with snake food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_keeper.update_score()
        snake.extend()

    # detect for wall collisions
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score_keeper.reset()
        snake.snake_reset()

    # detect for snake on snake collision
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score_keeper.game_reset()
            snake.snake_reset()


screen.exitonclick()
