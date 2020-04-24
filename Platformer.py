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

p_pos = [50,50]
x_speed = 4
y_speed = 6
y_acc = 0
y_max = 6
jumping = False

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
                y_acc = -6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False
    if p_pos[1] > w_size[1]-p_img.get_height():
        y_acc = -y_acc
    else:
        y_acc += 0.2
    p_pos[1] += y_acc
    if jumping:
        y_speed -= y_acc
        if y_speed < -6 and y_speed > 0:
            y_speed = 6
            jumping = False


    if right:
        p_pos[0] += x_speed
    if left:
        p_pos[0] -= x_speed




    w.blit(p_img, p_pos)




    pygame.display.update()
    c.tick(60)
