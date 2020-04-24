import pygame
import sys
import time
from pygame import *

pygame.init()

c = pygame.time.Clock()


w_size = [500,350]

sky = (130, 178, 255)
w = pygame.display.set_mode(w_size)
w.fill(sky)

right = False
left = False

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map('map')
true_scroll = [0,0]
p_pos = [100,50]
x_speed = 4
y_speed = 0
j_speed = 6
grav = 0.4
jumping = False
air_timer = 0
space = 0
p_rect = pygame.Rect(p_pos[0],p_pos[1],16,16)
p_img = pygame.image.load('player.png')
grass = pygame.image.load('grass.png')
dirt =  pygame.image.load('dirt.png')
cloud = pygame.image.load('cloud.png')



playing = True
while playing:
    w.fill(sky)
    p_rect.x, p_rect.y = p_pos[0], p_pos[1]
    true_scroll[0] += (p_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (p_rect.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                w.blit(dirt,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                w.blit(grass,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '3':
                w.blit(cloud,(x*16-scroll[0],y*16-scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_SPACE:
                space = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_SPACE:
                space = 0
    for rec in tile_rects:
        if p_rect.colliderect(rec):
            y_speed = 0
    if p_pos[1] > w_size[1]-p_img.get_height():
        y_speed = space * -j_speed
    elif y_speed < 10:
        y_speed += grav
    if right:
        p_pos[0] += x_speed
    if left:
        p_pos[0] -= x_speed


    p_pos[1] += y_speed

    w.blit(p_img, p_pos)




    pygame.display.update()
    c.tick(60)
