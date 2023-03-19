import pygame as pg

from setting import Settings


class Grading:

    def __init__(self, game, pos):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.bg_color = self.settings.score_bg_color
        self.score_text_color = self.settings.score_text_color
        self.width = self.settings.score_width
        self.height = self.settings.score_height
        self.font = pg.font.SysFont(None, 45)

        self.score_rect = pg.Rect(pos[0], pos[1], self.width, self.height)

        self.score = 0
        pg.mixer.init()
        pg.mixer.music.set_volume(1)

        pass
    # 先画计算总分的文本框，再把分数信息打进框的正中间
    def blitme(self):
        score_image = self.font.render("Total Score: " + str(self.score), True, self.score_text_color, self.bg_color)
        score_image_rect = score_image.get_rect()
        score_image_rect.center = self.score_rect.center
        self.screen.fill(self.bg_color, self.score_rect)
        self.screen.blit(score_image, score_image_rect)

    # 播放音乐，如果成功，播放正确音乐，否则播放错误音乐
    def _play_music(self, correct):
        if correct:
            pg.mixer.music.load("sound/correct.wav")
        else:
            pg.mixer.music.load("sound/fault.wav")

        pg.mixer.music.play()

    # 判断符号优先级，先乘除后加减
    def _higher(self, symbol):
        if (symbol == 'plus' or symbol == 'minus'):
            return False
        else:
            return True

    # 计算两个数的加减乘除的数值
    def _caculate(self, number1, number2, symbol):
        if symbol == "plus":
            return number1 + number2
        elif symbol == "minus":
            return number1 - number2
        elif symbol == "mul":
            return number1 * number2
        elif symbol == "div":
            return number1 / number2

    # 穷举所有的可能出现的运算优先级顺序，计算结果是否等于24，如果等于返回True，否则返回False
    def _check(self, number1, number2, number3, number4, symbol1, symbol2, symbol3):
        # * * *  1 2 3 4
        if self._higher(symbol1) and self._higher(symbol2) and self._higher(symbol3):
            return 24.0 == self._caculate(self._caculate(self._caculate(number1, number2, symbol1), number3, symbol2), number4, symbol3)
        # * * +  1 2 3 4
        elif self._higher(symbol1) and self._higher(symbol2) and not self._higher(symbol3):
            return 24.0 == self._caculate(self._caculate(self._caculate(number1, number2, symbol1), number3, symbol2), number4, symbol3)
        # * + *  1 2    3 4
        elif self._higher(symbol1) and not self._higher(symbol2) and self._higher(symbol3):
            return 24.0 == self._caculate(self._caculate(number1, number2, symbol1), self._caculate(number3, number4, symbol3), symbol2)
        # * + +  1 2 3 4
        elif self._higher(symbol1) and not self._higher(symbol2) and not self._higher(symbol3):
            return 24.0 == self._caculate(self._caculate(self._caculate(number1, number2, symbol1), number3, symbol2), number4, symbol3)
        # + * *  2 3  4
        elif not self._higher(symbol1) and self._higher(symbol2) and self._higher(symbol3):
            return 24.0 == self._caculate(number1, self._caculate(self._caculate(number2, number3, symbol2), number4, symbol3), symbol1)
        # + * +  2 3  1  4
        elif not self._higher(symbol1) and self._higher(symbol2) and not self._higher(symbol3):
            return 24.0 == self._caculate(self._caculate(number1, self._caculate(number2, number3, symbol2), symbol1), number4, symbol3)
        # + + *  3 4  1  2
        elif not self._higher(symbol1) and not self._higher(symbol2) and self._higher(symbol3):
            return 24.0 == self._caculate(self._caculate(number1, number2, symbol1), self._caculate(number3, number4, symbol3), symbol2)
        # + + +  1 2 3 4
        elif not self._higher(symbol1) and not self._higher(symbol2) and not self._higher(symbol3):
            return 24.0 == self._caculate(self._caculate(self._caculate(number1, number2, symbol1), number3, symbol2), number4, symbol3)

    # Check按钮的处理函数，计算是否24，如果有空的格子，直接返回错误，如果计算正确，总分加10分
    def check(self, number1, number2, number3, number4, symbol1, symbol2, symbol3):
        if (number1 is None
                or number2 is None
                or number3 is None
                or number4 is None
                or symbol1 is None
                or symbol2 is None
                or symbol3 is None):
            self._play_music(False)
            return False

        #print(self._check(1, 2, 3, 4, "mul", "mul", "mul"))
        #print(self._check(3, 3, 2, 6, "mul", "mul", "plus"))
        #print(self._check(3, 4, 3, 4, "mul", "plus", "mul"))
        #print(self._check(3, 4, 6, 6, "mul", "plus", "plus"))
        #print(self._check(6, 2, 3, 3, "plus", "mul", "mul"))
        #print(self._check(6, 3, 4, 6, "plus", "mul", "plus"))
        #print(self._check(6, 6, 3, 4, "plus", "plus", "mul"))
        #print(self._check(6, 6, 6, 6, "plus", "plus", "plus"))

        result = self._check(number1, number2, number3, number4, symbol1, symbol2, symbol3)
        if result:
            self.score += 10

        self._play_music(result)
        return result

    # 获取玩家分数
    def get_score(self):
        return self.score

    def get_answer(self):
        pass
