import sys
import pygame as pg

from setting import Settings


class SelectedSymbol:

    def __init__(self, game, index):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.selected = False
        self.bg_color = self.settings.symbol_bg_color
        self.width = self.settings.symbol_width
        self.height = self.settings.symbol_height
        self.selected_border = self.settings.selected_border
        self.symbol = None
        self.image = None

        if index == 1:
            self.bg_rect = pg.Rect(373, 460, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(373 + self.selected_border, 460 + self.selected_border, self.width, self.height)
        elif index == 2:
            self.bg_rect = pg.Rect(613, 460, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(613 + self.selected_border, 460 + self.selected_border, self.width, self.height)
        elif index == 3:
            self.bg_rect = pg.Rect(853, 460, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(853 + self.selected_border, 460 + self.selected_border, self.width, self.height)
        else:
            print("Invalid Symbol Index!")
            sys.exit()

    def blitme(self):
        pg.draw.rect(self.screen, self.bg_color, self.bg_rect)
        if self.image:
            self.screen.blit(self.image, self.image_rect)

    def update(self, pos):
        if self._check_selected(pos):
            self._select()
        else:
            self.unselect()

    def _check_selected(self, pos):
        return self.image_rect.collidepoint(pos)

    def is_selected(self):
        return self.selected

    def _select(self):
        self.selected = True
        if self.symbol:
            self.bg_color = self.settings.selected_color

    def unselect(self):
        self.selected = False
        self.bg_color = self.settings.symbol_bg_color

    def cancel_select(self):
        self.selected = False
        self.bg_color = self.settings.symbol_bg_color

    def set_symbol(self, symbol):
        self.symbol = symbol
        if symbol:
            self.image = pg.image.load("images/symbols/" + symbol + ".png")
            self.image = pg.transform.scale(self.image, (self.width, self.height))
        else:
            self.image = None
