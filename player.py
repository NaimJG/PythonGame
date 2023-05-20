import pygame

# Definir las dimensiones de la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 590

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("froggie.png")
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.velocity_y = 0
        self.jump_speed = -1
        self.jumping = False

    def move_right(self):
        if self.rect.x < 940:
            self.rect.x += 1

    def move_left(self):
        if self.rect.x > -10:
            self.rect.x -= 1

    def move_up(self):
        if not self.jumping:
            self.jumping = True
            self.velocity_y = -2

    def update(self):
        # Actualizar la posición vertical
        self.rect.y += self.velocity_y

        # Actualizar la velocidad vertical para simular la gravedad
        if self.velocity_y < 5:
            self.velocity_y += .02

        # Comprobar si ha tocado el suelo
        if self.rect.y >= 390:
            self.rect.y = 390
            self.velocity_y = 0
            self.jumping = False