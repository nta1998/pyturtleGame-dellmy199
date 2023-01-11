import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
cars = CarManager()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")
game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    cars.new_car()
    cars.move_cars()
    
    for car in cars.all_cars:
        if car.distance(player) < 20 :
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        cars.speed_up()
        scoreboard.score_up()
        player.goto(0,-280)
    
    
    
    
screen.exitonclick()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
screen.exitonclick()