import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

# player
player_surf = pygame.Surface((50,50))
player_surf.fill('red')
player_rect = player_surf.get_rect(center = (300,300))
player_mask = pygame.mask.from_surface(player_surf)

# obsticale
obsticale_surf = pygame.image.load('pygame/alpha.png').convert_alpha()
obsticale_pos = (100,100)
obsticale_mask = pygame.mask.from_surface(obsticale_surf)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('white')

    # obsticale
    screen.blit(obsticale_surf,obsticale_pos)

    # moving part
    if pygame.mouse.get_pos():
        player_rect.center = pygame.mouse.get_pos()
    screen.blit(player_surf,player_rect)

    offset_x = obsticale_pos[0] - player_rect.left
    offset_y = obsticale_pos[1] - player_rect.top
    #if player_mask.overlap(obsticale_mask,(offset_x,offset_y)):
    #    print('collosion')

    if player_mask.overlap_area(obsticale_mask,(offset_x,offset_y)) >= 10:
        print('collosion')

    pygame.display.update()
    clock.tick(60)