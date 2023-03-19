import pygame as pg

from setting import Settings


class Bracket:

    def __init__(self, game, index):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.selected = False
        self.width = self.settings.bracket_width
        self.height = self.settings.bracket_height
        self.bracket_color = self.settings.bracket_unselected_color
        self.bg_color = self.settings.bracket_bg_color
        self.pos = self.settings.bracket_pos
        self.font = pg.font.SysFont(None, 120)

        self.value = self.settings.bracket[index - 1]
        self.bracket_rect = pg.Rect(self.pos[index - 1][0], self.pos[index - 1][1], self.width, self.height)

    def blitme(self):
        bracket_image = self.font.render(str(self.value), True, self.bracket_color, self.bg_color)
        bracket_image_rect = bracket_image.get_rect()
        bracket_image_rect.center = self.bracket_rect.center
        self.screen.fill(self.bg_color, self.bracket_rect)
        self.screen.blit(bracket_image, bracket_image_rect)

    def update(self, pos):
        if self._check_selected(pos):
            if self.selected:
                self.unselect()
            else:
                self._select()

    def _check_selected(self, pos):
        return self.bracket_rect.collidepoint(pos)

    def is_selected(self):
        return self.selected

    def _select(self):
        self.selected = True
        self.bracket_color = self.settings.bracket_selected_color

    def unselect(self):
        self.selected = False
        self.bracket_color = self.settings.bracket_unselected_color
