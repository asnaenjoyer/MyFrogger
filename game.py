import pygame
from core.managers.scene_manager import SceneManager
from core.managers.texture_manager import TextureManager
from gameplay import Gameplay

class Game:
    def __init__(self, width=600, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("My Game")

        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True
        
        self.texture_manager = TextureManager()
        
        self.scene_manager = SceneManager()
        self.scene_manager.change_scene(Gameplay(self))

    def run(self):
        while self.running:
            self.dt = self.clock.tick(120) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.scene_manager.handle_event(event)

            self.scene_manager.update()
            self.screen.fill((0, 0, 0))
            self.scene_manager.render()
            pygame.display.flip()

        pygame.quit()
