import os
import random

import pygame
from entity.floor import Floor
from entity.bird import Bird
from entity.pipe import Pipe
import entity.score

# 窗口宽高
W, H = 288, 512
# 每秒刷新次数
FPS = 30
# 向后移动速度
SPEED = 2
# 地板初始x坐标
FLOOR_X = 0
# 图片字典
IMAGES = {}
# 音频字典
AUDIO = {}
# 场景对象
SCENE: pygame.Surface = {}
# 场景容器
SCENE_RECT: pygame.Rect = {}
# 窗口中心
CENTER = (0, 0)
# 定时器
CLOCK = pygame.time.Clock()


def init():
    global SCENE
    global SCENE_RECT
    pygame.init()
    SCENE = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Flappy Bird')
    SCENE_RECT = SCENE.get_rect()


def load_assets():
    # 加载图片
    for file in os.listdir('assets/sprites'):
        name, suffix = os.path.splitext(file)
        path = os.path.join('assets/sprites', file)
        IMAGES[name] = pygame.image.load(path)
    # 随机背景
    IMAGES['bg'] = IMAGES[random.choice(['day', 'night'])]
    # 随机小鸟
    color = random.choice(['blue', 'red', 'yellow'])
    IMAGES['bird'] = [IMAGES[color + '-down'], IMAGES[color + '-mid'], IMAGES[color + '-up']]
    # 随机水管
    IMAGES['pipe'] = IMAGES[random.choice(['green', 'red']) + '-pipe']

    # 加载音乐
    for file in os.listdir('assets/audio'):
        name, suffix = os.path.splitext(file)
        path = os.path.join('assets/audio', file)
        AUDIO[name] = pygame.mixer.Sound(path)


def main():
    global CENTER
    floor = Floor(IMAGES['floor'], SCENE_RECT)
    CENTER = list(CENTER)
    CENTER[0] = SCENE_RECT.center[0]
    CENTER[1] = (SCENE_RECT.height - floor.rect.height) // 2
    CENTER = tuple(CENTER)

    while True:
        guide_window(floor)
        game_window(floor)
        over_window()


def guide_window(floor):
    global FLOOR_X
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        SCENE.blit(IMAGES['bg'], (0, 0))
        SCENE.blit(IMAGES['floor'], (FLOOR_X, SCENE_RECT.height - floor.rect.height))
        guide_rect = IMAGES['guide'].get_rect()
        guide_rect.center = CENTER
        SCENE.blit(IMAGES['guide'], guide_rect)
        pygame.display.update()
        CLOCK.tick(FPS)

        FLOOR_X = floor.move(FLOOR_X, SPEED)


def game_window(floor):
    global FLOOR_X
    bird = Bird(IMAGES['bird'], SCENE_RECT)

    pipe_group = pygame.sprite.Group()
    distance = 150
    pip_gap = 100
    for i in [2, 3, 4, 5]:
        bottom_pipe = Pipe(IMAGES['pipe'])
        top_pipe = Pipe(IMAGES['pipe'], True)
        bottom_pipe.rect.x = i * distance
        bottom_pipe.rect.top = random.randint(int(H * 0.3), int(H * 0.7))
        top_pipe.rect.x = i * distance
        top_pipe.rect.bottom = bottom_pipe.rect.top - pip_gap
        pipe_group.add(bottom_pipe)
        pipe_group.add(top_pipe)

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.up()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.up()

        SCENE.blit(IMAGES['bg'], (0, 0))

        first_pip, second_pip, *_ = pipe_group
        if first_pip.rect.right <= 0:
            pipe_group.remove(first_pip)
            pipe_group.remove(second_pip)
            last_pipe = list(pipe_group)[-1]
            new_first_pip = Pipe(IMAGES['pipe'])
            new_second_pip = Pipe(IMAGES['pipe'], pipe.upwards)
            new_first_pip.rect.x = last_pipe.rect.x + distance
            new_second_pip.rect.x = last_pipe.rect.x + distance
            new_first_pip.rect.top = random.randint(int(H * 0.3), int(H * 0.7))
            new_second_pip.rect.bottom = new_first_pip.rect.top - pip_gap
            pipe_group.add(new_first_pip)
            pipe_group.add(new_second_pip)

        for pipe in pipe_group:
            if (bird.rect.left - SPEED) <= pipe.rect.centerx < bird.rect.left:
                score += 0.5

            pipe.rect.x -= SPEED
            SCENE.blit(pipe.image, pipe.rect)

        SCENE.blit(IMAGES['floor'], (FLOOR_X, SCENE_RECT.height - floor.rect.height))

        SCENE.blit(bird.image, bird.rect)
        bird.fly()

        entity.score.show(score, IMAGES, SCENE_RECT, SCENE)

        pygame.display.update()
        CLOCK.tick(FPS)

        FLOOR_X = floor.move(FLOOR_X, SPEED)
        if bird.rect.top <= SCENE_RECT.top:
            return
        is_die = pygame.sprite.collide_rect(bird, floor)
        if is_die:
            return
        # is_die = pygame.sprite.spritecollideany(bird, pipe_group)
        # if is_die:
        #     return


def over_window():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        over_rect = IMAGES['gameover'].get_rect()
        over_rect.center = CENTER
        SCENE.blit(IMAGES['gameover'], over_rect)
        pygame.display.update()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    init()
    load_assets()
    main()
