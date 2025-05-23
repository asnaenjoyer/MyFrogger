import pygame
from abc import ABC, abstractmethod

class Scene(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def load_resources(self) -> None:
        pass

    @abstractmethod
    def handle_event(self, event : pygame.Event) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass