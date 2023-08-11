import pygame
import os
import random
pygame.font.init()
from Classes.game import Game
from Classes.player import Player

DEMENTOR_IMAGE = pygame.image.load(os.path.join('Assets', 'death_eater.png'))

#initiating the class of the enemy 
class Enemy(Game):w
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 150
        self.vel = 5
        self.enenmy_image = pygame.image.load(os.path.join('Assets', 'death_eater.png'))
        self.dementor = pygame.transform.rotate(pygame.transform.scale(self.enenmy_image, (self.width, self.height)), 0)
        self.x = self.win_width
        self.y = 100
    
    
    def update(self):
        # Move the dementor from right to left
        self.x -= self.vel

        # Check if the dementor has moved off the screen
        if self.x + self.width < 0:
            # Reset the dementor's position to the right edge of the screen
            self.x = self.win_width

    #having the enemy appear on the screen 
    def draw_enemy(self):
        self.window.blit(self.dementor, (self.x, self.y))
        pygame.display.update()

    

