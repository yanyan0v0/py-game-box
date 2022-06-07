import pygame


def show(score, image_dir, container_rect: pygame.Rect, scene: pygame.Surface):
    score_str = str(int(score))
    score_len = len(score_str)
    w = int(image_dir['0'].get_width() * 1.1)
    x = (container_rect.width - score_len * w) // 2
    y = int(container_rect.height * 0.1)
    for number in score_str:
        scene.blit(image_dir[number], (x, y))
        x += w
