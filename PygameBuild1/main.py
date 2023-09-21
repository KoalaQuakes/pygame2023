import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # draw all elements
    screen.blit(test_surface,(0,0))

    
    # update the screen
    pygame.display.update()
    clock.tick(60) #while loop should not run faster than 60 frmaes per second