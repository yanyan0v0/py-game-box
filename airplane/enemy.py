import pygame
import random
from pygame.rect import Rect


class Enemy(pygame.sprite.Sprite):
    enemy_count = 50
    speed = 1
    _image = pygame.image.load("static/enemy.png")
    _rect = _image.get_rect()

    def __init__(self, container_rect: Rect):
        super().__init__()
        self.image = pygame.image.load("static/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.get_x(container_rect)
        self.rect.y = container_rect.top
        self.move_y = 'bottom'
        randint = random.randint(0, 2)
        # 向左
        if randint == 0:
            self.move_x = 'left'
        # 向右
        else:
            self.move_x = 'right'

    def get_x(self, container_rect: Rect):
        return random.randint(self._rect.width, container_rect.width - self._rect.width)

    def move(self, container_rect: Rect):
        if self.move_x == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.move_y == 'bottom':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

        if self.rect.left <= container_rect.left:
            self.move_x = 'right'

        if self.rect.right >= container_rect.right:
            self.move_x = 'left'

        if self.rect.bottom <= container_rect.top:
            self.move_y = 'bottom'

        if self.rect.top >= container_rect.bottom:
            self.move_y = 'top'

