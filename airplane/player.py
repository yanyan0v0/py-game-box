import pygame
from pygame.rect import Rect

class Player(pygame.sprite.Sprite):
    def __init__(self, container_rect: Rect):
        super().__init__()
        self.image = pygame.image.load("static/player.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = container_rect.midbottom
        self.rect.bottom = container_rect.bottom - 10