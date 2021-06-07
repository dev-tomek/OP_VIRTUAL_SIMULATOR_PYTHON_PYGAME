import pygame
import os
import random

class Organism:
    def __init__(self, xpos, ypos, game):
        self.g = game
        self.xpos = xpos
        self.ypos = ypos
        self.icon = pygame.image.load(os.path.join('assets', 'empty.png'))
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.age = 0

    def draw(self):
        self.game.WINDOW.blit(self.icon, (self.rect.x, self.rect.y))

    





