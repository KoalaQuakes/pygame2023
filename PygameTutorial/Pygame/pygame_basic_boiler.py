import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600,600])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))
    pygame.display.flip()
    clock.tick(30)