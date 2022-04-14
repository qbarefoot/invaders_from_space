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

        #aliens return on screen once they hit edge
        def check_edges(self):
            screen_rect = self.screen.get_rect()
            if self.rect.right >= screen_rect.right or self.rect.left <= 0:
                return True

        #move alien fleet right on screen
        def update(self):
            self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
            self.rect.x = self.x
