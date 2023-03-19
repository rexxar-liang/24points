import pygame as pg

from point.config.setting import Settings


class Timer:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.bg_color = self.settings.timer_bg_color
        self.timer_text_color = self.settings.timer_text_color
        self.width = self.settings.timer_width
        self.height = self.settings.timer_height
        self.timer_text = self.settings.timer_text
        self.font = pg.font.SysFont(None, 45)
        self.timer_pos = self.settings.timer_pos

        self.timer_rect = pg.Rect(self.timer_pos[0], self.timer_pos[1], self.width, self.height)

        self.counter = self.settings.timer_counts

        pg.time.set_timer(self.settings.EVENT_TIMING, self.settings.timer_interval)

    def blitme(self):
        timer_image = self.font.render(self.timer_text + str(self.counter), True, self.timer_text_color, self.bg_color)
        timer_image_rect = timer_image.get_rect()
        timer_image_rect.center = self.timer_rect.center
        self.screen.fill(self.bg_color, self.timer_rect)
        self.screen.blit(timer_image, timer_image_rect)

    def restart(self):
        self.counter = self.settings.timer_counts

    def update(self):
        if self.counter > 0:
            self.counter = self.counter - 1
            return False
        else:
            self.counter = self.settings.timer_counts
            return True
