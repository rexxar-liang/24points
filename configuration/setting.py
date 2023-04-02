import pygame


class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 740

        self.bg_color = (230, 230, 230)
        self.selected_color = (0, 255, 0)
        self.number_bg_color = (200, 200, 200)
        self.symbol_bg_color = (200, 200, 200)
        self.button_bg_color = (200, 200, 200)
        self.button_color = (128, 128, 128)
        self.button_text_color = (255, 255, 255)

        self.score_bg_color = self.bg_color
        self.score_text_color = (224, 64, 0)

        self.timer_bg_color = self.bg_color
        self.timer_text_color = (224, 64, 0)

        self.bracket_selected_color = (0, 0, 0)
        self.bracket_unselected_color = (200, 200, 200)
        self.bracket_bg_color = self.bg_color

        self.selected_border = 2
        self.symbol_width = 50
        self.symbol_height = 50
        self.number_width = 156
        self.number_height = 234
        self.button_width = 100
        self.button_height = 50

        self.score_width = 200
        self.score_height = 50

        self.timer_width = 100
        self.timer_height = 50

        self.bracket_width = 24
        self.bracket_height = 82

        self.symbol = ["plus", "minus", "mul", "div"]
        self.bracket = ['(', '(', ')', '(', ')', ')']
        self.symbol_pos = [(50, 60), (50, 120), (50, 180), (50, 240)]
        self.number_pos = [(160, 60), (430, 60), (710, 60), (965, 60)]
        self.selected_number_pos = [(160, 360), (420, 360), (710, 360), (965, 360)]
        self.selected_symbol_pos = [(330, 460), (620, 460), (900, 460)]
        self.bracket_pos = [(130, 446), (390, 446), (585, 446), (680, 446), (870, 446), (1130, 446)]
        self.score_pos = (950, 0)
        self.check_button_pos = (480, 630)
        self.next_button_pos = (707, 630)
        self.finish_button_pos = (1000, 630)

        self.timer_pos = (750, 0)
        self.timer_counts = 90
        self.timer_interval = 1000
        self.timer_text = "Time Left: "

        self.ranking_file = "ranking.json"
        self.max_ranking_list = 10

        self.EVENT_TIMING = pygame.USEREVENT + 1

        self.font_file = "./res/font/SimSun.ttf"
        self.number_path = "./res/images/numbers/"
        self.symbol_path = "./res/images/symbols/"
        self.sound_path = "./res/sound/"
