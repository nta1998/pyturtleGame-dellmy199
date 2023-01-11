COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle, speed
import random

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = 10
    def new_car(self):
        
        faest = random.randint(1,6)
        if faest == 1:
            new_cars = Turtle()
            new_cars.color(random.choice(COLORS))
            new_cars.shape("square")
            new_cars.shapesize(0.8,2)
            new_cars.penup()
            ry = random.randint(-250, 250)
            new_cars.goto(300,ry)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
        
    def speed_up(self):
        self.speed += 5
