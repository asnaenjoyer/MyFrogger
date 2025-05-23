import math
from game_objects.sprite_stack import SpriteStack
from core.managers.texture_manager import TextureManager
from ai.car_ai import AIType

class Car(SpriteStack):
    textures_count = 9
    def __init__(self, tm: TextureManager, pos=(0,0), ai_type=AIType.LEFT):
        self.speed = 30
        self.name = self.__class__.__name__
        super().__init__(tm.get_slice(f"{self.name}_0", f"{self.name}_{self.textures_count-1}", True), pos)
        self._ai = ai_type
        
    def update(self, dt, *args, **kwargs):
        if self._ai:
            self._ai(self, dt)
        rad = math.radians(self.rotation)
        dx = math.cos(rad)
        dy = -math.sin(rad)  
        self.move((dx * self.speed * dt, dy * self.speed * dt))
        
    def ai(self):
        pass
        
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