#used to store and change settings for game
class Settings:

#initalize the game and screen settings
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.spaceship_speed = 1.5
        self.spaceship_limit = 3

        #missile settings
        self.missile_speed = 2.0
        self.missile_width = 10
        self.missile_height = 15
        self.missile_color = (80, 80, 80)
        self.missiles_allowed = 3

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        self.fleet_direction = 1

        #speed up game after new fleet appears
        self.speedup_scale = 1.0

        self.initialize_dynamic_settings()
        
        self.alien_points = 100

    #init settings that continue to change with each new level
    def initialize_dynamic_settings(self):
        self.spaceship_speed = 1.5
        self.missile_speed = 3.0
        self.alien_speed = 1.0

        #fleet_direction of 1 indicates the fleet is going right
        self.fleet_direction = 1

    #the speed settings 
    def increase_speed(self):
        self.spaceship_speed *= self.speedup_scale
        self.missile_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
