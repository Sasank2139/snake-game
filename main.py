from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard   
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game") 
screen.bgcolor("black")
screen.tracer(0)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.080)    
    snake.move()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            is_game_on = False
            scoreboard.game_over()        
screen.exitonclick()