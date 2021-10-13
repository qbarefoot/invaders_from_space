import pygame
from pygame.sprite import Sprite

#the class represents an alien
class Alien(Sprite):

    #used to set the alien starting position
        def __init__(self, ai_game):
            super().__init__()
            self.screen = ai_game.screen
            self.settings = ai_game.settings

            #load alien sprite and attributes
            self.image = pygame.image.load("images/alien_ufo.bmp")
            self.rect = self.image.get_rect()

            #starting position at top left of window
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height

            #used to store horizonal position
            self.x = float(self.rect.x)

        #move alien fleet right on screen
        def update(self):
            self.x += self.settings.alien_speed
            self.rect.x = self.x
