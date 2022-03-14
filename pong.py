import sys
import pygame
from settings import Settings
from pad import Player1, Player2
from ball import Ball
from stats import Stats, Scoring
from msgs import Title, Start, GameOver
from sounds import Sounds


class Pong:
    # manage game behavior at startup
    def __init__(self):
        # initialize sounds
        pygame.mixer.pre_init(22050, -16, 2, 64)
        pygame.mixer.init()
        # start game engine
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width)) # ,pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Pong by MS")
        self.p1 = Player1(self)
        self.p2 = Player2(self)
        self.balls = pygame.sprite.Group()  # without sprites - Ball(self)
        self.stats = Stats()
        self.scoring = Scoring(self)
        self.title = Title(self)
        self.start = Start(self)
        self.gameover = GameOver(self)
        self.sounds = Sounds()

    def run_game(self):
        # main loop for the game
        while True:
            self._check_events()  # listening to keyboard or mouse inputs
            if self.stats.game_active:
                self.p1.update()  # updates Player1 position
                self.p2.update()
                self._balls_update()
            self._update_screen()  # redering to screen - last step in function!

    def _check_events(self):
        # listening to keyboard or mouse inputs
        for event in pygame.event.get():
            # respond to closing window
            if event.type == pygame.QUIT:
                sys.exit()
            # checks for any down keys for both players
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # checks for any up keys for both players
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.p1.moving_up = False
        elif event.key == pygame.K_s:
            self.p1.moving_down = False
        elif event.key == pygame.K_UP:
            self.p2.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.p2.moving_down = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.p1.moving_up = True
        elif event.key == pygame.K_s:
            self.p1.moving_down = True
        elif event.key == pygame.K_UP:
            self.p2.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.p2.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.stats.game_active:
                self._shoot_ball()
                pygame.mixer.Sound.play(self.sounds.ball_bounce)
            # if its not active change state to True ------>   missing ???
            elif self.stats.winner == 0:
                self.stats.game_active = True
        # RESET GAME
        elif event.key == pygame.K_r:
            self.stats.p1_score = 0
            self.stats.p2_score = 0
            self.stats.game_active = True

        # quit game
        elif event.key == pygame.K_ESCAPE:
            print("\n\tThanks for playing Pong !!!\n\n")
            sys.exit()

    def _shoot_ball(self):
        if len(self.balls) < self.settings.balls_allowed:
            
            new_ball = Ball(self)
            new_ball.ball_moving = True
            new_ball.ball_direction = 1
            self.balls.add(new_ball)

    def _balls_update(self):
        # when ball hit right or left edge of screen aka loosing point
        self.balls.update()
        self.scoring.prep_score()
        for ball in self.balls.copy():

            # right screen collision
            if ball.rect.right >= self.settings.screen_width:
                # remove bullets
                pygame.mixer.Sound.play(self.sounds.ball_lost)
                self.balls.remove(ball)
                self.stats.p1_score += 1
                self.stats.ball_owner = 1
                if self.stats.p1_score == self.settings.maxscore:
                    self.stats.winner = 1
                    self._game_end()

            # left screen collision
            if ball.rect.left <= 0:
                # remove bullets
                pygame.mixer.Sound.play(self.sounds.ball_lost)
                self.balls.remove(ball)
                self.stats.p2_score += 1
                self.stats.ball_owner = 2
                if self.stats.p2_score == self.settings.maxscore:
                    self.stats.winner = 2
                    self._game_end()

            # ball and pad colision detection pad 2
            if pygame.sprite.spritecollideany(self.p2, self.balls):
                pygame.mixer.Sound.play(self.sounds.ball_bounce)
                pad_collision_position = self._ball_contact_pad_pos(2, ball)
                ball.ball_direction = -1
                self._ball_controll(pad_collision_position)

            # ball and pad colision detection pad 1
            if pygame.sprite.spritecollideany(self.p1, self.balls):
                pygame.mixer.Sound.play(self.sounds.ball_bounce)
                pad_collision_position = self._ball_contact_pad_pos(1, ball)
                ball.ball_direction = 1
                self._ball_controll(pad_collision_position)

    def _game_end(self):
        self.stats.game_active = False

    def _ball_contact_pad_pos(self, padNum, ball):
        # detecting colision position on the pad
        if padNum == 2:
            padCheck = self.p2.y
        else:
            padCheck = self.p1.y
        if padCheck > ball.y:
            return int(padCheck - ball.y)
        else:
            return int(-1 * (padCheck - ball.y))

    # ball controll after pad contact
    def _ball_controll(self, pad_collision_position):
        if pad_collision_position < self.settings.pad_quater:
            self.settings.ball_angle = 1
        # if colision on 2nd quater
        if self.settings.pad_quater < pad_collision_position < (2 * self.settings.pad_quater):
            self.settings.ball_angle = 0.5
        # if colision on 3rd quater
        if (2 * self.settings.pad_quater) < pad_collision_position < (3 * self.settings.pad_quater):
            self.settings.ball_angle = 0.1
        # if colision on 4st quater
        if (3 * self.settings.pad_quater) < pad_collision_position < (4 * self.settings.pad_quater):
            self.settings.ball_angle = 1.3

    def _after_end(self, msg):
        self.scoring.prep_score()
        self.scoring.show_score()
        self.gameover.prep_message(msg)
        self.gameover.draw_message()
        msg_r = "PRESS R TO RESTART"
        self.start.prep_message(msg_r)
        self.start.draw_message()

    def _update_screen(self):
        # redraw screen on each loop
        self.screen.fill(self.settings.bg_color)
        self.p1.show_me()
        self.p2.show_me()

        for ball in self.balls.sprites():
            ball.draw_ball()

        self.scoring.show_score()
        if not self.stats.game_active:

            if self.stats.winner == 1:
                msg = "GAME OVER - PLAYER1 WINS !!!"
                self._after_end(msg)

            elif self.stats.winner == 2:
                msg = "GAME OVER - PLAYER2 WINS !!!"
                self._after_end(msg)

            elif self.stats.winner == 0:
                self.title.draw_message()
                msg = "SPACE: shoot, P1: W - up, S - down, P2: arrows"
                self.start.prep_message(msg)
                self.start.draw_message()
        # make recently rendered screen visible
        pygame.display.flip()


if __name__ == '__main__':
    p = Pong()
    p.run_game()
