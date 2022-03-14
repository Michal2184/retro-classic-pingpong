import pygame.font

class Message:
    def __init__(self,pong):
        # get screen attributes
        self.screen = pong.screen
        self.screen_rect = self.screen.get_rect()

        # visual representation
        self.width = 100
        self.height = 30
        self.button_color = (255,255,255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font("fonts/Retro_Gaming.ttf", 18)
        # prepare container
        self.rect = pygame.Rect(0 ,0, self.width, self.height)

    def draw_message(self):
        # render to screen
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Title(Message):
    def __init__(self, pong):
        super(Title, self).__init__(pong)
        self.msg = "PONG GAME"
        self.rect.center = self.screen_rect.center
        self._prep_message(self.msg)

    def _prep_message(self, msg):
        # change to image and center text on top
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


class Start(Message):
    def __init__(self, pong):
        super(Start, self).__init__(pong)
        self.rect.midbottom = self.screen_rect.midbottom

    def prep_message(self, msg):
        # change to image and center text on top
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.midbottom = self.rect.midbottom
        # Manual offset
        self.msg_image_rect.y -= 100

class GameOver(Message):
    def __init__(self, pong):
        super(GameOver, self).__init__(pong)
        self.rect.center = self.screen_rect.center

    def prep_message(self, msg):
        # change to image and center text on top
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
