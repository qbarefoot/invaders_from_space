#used to hide pygame message in terminal
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from settings import Settings
import sys 
from spaceship import Space_Ship
from missile import Missile
from alien import Alien




#the class being used to manage the entire game itself
class Invaders_Game:

    #method used to turn on the game and manage assests
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Invaders From Space")

        self.spaceship = Space_Ship(self)
        self.missiles = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    #used to spawn aliens
    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)


    #the main loop for the game
    def run_game(self):
        while True:
            self._check_events()
            self.spaceship.update()
            self._update_screen()
            self._update_missiles()

        #delete missile
            for missile in self.missiles.copy():
                if missile.rect.bottom <= 0:
                    self.missiles.remove(missile)
            print(len(self.missiles))

    #used to respond to input from keyboard and mouse events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_missile()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = False

    #create missiles and add to the missiles group
    def _fire_missile(self):
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    #missiles deleted, and positions updated
    def _update_missiles(self):
        self.missiles.update()
        

    #updates and flip images on player screen
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.spaceship.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    #used to run invaders from space
if __name__ == '__main__':
    ai = Invaders_Game()
    ai.run_game()