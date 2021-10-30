#used to hide pygame message in terminal
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys 
from time import sleep
from settings import Settings
from spaceship import Space_Ship
from missile import Missile
from alien import Alien
from invader_stats import InvaderStats
from button import Button




#the class being used to manage the entire game itself
class Invaders_Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Invaders Are Coming!!!")

        #used to store game stats instance
        self.stats = InvaderStats(self)

        self.spaceship = Space_Ship(self)
        self.missiles = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #create play button
        self.play_button = Button(self, "Play")

    #start main game
    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.spaceship.update()
                self._update_missiles()
                self._update_aliens()

            self._update_screen()

    #control key and mouse responses
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    #click "Play" button to start new game and reset stats
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            #mouse cursor not visible
            pygame.mouse.set_visible(True)

            #discard remaining aliens and missiles
            self.aliens.empty()
            self.missiles.empty()

            #create new aliens and center player
            self._create_fleet()
            self.spaceship.center_spaceship()

    #response to key down
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_missile()

    #response to key releases
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = False

    #used to create missiles 
    def _fire_missile(self):
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    #update and delete missiles on screen
    def _update_missiles(self):
        self.missiles.update()
        for missile in self.missiles.copy():
            if missile.rect.bottom <= 0:
                self.missiles.remove(missile)


        #remove missiles and spawn a new a fleet
        if not self.aliens:
                self.missiles.empty()
                self._create_fleet()

        self._check_missile_alien_collisions()

    #used to check missile and alien collisions
    def _check_missile_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.missiles, self.aliens, True, True)

        #used to get rid of old missiles and create new fleet
        if not self.aliens:
            self.missiles.empty()
            self._create_fleet()
            self.settings.increase_speed()

    #update the alien positions and fleet
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        #detect alien-player ship collisions
        if pygame.sprite.spritecollideany(self.spaceship, self.aliens):
            self._spaceship_impact()

    # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    #in place to check when alien fleet reachs bottom of screen
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                
                #used to reverify if ship is hit
                self._spaceship_impact()
                break

    #reponse to ship impact by alien
    def _spaceship_impact(self):
        if self.stats.spaceships_left > 0:
            self.stats.spaceships_left -= 3

            #missiles and aliens removed that remain
            self.aliens.empty()
            self.missiles.empty()

            #new fleet created and player ship centered
            self._create_fleet()
            self.spaceship.center_spaceship()

            #game paused
            sleep(1.0)
        else:
            self.stats.game_active = False

    #used to spawn aliens
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (4 * alien_width)
        number_aliens_x = available_space_x // (4 * alien_width)
        
        #used to determine the number of aliens on that can be fit on screen
        spaceship_height = self.spaceship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - spaceship_height)
        number_rows = available_space_y // (4 * alien_height)
        
        # creates the entire alien force
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    #creates row of aliens
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    #used to check aliens reaching edge of screen
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    #determines fleet direction and drop      
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    #updates and flip images on player screen
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.spaceship.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        self.aliens.draw(self.screen)
    
        #will draw the play button when game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

#used to run invaders from space
if __name__ == '__main__':
    ai = Invaders_Game()
    ai.run_game()