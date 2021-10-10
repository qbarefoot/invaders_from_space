import pygame

#used to manage the player's ship
class Space_Ship

#initalize ship and the starting point on screen
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

#
