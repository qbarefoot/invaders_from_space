import pygame

#used to manage the player's ship
class Space_Ship:

#initalize ship and the starting point on screen
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
#player ship settings
        self.spaceship_speed = 1.5        

#load player ship image and get rect or "rectangles"
        self.image= pygame.image.load('images/playership.bmp')
        self.rect =self.image.get_rect()

#start player ship at middle-bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

#decimal value stored for horizonal position of player ship
        self.x = float(self.rect.x)

        #ship movement flag
        self.moving_right = False
        self.moving_left = False

#player ship position based on movement flag
    def update(self):
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1



#this will draw player ship at the current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)