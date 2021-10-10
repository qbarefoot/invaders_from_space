import pygame
from settings import Settings
import sys 




#the class being used to manage the entire game itself
class Invaders_Game:

#method used to turn on the game and manage assests
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        #used "pygame.display.set_mode" to make a display window, use the tuple "(1600, 900) for screen dimension", then assigned everything to "self.screen" attribute
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invaders From Space!")

        #used to mod the background color
        self.bg_color = (230, 230, 230)

#the main loop for the game
    def run_game(self):
        while True:
            #event listener used to listen for controls to close the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #recreate screen during each pass on the loop
            self.screen.fill(self.settings.bg_color)

            #used to update and make the newest screen visible
            pygame.display.flip()

#used to run Invaders From Space
if __name__ == "__main__":
    ai = Invaders_Game()
    ai.run_game()