from pygame import mixer


class Sounds:
    def __init__(self):
        self.ball_bounce = mixer.Sound('sounds/ball_bounce.wav')
        self.ball_lost = mixer.Sound('sounds/ball_lost.wav')