from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
X_AXIS = []
Y_AXIS = [-250, 250]


class CarManager:

    def __init__(self):
        self.new_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            cars = Turtle("square")
            cars.penup()
            cars.color(random.choice(COLORS))
            cars.shapesize(1, 2)
            cars.left(180)
            y_axis = random.randint(-250, 250)
            cars.goto(300, y_axis)
            self.new_cars.append(cars)

    def move(self):
        for car in self.new_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
