import pygame
from pygame.sprite import Sprite

#the class used to manage the ship's projectiles
class Missile(Sprite):
    
    #missile object created at player ship's position
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.missile_color

        #missile created at rect position and then setting correct position
        self.rect = pygame.Rect(0, 0, self.settings.missile_width,
            self.settings.missile_height)
        self.rect.midtop = ai_game.spaceship.rect.midtop

        #used to store missile position as a decimal
        self.y = float(self.rect.y)

    #to move the missile towards top of screen and hit aliens
    def update(self):
        self.y -= self.settings.missile_speed
        self.rect.y = self.y

    #draw missile on screen
    def draw_missile(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


