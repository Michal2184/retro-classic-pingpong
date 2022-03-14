import pygame


class Pad:
    def __init__(self, pong):
        self.screen = pong.screen
        self.screen_rect = pong.screen.get_rect()
        self.color = pong.settings.pad_color
        # changing y position to float
        self.setting = pong.settings
        self.moving_down = False
        self.moving_up = False

    def show_me(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        # update position based on the movment
        if self.moving_up and self.rect.y > self.screen_rect.top:
            self.y -= self.setting.pad_speed

        if self.moving_down and self.rect.y < (self.screen_rect.bottom - self.setting.pad_height):
            self.y += self.setting.pad_speed

        # update Y position
        self.rect.y = self.y


# both players inherits from Pad ( do all changes in Parent Class )
class Player1(Pad):
    def __init__(self, pong):
        super(Player1, self).__init__(pong)
        # render ships pixel positions
        self.rect = pygame.Rect(10, 260, pong.settings.pad_width, pong.settings.pad_height)
        self.y = float(self.rect.y)


class Player2(Pad):
    def __init__(self, pong):
        super(Player2, self).__init__(pong)
        # render ships pixel positions
        self.rect = pygame.Rect((pong.settings.screen_width - 20), 260, pong.settings.pad_width, pong.settings.pad_height)
        self.y = float(self.rect.y)


