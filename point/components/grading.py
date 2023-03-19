import pygame as pg

from point.config.setting import Settings
from point.caculator import checker


# 播放音乐，如果成功，播放正确音乐，否则播放错误音乐
def _play_music(correct):
    if correct:
        pg.mixer.music.load("sound/correct.wav")
    else:
        pg.mixer.music.load("sound/fault.wav")

    pg.mixer.music.play()


class Grading:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.bg_color = self.settings.score_bg_color
        self.score_text_color = self.settings.score_text_color
        self.width = self.settings.score_width
        self.height = self.settings.score_height
        self.font = pg.font.SysFont(None, 45)
        self.score_pos = self.settings.score_pos

        self.score_rect = pg.Rect(self.score_pos[0], self.score_pos[1], self.width, self.height)

        self.score = 0
        pg.mixer.init()
        pg.mixer.music.set_volume(1)

    # 先画计算总分的文本框，再把分数信息打进框的正中间
    def blitme(self):
        score_image = self.font.render("Total Score: " + str(self.score), True, self.score_text_color, self.bg_color)
        score_image_rect = score_image.get_rect()
        score_image_rect.center = self.score_rect.center
        self.screen.fill(self.bg_color, self.score_rect)
        self.screen.blit(score_image, score_image_rect)

    # Check按钮的处理函数，计算是否24，如果有空的格子，直接返回错误，如果计算正确，总分加10分
    def check(self, number1, number2, number3, number4,
              symbol1, symbol2, symbol3,
              bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
        # checker.test_check()
        result = checker.check(number1, number2, number3, number4,
                               symbol1, symbol2, symbol3,
                               bracket1, bracket2, bracket3, bracket4, bracket5, bracket6)
        if result:
            self.score += 10

        _play_music(result)
        return result

    # 获取玩家分数
    def get_score(self):
        return self.score
