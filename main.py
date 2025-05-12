import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard  = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()
    
    if player.at_Finish():
        player.go_back()
        car.lvl_up()
        scoreboard.increase_level()
        

    for car1 in car.all_cars:
        if car1.distance(player) < 20:
            game_is_on = False

screen.exitonclick()

    