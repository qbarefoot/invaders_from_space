#used to store and change settings for game
class Settings:

#initalize the game and screen settings
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.spaceship_speed = 1.5

        #missile settings
        self.missile_speed = 1.0
        self.missile_width = 3
        self.missile_height = 15
        self.missile_color = (60, 60, 60)

