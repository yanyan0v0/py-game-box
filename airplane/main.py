import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet

pygame.init()
scene = pygame.display.set_mode((800, 600))
bg = pygame.image.load("static/bg.png")
icon = pygame.image.load("static/ufo.png")
scene_rect = scene.get_rect()
pygame.display.set_caption("飞机大战")
pygame.display.set_icon(icon)
pygame.mixer.music.load('static/bg.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound('static/exp.wav')
boom_sound.set_volume(0.4)
speed = 0
enemy_default_count = 6

player = Player(scene_rect)
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
for index in range(enemy_default_count):
    enemy = Enemy(scene_rect)
    enemy_list.add(enemy)

score = 0
font = pygame.font.SysFont('Microsoft YaHei UI', 32, True)


def show_score():
    text = f"分数：{score}"
    text_render = font.render(text, True, (0, 255, 0))
    scene.blit(text_render, (10, 10))


def show_enemy():
    for enemy in enemy_list:
        enemy.move(scene_rect)
        scene.blit(enemy.image, enemy.rect)


def show_bullet():
    global bullet_list
    for bullet in bullet_list:
        bullet.move()
        scene.blit(bullet.image, bullet.rect)
        # 判断越界
        if (bullet.rect.top <= scene_rect.top):
            pygame.sprite.Sprite.remove(bullet, bullet_list)


def show_over():
    if (is_over):
        over_font = pygame.font.SysFont('Microsoft YaHei UI', 48, True)
        text = "Game Over"
        text_render = over_font.render(text, True, (255, 0, 0))
        text_rect = text_render.get_rect()
        text_rect.center = scene_rect.center
        scene.blit(text_render, text_rect)
        enemy_list.empty()
        bullet_list.empty()


running = True
is_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed = 0
            if event.key == pygame.K_LEFT:
                speed = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                speed = 3
            if event.key == pygame.K_LEFT:
                speed = -3
            if event.key == pygame.K_SPACE:
                bullet_list.add(Bullet(player.rect))

    player.rect.x += speed
    if player.rect.right >= scene_rect.right:
        player.rect.right = scene_rect.right
    if player.rect.left <= scene_rect.left:
        player.rect.left = scene_rect.left

    scene.blit(bg, scene_rect)
    scene.blit(player.image, player.rect)
    show_enemy()
    show_bullet()
    show_score()
    show_over()
    group_collide = pygame.sprite.groupcollide(enemy_list, bullet_list, True, True)
    if (group_collide):
        for enemy in group_collide:
            boom_sound.play()
            score += 1
            enemy_list.add(Enemy(scene_rect))

    player_collide = pygame.sprite.spritecollideany(player, enemy_list)
    if (player_collide):
        is_over = True


    pygame.display.update()
