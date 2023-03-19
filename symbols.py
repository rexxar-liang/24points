import sys
import pygame as pg

from setting import Settings


class Symbol:

    def __init__(self, game, type):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.selected = False
        self.bg_color = self.settings.symbol_bg_color
        self.width = self.settings.symbol_width
        self.height = self.settings.symbol_height
        self.selected_border = self.settings.selected_border
        self.symbol = type

        if type == 'plus':
            self.image = pg.image.load("images/symbols/plus.png")
            self.bg_rect = pg.Rect(50, 60, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(50 + self.selected_border, 60 + self.selected_border, self.width, self.height)
        elif type == 'minus':
            self.image = pg.image.load("images/symbols/minus.png")
            self.bg_rect = pg.Rect(50, 120, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(50 + self.selected_border, 120 + self.selected_border, self.width, self.height)
        elif type == 'mul':
            self.image = pg.image.load("images/symbols/mul.png")
            self.bg_rect = pg.Rect(50, 180, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(50 + self.selected_border, 180 + self.selected_border, self.width, self.height)
        elif type == 'div':
            self.image = pg.image.load("images/symbols/div.png")
            self.bg_rect = pg.Rect(50, 240, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(50 + self.selected_border, 240 + self.selected_border, self.width, self.height)
        else:
            print("Invalid Symbol Type!")
            sys.exit()

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
