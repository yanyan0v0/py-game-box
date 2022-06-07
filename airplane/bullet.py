import pygame
from pygame.rect import Rect


class Bullet(pygame.sprite.Sprite):
    speed = 5
    _image = pygame.image.load("static/bullet.png")
    _rect = _image.get_rect()

    def __init__(self, player_rect):
        super().__init__()
        self.image = pygame.image.load("static/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = player_rect.center
        self.rect.bottom = player_rect.top
        self.is_alive = True

    def move(self):
        self.rect.y -= self.speed
