import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, image_list: list[pygame.Surface], container_rect: pygame.Rect):
        super().__init__()
        self.image_list = image_list
        self.image = image_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = container_rect.center
        self.frames = [0, 0, 0, 0,  1, 1, 1, 1,  2, 2, 2, 2,  1, 1, 1, 1,  0, 0, 0, 0]
        self.index = 0
        self.max_speed = -8
        self.speed = 0
        self.gravity_speed = 1
        self.max_rotate = 45
        self.rotate = 0
        self.rotate_speed = -2

    def fly(self):
        self.image = self.image_list[self.frames[self.index]]
        self.index += 1
        if self.index >= (len(self.frames) - 1):
            self.index = 0

        self.speed += self.gravity_speed
        self.rect.y += self.speed

        self.rotate += self.rotate_speed
        if self.rotate <= -self.max_rotate:
            self.rotate = -self.max_rotate
        self.image = pygame.transform.rotate(self.image, self.rotate)

    def up(self):
        self.speed += self.max_speed
        self.rect.y += self.speed
        self.image = self.image_list[self.frames[self.index]]
        self.rotate += self.max_rotate
        if self.rotate >= self.max_rotate:
            self.rotate = self.max_rotate
        self.image = pygame.transform.rotate(self.image, self.rotate)
