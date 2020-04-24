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
y_speed = 0
y_acc = 0.4
y_max = 6


p_img = pygame.image.load('player.png')
grass = pygame.image.load('grass.png')
dirt =  pygame.image.load('dirt.png')
cloud = pygame.image.load('cloud.png')

playing = True
while playing:
    w.fill(sky)



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
                if y_speed > -y_acc:
                    y_speed = y_acc
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False



    if right:
        p_pos[0] += x_speed
    if left:
        p_pos[0] -= x_speed



    w.blit(p_img, p_pos)





    pygame.display.update()
    c.tick(60)
