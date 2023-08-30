import pygame, math, random
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.heigt = tile_size

        self.image = pygame.Surface([self.width,self.heigt])
        self.image.fill(red)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass