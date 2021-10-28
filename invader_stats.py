#used to track statistics for game
class InvaderStats:

    #initialize stats
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        #game will start in an active state.
        self.game_active = True

    #used to keep track of initialized stats that change during gameplay
    def reset_stats(self):
        self.spaceships_left = self.settings.spaceship_limit
        
