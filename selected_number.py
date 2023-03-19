import sys
import pygame as pg

from setting import Settings


class SelectedNumber:

    def __init__(self, game, index):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.selected = False
        self.bg_color = self.settings.number_bg_color
        self.width = self.settings.number_width
        self.height = self.settings.number_height
        self.selected_border = self.settings.selected_border
        self.number = None
        self.image = None

        if index == 1:
            self.bg_rect = pg.Rect(200, 360, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(200 + self.selected_border, 360 + self.selected_border, self.width, self.height)
        elif index == 2:
            self.bg_rect = pg.Rect(440, 360, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(440 + self.selected_border, 360 + self.selected_border, self.width, self.height)
        elif index == 3:
            self.bg_rect = pg.Rect(680, 360, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(680 + self.selected_border, 360 + self.selected_border, self.width, self.height)
        elif index == 4:
            self.bg_rect = pg.Rect(920, 360, self.width + self.selected_border * 2, self.height + self.selected_border * 2)
            self.image_rect = pg.Rect(920 + self.selected_border, 360 + self.selected_border, self.width, self.height)
        else:
            print("Invalid Index!")
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
        if self.number:
            self.bg_color = self.settings.selected_color

    def unselect(self):
        self.selected = False
        self.bg_color = self.settings.number_bg_color

    def set_number(self, number):
        self.number = number
        if number:
            self.image = pg.image.load("images/numbers/" + str(number) + ".jpeg")
            self.image = pg.transform.scale(self.image, (self.width, self.height))
        else:
            self.image = None

    def unset_number(self):
        self.number = None
        self.image = None

