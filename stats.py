import pygame

class Stats:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0
        self.ball_owner = 1
        self.game_active = False
        self.winner = 0

class Scoring:
    def __init__(self, pong):
        self.screen = pong.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pong.settings
        self.stats = pong.stats

        # visual representation
        self.text_color = (255,255,255)
        self.font = pygame.font.Font("fonts/Retro_Gaming.ttf", 20)
        self.prep_score()

    def prep_score(self):
        # rendering score to screen
        score_str = str(self.stats.p1_score) + " : " + str(self.stats.p2_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # position to display score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = self.screen_rect.midtop
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

