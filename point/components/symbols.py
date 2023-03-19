
import pygame as pg

from point.config.setting import Settings


class Symbol:

    def __init__(self, game, index):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.selected = False
        self.bg_color = self.settings.symbol_bg_color
        self.width = self.settings.symbol_width
        self.height = self.settings.symbol_height
        self.pos = self.settings.symbol_pos
        self.selected_border = self.settings.selected_border
        self.symbol = self.settings.symbol[index - 1]

        self.image = pg.image.load("images/symbols/" + self.symbol + ".png")
        self.bg_rect = pg.Rect(self.pos[index - 1][0],
                               self.pos[index - 1][1],
                               self.width + self.selected_border * 2,
                               self.height + self.selected_border * 2)
        self.image_rect = pg.Rect(self.pos[index - 1][0] + self.selected_border,
                                  self.pos[index - 1][1] + self.selected_border,
                                  self.width,
                                  self.height)

        self.image = pg.transform.scale(self.image, (self.width, self.height))

    def blitme(self):
        pg.draw.rect(self.screen, self.bg_color, self.bg_rect)
        self.screen.blit(self.image, self.image_rect)

    def update(self, pos):
        if self._check_selected(pos):
            self._select()
        else:
            self._unselect()

    def _check_selected(self, pos):
        return self.image_rect.collidepoint(pos)

    def is_selected(self):
        return self.selected

    def _select(self):
        self.selected = True
        self.bg_color = self.settings.selected_color

    def _unselect(self):
        self.selected = False
        self.bg_color = self.settings.symbol_bg_color

    def cancel_select(self):
        self.selected = False
        self.bg_color = self.settings.symbol_bg_color
