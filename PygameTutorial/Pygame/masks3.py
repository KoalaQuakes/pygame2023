import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

# creation the obstacle
obstacle_surf = pygame.image.load('Pygame2023/PygameTutorial/load.png').convert_alpha()
obstacle_pos = (100,100)
obstacle_mask = pygame.mask.from_surface(obstacle_surf)

# mask into surface
#new_obstacle_surf = obstacle_mask.to_surface()
#new_obstacle_surf.set_colorkey((0,0,0))

# filling in the surface with a color
#surf_w,surf_h = new_obstacle_surf.get_size()
#for x in range(surf_w):
#    for y in range(surf_h):
#        if new_obstacle_surf.get_at((x,y))[0] != 0:
#            new_obstacle_surf.set_at((x,y),'orange')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    screen.blit(obstacle_surf,obstacle_pos)
    #screen.blit(new_obstacle_surf,obstacle_pos)

    # a simple way to create an outline from a mask
    for point in obstacle_mask.outline():
        x = point[0] + obstacle_pos[0]
        y = point[1] + obstacle_pos[1]
        pygame.draw.circle(screen, 'red', (x,y), 3)


    pygame.display.update()
    clock.tick(60)