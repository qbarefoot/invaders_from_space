import pygame.font

#used to display player score info
class Scoreboard:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #settings for player score color
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        #display score image
        self.prep_score()

    #used to render scoreboard image
    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, 
                self.text_color, self.settings.bg_color)

        #used to display the player score in the top right hand corner of window
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    #score is drawn on screen
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
