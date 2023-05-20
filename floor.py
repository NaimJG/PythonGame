import pygame

BROWN = (255, 250, 100)

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([800, 50])
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 550
