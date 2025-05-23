import pygame

class SpriteStack(pygame.sprite.Sprite):
    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float], z_spacing=1):
        super().__init__()
        self.images = images
        self._pos = pos
        self.z_spacing = z_spacing
        self.rotation = 0
        self.image = pygame.Surface(images[0].get_size(), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self.rect.topleft = value
        
    def set_position(self, pos: tuple[float, float]):
        self.pos = pos
        
    def move(self, val: tuple[float, float]):
        self.pos = (self._pos[0] + val[0], self._pos[1] + val[1])
        
    def set_rotation(self, r):
        self.rotation = r
        
    def rotate(self, r):
        self.rotation += r
            
    def update(self, *args, **kwargs):
        pass

    def draw(self, surface):
        for i, img in enumerate(self.images):
            offset_y = -i * self.z_spacing
            rotated_img = pygame.transform.rotate(img, self.rotation)
            surface.blit(rotated_img, (self.pos[0] - rotated_img.get_width() // 2, self.pos[1] - rotated_img.get_height() // 2 + offset_y))
