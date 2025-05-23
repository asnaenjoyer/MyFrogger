import pygame
import os
from core.tools.dict_tool import dict_slice_by_keys

class TextureManager:
    def __init__(self):
        self.textures = {}

    def load(self, name, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        texture = pygame.image.load(filepath).convert_alpha()
        self.textures[name] = texture
        
    def load_from_spritesheet(self, base_name, filepath, frame_width, frame_height, spacing=0, margin=0):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        sheet = pygame.image.load(filepath).convert_alpha()

        sheet_width, sheet_height = sheet.get_size()
        index = 0

        for y in range(margin, sheet_height, frame_height + spacing):
            for x in range(margin, sheet_width, frame_width + spacing):
                rect = pygame.Rect(x, y, frame_width, frame_height)
                frame = sheet.subsurface(rect).copy()
                self.textures[f"{base_name}_{index}"] = frame
                index += 1

    def get(self, name):
        texture = self.textures.get(name)
        if texture is None:
            raise KeyError(f"Texture with name '{name}' have not loaded properly.")
        return texture
    
    def get_slice(self, start_key, end_key, inclusive=True):
        return dict_slice_by_keys(self.textures, start_key, end_key, inclusive)

    def unload(self, name):
        if name in self.textures:
            del self.textures[name]

    def clear(self):
        self.textures.clear()
