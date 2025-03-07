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

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate random cars and move them across the screen
    car_manager.generate_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.new_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Player crosses the finish line and goes again
    if player.is_at_finish_line():
        player.go_to_starting_position()
        car_manager.increase_speed()
        scoreboard.level_up()


screen.exitonclick()
