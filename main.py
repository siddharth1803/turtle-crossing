import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for all_cars in car_manager.all_cars:
        if all_cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            break
    if player.is_at_finish_line() is False:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
