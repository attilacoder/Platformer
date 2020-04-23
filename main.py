import pygame
pygame.init()
c = pygame.time.Clock()

w_size = [400,400]
w = pygame.display.set_mode(w_size)
pygame.display.set_caption('Platformer')
player_loc = [0,368]

player_image = pygame.image.load("player.png")
player_rect = pygame.Rect(player_loc[0],player_loc[1],player_image.get_width(),player_image.get_height())
player_y_momen = 0


test_rect = pygame.Rect(100, 368, 32,32)

moving_r = False
moving_l = False


playing = True
while playing:
    w.fill((255,255,255))

    if player_loc[1] > w_size[1]-player_image.get_height():
        player_y_momen = -player_y_momen
    else:
        player_y_momen += 0.2
    player_loc[1] += player_y_momen

    player_rect.x, player_rect.y = player_loc[0], player_loc[1]
    if moving_r:
        player_loc[0] += 4
    if moving_l:
        player_loc[0] -= 4
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_r = True
            if event.key == pygame.K_a:
                moving_l = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_r = False
            if event.key == pygame.K_a:
                moving_l = False
    if player_rect.colliderect(test_rect):
        pygame.draw.rect(w,(255,0,0),test_rect)
    else:
        pygame.draw.rect(w,(0,0,0),test_rect)
    w.blit(player_image, player_loc)
    pygame.display.update()
    c.tick(60)
