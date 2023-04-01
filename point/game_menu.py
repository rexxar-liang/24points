import pygame_menu as game_menu

from point.config.setting import Settings

RANKING_FIELDS = {"name": "Name", "score": "Score", "date": "Time"}
RANKING_LIST_MIN_ROW = 6


class GameMenu:

    def __init__(self, game):
        self.game = game
        self.settings = Settings()
        self.font_file = self.settings.font_file

    def about_menu(self):
        menu = game_menu.Menu(
            center_content=False,
            height=300,
            mouse_visible=True,
            theme=game_menu.themes.THEME_BLUE,
            title='About',
            width=600,
            rows=6,
            columns=2
        )

        menu.add.label("  Author:", font_name=self.font_file)
        menu.add.label("", font_name=self.font_file)
        menu.add.label("  Artist:", font_name=self.font_file)
        menu.add.label("  Code:  ", font_name=self.font_file)
        menu.add.label("", font_name=self.font_file)
        menu.add.label("")
        menu.add.url(href="https://github.com/rexxar-liang", align=game_menu.locals.ALIGN_LEFT, title="Rexxar Liang",
                     font_name=self.font_file)
        menu.add.url(href="https://github.com/Anduin-Liang", align=game_menu.locals.ALIGN_LEFT, title="Anduin Liang",
                     font_name=self.font_file)
        menu.add.label(title="m_marguerite", align=game_menu.locals.ALIGN_LEFT, font_name=self.font_file)
        menu.add.url(href="https://github.com/rexxar-liang/24points", align=game_menu.locals.ALIGN_LEFT,
                     title="rexxar-liang/24points",
                     font_name=self.font_file)
        menu.add.label("", font_name=self.font_file)
        menu.add.button('Return to Menu', game_menu.events.BACK, align=game_menu.locals.ALIGN_LEFT)
        return menu

    def ranking_menu(self):
        ranking_theme = game_menu.themes.THEME_BLUE.copy()
        ranking_theme.scrollbar_cursor = game_menu.locals.CURSOR_HAND

        ranking_list = self.game.ranking.get_ranking_list()
        ranking_list.insert(0, RANKING_FIELDS)
        ranking_menu = game_menu.Menu(
            columns=4,
            height=400,
            onclose=game_menu.events.EXIT,
            rows=max(RANKING_LIST_MIN_ROW + 1, len(ranking_list) + 1),
            theme=ranking_theme,
            title='Ranking',
            width=600
        )

        ranking_menu.add.label("NO.", font_name=self.font_file)
        for i in range(1, len(ranking_list)):
            ranking_menu.add.label(str(i), font_name=self.font_file)
        if len(ranking_list) < RANKING_LIST_MIN_ROW:
            for i in range(len(ranking_list), RANKING_LIST_MIN_ROW):
                ranking_menu.add.label("")
        ranking_menu.add.label("")
        for ranking in ranking_list:
            ranking_menu.add.label(ranking.get("name"), font_name=self.font_file)
        if len(ranking_list) < RANKING_LIST_MIN_ROW:
            for i in range(len(ranking_list), RANKING_LIST_MIN_ROW):
                ranking_menu.add.label("")
        ranking_menu.add.label("")
        for ranking in ranking_list:
            ranking_menu.add.label(ranking.get("score"), font_name=self.font_file)
        if len(ranking_list) < RANKING_LIST_MIN_ROW:
            for i in range(len(ranking_list), RANKING_LIST_MIN_ROW):
                ranking_menu.add.label("")
        ranking_menu.add.button('Return to Menu', game_menu.events.BACK, font_name=self.font_file)
        for ranking in ranking_list:
            ranking_menu.add.label(ranking.get("date"), font_name=self.font_file)
        if len(ranking_list) < RANKING_LIST_MIN_ROW:
            for i in range(len(ranking_list), RANKING_LIST_MIN_ROW):
                ranking_menu.add.label("")
        ranking_menu.add.label("")

        return ranking_menu

    def show_menu(self):
        menu = game_menu.Menu('Welcome', 400, 300,
                              theme=game_menu.themes.THEME_BLUE)

        menu.add.button('Play', self.game.play)
        menu.add.button('Ranking', self.ranking_menu())
        menu.add.button("About", self.about_menu())
        menu.add.button('Quit', game_menu.events.EXIT)
        menu.mainloop(self.game.screen)
