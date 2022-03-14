import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, pong):
        super().__init__()
        self.screen = pong.screen
        self.screen_rect = pong.screen.get_rect()
        self.settings = pong.settings
        self.stats = pong.stats
        self.color = pong.settings.ball_color
        self.ball_moving = True
        self.ball_direction = 1  # -1 for player2
        self.moving_x = 1
        self.moving_y = -1
        # Create bullet react
        self.rect = pygame.Rect(0, 0, self.settings.ball_width, self.settings.ball_height)

        # set ball position to P1
        if self.stats.ball_owner == 2:
            self.rect.midleft = pong.p2.rect.midleft
        if self.stats.ball_owner == 1:
            self.rect.midleft = pong.p1.rect.midleft


        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        # Ball movment
        if self.ball_moving:
            if self.ball_direction == 1:   # if ball right to left movment
                self.x += self.settings.ball_speed
                self.y += self.moving_y * (self.settings.ball_speed * self.settings.ball_angle)
                # change dir on top collision
                if self.y > self.screen_rect.bottom:
                   self.moving_y = -1
                # change direction on bottom colision
                if self.y < self.screen_rect.top:
                    self.moving_y = 1
            if self.ball_direction == -1:
                self.x -= self.settings.ball_speed
                self.y += self.moving_y * (self.settings.ball_speed * self.settings.ball_angle)
                # change dir on top collision
                if self.y > self.screen_rect.bottom:
                    self.moving_y = -1
                # change direction on bottom colision
                if self.y < self.screen_rect.top:
                    self.moving_y = 1


        # update X and Y position
        self.rect.x = self.x
        self.rect.y = self.y
        # print(f" X: {self.rect.x}    |     Y: {self.rect.y}\n")

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)