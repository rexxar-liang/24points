
import pygame as pg

from setting import Settings


class Button:

    def __init__(self, game, pos, msg):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.bg_color = self.settings.button_bg_color
        self.button_color = self.settings.button_color
        self.button_text_color = self.settings.button_text_color
        self.width = self.settings.button_width
        self.height = self.settings.button_height
        self.selected_border = self.settings.selected_border
        self.selected = False
        self.msg = msg
        self.font = pg.font.SysFont(None, 45)

        self.bg_rect = pg.Rect(pos[0], pos[1], self.width + self.selected_border * 2, self.height + self.selected_border * 2)
        self.button_rect = pg.Rect(pos[0] + self.selected_border, pos[1] + self.selected_border, self.width, self.height)
        self.msg_image = self.font.render(msg, True, self.button_text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center

    def blitme(self):
        self.screen.fill(self.bg_color, self.bg_rect)
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update(self, pos):
        if self._check_selected(pos):
            self._select()
        else:
            self.unselect()


    def _check_selected(self, pos):
        return self.button_rect.collidepoint(pos)

    def is_selected(self):
        return self.selected

    def _select(self):
        self.selected = True
        self.bg_color = self.settings.selected_color

    def unselect(self):
        self.selected = False
        self.bg_color = self.settings.button_bg_color
