from game_objects.cars import GreenBigCar, GreenCar, PurpleCar, RedCar, YellowCar
from core.managers.texture_manager import TextureManager
from ai.car_ai import AIType
import pygame
import random

class CarManager:
    def __init__(self, tm: TextureManager):
        self.cars = []
        self.tm = tm

        car_classes = [GreenBigCar, GreenCar, PurpleCar, RedCar, YellowCar]

        start_x = 75
        start_y = 16
        spacing_y = 16  

        ai_type = AIType.LOOP
        for i, cls in enumerate(car_classes):
            x = start_x
            y = start_y + i * spacing_y
            ai_type = AIType.RIGHT if ai_type == AIType.LOOP else AIType.LOOP
            car = cls(tm, (x, y), ai_type)
            self.cars.append(car)
            
        for i, cls in enumerate(car_classes):
            x = start_x
            y =  75 + start_y + i * spacing_y
            ai_type = AIType.RIGHT if ai_type == AIType.LEFT else AIType.LEFT
            car = cls(tm, (x, y), ai_type)
            self.cars.append(car)

    def create_car(self):
        pass
    
    def update(self, dt):
        for car in self.cars:
            car.update(dt)

    def draw(self, surface):
        for car in self.cars:
            car.draw(surface)
