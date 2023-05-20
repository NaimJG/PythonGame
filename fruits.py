import pygame
import random

# Frutas

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1000 - self.rect.width)
        self.rect.y = random.randrange(-250, -50)
        
    def update(self):
        self.rect.y += 1
        if self.rect.y > 500:
            self.kill()

class Banana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("banana.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1000 - self.rect.width)
        self.rect.y = random.randrange(-250, -50)
        
    def update(self):
        self.rect.y += 1
        if self.rect.y > 500:
            self.kill()    