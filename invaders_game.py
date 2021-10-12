import pygame
from settings import Settings
import sys 
from spaceship import Space_Ship




#the class being used to manage the entire game itself
class Invaders_Game:

#method used to turn on the game and manage assests
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        #used "pygame.display.set_mode" to make a display window, use the tuple "(600, 1200) for screen dimension", then assigned everything to "self.screen" attribute
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invaders From Space!")

        self.spaceship = Space_Ship(self)

        #used to mod the background color
        self.bg_color = (230, 230, 230)

#the main loop for the game
    def run_game(self):
        while True:
            self._check_events()
            self.spaceship.update()
            self._update_screen()

#used to respond to input from keyboard and mouse events 
    def _check_events(self):

            #event listener used to listen for controls to close the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.moving_right = True
                elif event.type == pygame.K_LEFT:
                    self.spaceship.moving_left = True

                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.spaceship.moving_right = False
                        elif event.key == pygame.K_LEFT:
                            self.spaceship.moving_left = False
                    #allows player to move player ship to right
                        self.spaceship.rect.x =+ 1


#updates and flip images on player screen
    def _update_screen(self):
            #recreate screen during each pass on the loop
            self.screen.fill(self.settings.bg_color)
            self.spaceship.blitme()

            #used to update and make the newest screen visible
            pygame.display.flip()

#used to run Invaders From Space
if __name__ == "__main__":
    ai = Invaders_Game()
    ai.run_game()