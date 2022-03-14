class Settings:
    def __init__(self):
        self.screen_width = 740
        self.screen_height = 880
        # set background color
        self.bg_color = (0, 0, 0)
        self.pad_color = (255,255,255)
        #pad setings
        self.pad_width = 10
        self.pad_height = 60
        self.pad_speed = 0.5
        self.pad_quater = self.pad_height / 4

        # ball settings
        self.ball_width = 5
        self.ball_height = 5
        self.ball_speed = 0.2
        self.ball_color = (255,255,255)
        self.ball_angle = 0.5
        self.balls_allowed = 1

        self.maxscore = 10