import sys
import pygame as pg
import random

from config.setting import Settings
from components.symbols import Symbol
from components.selected_symbol import SelectedSymbol
from components.numbers import Number
from components.selected_number import SelectedNumber
from components.button import Button
from components.bracket import Bracket
from components.grading import Grading
from components.timer import Timer

from caculator.answer import Answer
from ranking import Ranking


class Points:

    def __init__(self):
        self.ranking = Ranking()

        pg.init()
        self.settings = Settings()
        self.select_symbol = None
        self.last_selected_symbol = None
        self.current_selected_number = None
        self.last_selected_number = None

        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("24点")

        self.answer = Answer()

        self.bg_color = (230, 230, 230)
        self.symbol1 = Symbol(self, 1)
        self.symbol2 = Symbol(self, 2)
        self.symbol3 = Symbol(self, 3)
        self.symbol4 = Symbol(self, 4)

        self.selected_symbol1 = SelectedSymbol(self, 1)
        self.selected_symbol2 = SelectedSymbol(self, 2)
        self.selected_symbol3 = SelectedSymbol(self, 3)

        number1, number2, number3, number4 = self._gen_numbers()
        self.number1 = Number(self, 1, number1)
        self.number2 = Number(self, 2, number2)
        self.number3 = Number(self, 3, number3)
        self.number4 = Number(self, 4, number4)

        self.selected_number1 = SelectedNumber(self, 1)
        self.selected_number2 = SelectedNumber(self, 2)
        self.selected_number3 = SelectedNumber(self, 3)
        self.selected_number4 = SelectedNumber(self, 4)

        self.bracket1 = Bracket(self, 1)
        self.bracket2 = Bracket(self, 2)
        self.bracket3 = Bracket(self, 3)
        self.bracket4 = Bracket(self, 4)
        self.bracket5 = Bracket(self, 5)
        self.bracket6 = Bracket(self, 6)

        self.check_button = Button(self, self.settings.check_button_pos, "Check")
        self.next_button = Button(self, self.settings.next_button_pos, "Next")
        self.finish_button = Button(self, self.settings.finish_button_pos, "Finish")

        self.grading = Grading(self)
        self.timer = Timer(self)

    def _update(self, event):
        self.symbol1.update(event.pos)
        self.symbol2.update(event.pos)
        self.symbol3.update(event.pos)
        self.symbol4.update(event.pos)

        self.selected_symbol1.update(event.pos)
        self.selected_symbol2.update(event.pos)
        self.selected_symbol3.update(event.pos)

        self.number1.update(event.pos)
        self.number2.update(event.pos)
        self.number3.update(event.pos)
        self.number4.update(event.pos)

        self.selected_number1.update(event.pos)
        self.selected_number2.update(event.pos)
        self.selected_number3.update(event.pos)
        self.selected_number4.update(event.pos)

        self.bracket1.update(event.pos)
        self.bracket2.update(event.pos)
        self.bracket3.update(event.pos)
        self.bracket4.update(event.pos)
        self.bracket5.update(event.pos)
        self.bracket6.update(event.pos)

        self.check_button.update(event.pos)
        self.next_button.update(event.pos)
        self.finish_button.update(event.pos)

    def _try_button_action(self):
        if self.next_button.is_selected():
            self._next_round()
        elif self.finish_button.is_selected():
            self.ranking.add_new_record(self.grading.score)
            sys.exit()
        elif self.check_button.is_selected():
            result = self.grading.check(self.selected_number1.number,
                                        self.selected_number2.number,
                                        self.selected_number3.number,
                                        self.selected_number4.number,
                                        self.selected_symbol1.symbol,
                                        self.selected_symbol2.symbol,
                                        self.selected_symbol3.symbol,
                                        self.bracket1.bracket,
                                        self.bracket2.bracket,
                                        self.bracket3.bracket,
                                        self.bracket4.bracket,
                                        self.bracket5.bracket,
                                        self.bracket6.bracket)
            if result:
                print("Correct!")
                self._next_round()
            else:
                print("Fault!")

    def _try_symbol_exchange(self):
        if self.symbol1.is_selected():
            self.select_symbol = self.symbol1
        elif self.symbol2.is_selected():
            self.select_symbol = self.symbol2
        elif self.symbol3.is_selected():
            self.select_symbol = self.symbol3
        elif self.symbol4.is_selected():
            self.select_symbol = self.symbol4

        if self.selected_symbol1.is_selected():
            if not self.last_selected_symbol:
                self.last_selected_symbol = self.selected_symbol1
        elif self.selected_symbol2.is_selected():
            if not self.last_selected_symbol:
                self.last_selected_symbol = self.selected_symbol2
        elif self.selected_symbol3.is_selected():
            if not self.last_selected_symbol:
                self.last_selected_symbol = self.selected_symbol3

        if self.select_symbol and self.last_selected_symbol:
            symbol = self.select_symbol.symbol
            self.last_selected_symbol.set_symbol(symbol)
            self.last_selected_symbol.unselect()
            self.select_symbol = None
            self.last_selected_symbol = None

        # exchange between selected symbols
        if self.last_selected_symbol:
            symbol = self.last_selected_symbol.symbol
            if self.selected_symbol1.is_selected() and symbol != self.selected_symbol1.symbol:
                self.last_selected_symbol.set_symbol(self.selected_symbol1.symbol)
                self.selected_symbol1.set_symbol(symbol)
                self.selected_symbol1.unselect()
                self.select_symbol = None
                self.last_selected_symbol = None
            elif self.selected_symbol2.is_selected() and symbol != self.selected_symbol2.symbol:
                self.last_selected_symbol.set_symbol(self.selected_symbol2.symbol)
                self.selected_symbol2.set_symbol(symbol)
                self.selected_symbol2.unselect()
                self.select_symbol = None
                self.last_selected_symbol = None
            elif self.selected_symbol3.is_selected() and symbol != self.selected_symbol3.symbol:
                self.last_selected_symbol.set_symbol(self.selected_symbol3.symbol)
                self.selected_symbol3.set_symbol(symbol)
                self.selected_symbol3.unselect()
                self.select_symbol = None
                self.last_selected_symbol = None

    def _try_number_exchange(self):
        self.current_selected_number = None

        if self.number1.is_selected():
            self.current_selected_number = self.number1
        elif self.number2.is_selected():
            self.current_selected_number = self.number2
        elif self.number3.is_selected():
            self.current_selected_number = self.number3
        elif self.number4.is_selected():
            self.current_selected_number = self.number4
        elif self.selected_number1.is_selected():
            self.current_selected_number = self.selected_number1
        elif self.selected_number2.is_selected():
            self.current_selected_number = self.selected_number2
        elif self.selected_number3.is_selected():
            self.current_selected_number = self.selected_number3
        elif self.selected_number4.is_selected():
            self.current_selected_number = self.selected_number4

        if self.current_selected_number:
            if not self.last_selected_number:
                self.last_selected_number = self.current_selected_number
        else:
            self.last_selected_number = None

        if self.current_selected_number and self.last_selected_number:
            if not (self.current_selected_number.type == self.last_selected_number.type
                    and self.current_selected_number.index == self.last_selected_number.index):
                number = self.current_selected_number.number
                self.current_selected_number.set_number(self.last_selected_number.number)
                self.last_selected_number.set_number(number)
                self.last_selected_number.unselect()
                self.current_selected_number.unselect()
                self.current_selected_number = None
                self.last_selected_number = None

    def _check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                self.check_button.unselect()
                self.next_button.unselect()
                self.finish_button.unselect()
            elif event.type == self.settings.EVENT_TIMING:
                is_run_outof_time = self.timer.update()
                if is_run_outof_time:
                    self._next_round()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self._update(event)

                self._try_button_action()
                self._try_symbol_exchange()
                self._try_number_exchange()

    def _gen_numbers(self):
        answers = []
        number1, number2, number3, number4 = None, None, None, None
        while not answers:
            number1 = random.randint(1, 10)
            number2 = random.randint(1, 10)
            number3 = random.randint(1, 10)
            number4 = random.randint(1, 10)
            answers = self.answer.get_answers(number1, number2, number3, number4)
        print(self.answer.get_one_answer())
        return number1, number2, number3, number4

    def _next_round(self):
        number1, number2, number3, number4 = self._gen_numbers()

        self.number1.set_number(number1)
        self.number2.set_number(number2)
        self.number3.set_number(number3)
        self.number4.set_number(number4)

        self.selected_number1.set_number(None)
        self.selected_number2.set_number(None)
        self.selected_number3.set_number(None)
        self.selected_number4.set_number(None)
        self.selected_symbol1.set_symbol(None)
        self.selected_symbol2.set_symbol(None)
        self.selected_symbol3.set_symbol(None)
        self.bracket1.unselect()
        self.bracket2.unselect()
        self.bracket3.unselect()
        self.bracket4.unselect()
        self.bracket5.unselect()
        self.bracket6.unselect()
        self.timer.restart()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.symbol1.blitme()
        self.symbol2.blitme()
        self.symbol3.blitme()
        self.symbol4.blitme()
        self.selected_symbol1.blitme()
        self.selected_symbol2.blitme()
        self.selected_symbol3.blitme()
        self.number1.blitme()
        self.number2.blitme()
        self.number3.blitme()
        self.number4.blitme()
        self.selected_number1.blitme()
        self.selected_number2.blitme()
        self.selected_number3.blitme()
        self.selected_number4.blitme()
        self.bracket1.blitme()
        self.bracket2.blitme()
        self.bracket3.blitme()
        self.bracket4.blitme()
        self.bracket5.blitme()
        self.bracket6.blitme()
        self.check_button.blitme()
        self.next_button.blitme()
        self.finish_button.blitme()
        self.grading.blitme()
        self.timer.blitme()

        pg.display.flip()

    def play(self):
        while True:
            self._check_event()
            self._update_screen()
