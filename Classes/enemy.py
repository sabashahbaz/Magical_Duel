import pygame
import os
import random
pygame.font.init()
from game import Game


DEMENTOR_IMAGE = pygame.image.load(os.path.join('../Assets', 'death_eater.png'))

#initiating the class of the enemy 
class Enemy(Game):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 150
        self.vel = 4
        self.enenmy_image = pygame.image.load(os.path.join('../Assets', 'death_eater.png'))
        self.dementor = pygame.transform.rotate(pygame.transform.scale(self.enenmy_image, (self.width, self.height)), 0)
        self.x = self.win_width
        self.y = 100
        self.left = True
    
       #having the enemy appear on the screen 
    def draw_enemy(self):
        self.window.blit(self.dementor, (self.x, self.y))
        pygame.display.update()
    
    def update(self):
        # Move the dementor from right to left
        if self.left:
            self.x -= self.vel
        else:
            self.x += self.vel

        # Check if the dementor has reached to the edge of the screen 
        if self.x < 0:
            self.left = False
        elif self.x + self.width >= self.win_width:
            self.left = True
    
        # print(self.x + self.width)
        assert self.x + self.width, "Enemy was not reset on screen boundary properly"
 
    def enemy_display_points(self):
        dementor_lives =10
        self.font = pygame.font.SysFont("Verdana", 30)
        lives_label = self.font.render(f"dementor lives: {dementor_lives}", 1, (255, 255, 255))
        self.window.blit(lives_label, (self.win_width - lives_label.get_width() -10, 10))