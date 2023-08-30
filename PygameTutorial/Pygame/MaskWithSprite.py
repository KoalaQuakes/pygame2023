import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (300,300))
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        if pygame.mouse.get_pos():
            self.rect.center = pygame.mouse.get_pos()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame/alpha.png').convert_alpha()
        self.rect = self.image.get_rect(center = (400,400))
        self.mask = pygame.mask.from_surface(self.image)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))

# group setup
player = pygame.sprite.GroupSingle(Player())
obstacle = pygame.sprite.GroupSingle(Obstacle())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('white')

    # updating and drawing
    player.update()
    player.draw(screen)
    obstacle.draw(screen)

    # collision
    if pygame.sprite.spritecollide(player.sprite,obstacle,False): # check rect first to optimise 
        if pygame.sprite.spritecollide(player.sprite,obstacle,False,pygame.sprite.collide_mask): # now check mask 
            player.sprite.image.fill('green')
        else:
            player.sprite.image.fill('red')

    pygame.display.update()
    clock.tick(60)