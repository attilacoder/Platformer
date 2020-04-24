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
    
p_pos = [50,50]
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
