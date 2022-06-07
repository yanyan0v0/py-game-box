import pygame


class Floor(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, container_rect: pygame.Rect):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.top = container_rect.height - self.rect.height
        self.container_rect = container_rect

    def move(self, x, speed) -> int:
        x -= speed
        if x <= self.container_rect.width - self.rect.width:
            x = 0

        return x

