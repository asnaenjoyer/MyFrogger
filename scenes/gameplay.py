from core.scene import Scene
from core.managers.texture_manager import TextureManager
from game_objects.car_manager import CarManager
import pygame
import os

class Gameplay(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.tm: TextureManager = self.game.texture_manager
        self.load_resources()
        self.surface = pygame.Surface((150,150))
        self.cars = CarManager(self.tm)

    def load_resources(self):
        assets_path = "assets"
        for filename in os.listdir(assets_path):
            if filename.endswith(".png"):
                name = os.path.splitext(filename)[0] 
                filepath = os.path.join(assets_path, filename)
                self.tm.load_from_spritesheet(name, filepath, 16, 16)

    def update(self):
        self.cars.update(dt=self.game.dt)

    def handle_event(self, event):
        pass

    def render(self):
        self.surface.fill((100, 0, 0))
        self.cars.draw(self.surface)
        
        surf = pygame.transform.scale(self.surface, (600,600))
        self.game.screen.blit(surf, (0, 0))