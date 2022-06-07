import random

import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, upwards = False):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.upwards = upwards
        if upwards:
            self.image = pygame.transform.flip(self.image, False, True)

