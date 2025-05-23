from enum import Enum, auto
import random

def ai_left(car, dt):
    pass

def ai_right(car, dt):
    car.set_rotation(180)
    
def ai_loop(car, dt):
    car.rotate(60 *dt)

class AIType(Enum):
    LEFT = ai_left
    RIGHT = ai_right
    LOOP = ai_loop