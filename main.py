import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
car_manager = CarManager()
screen.onkey(player.start_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.speed_car)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.check_finish():
        player.starting_position()
        car_manager.speed_car *= 0.5
        scoreboard.increase_score()

screen.exitonclick()
