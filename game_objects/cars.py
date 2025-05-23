import pygame
from game_objects.sprite_stack import SpriteStack
from core.managers.texture_manager import TextureManager

class Car(SpriteStack):
    textures_count = 9
    def __init__(self, tm: TextureManager):
        self.speed = 30
        self.direction = (1,0)
        self.name = self.__class__.__name__
        super().__init__(tm.get_slice(f"{self.name}_0", f"{self.name}_{self.textures_count-1}", True), (16,16))
        
    def update(self, dt, *args, **kwargs):
        self.move((self.speed * dt * self.direction[0], self.speed * dt * self.direction[1]))
        self.rotate(1)
        
class GreenBigCar(Car):
    textures_count = 10

class GreenCar(Car):
    textures_count = 6

class PurpleCar(Car):
    textures_count = 8

class RedCar(Car):
    textures_count = 8

class YellowCar(Car):
    textures_count = 12