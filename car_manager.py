from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars=[]
        self.car_speed=MOVE_INCREMENT
        
    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y=random.randint(-280,280)
            new_car.goto(x=300,y=random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for i in self.all_cars:
            i.forward(self.car_speed)
    
    def level_up(self):
         self.car_speed+=MOVE_INCREMENT
         
        
