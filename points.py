import sys
import pygame as pg
import random
import tkinter
from tkinter import messagebox

from setting import Settings
from symbols import Symbol
from selected_symbol import SelectedSymbol
from numbers import Number
from selected_number import SelectedNumber
from button import Button
from grading import Grading


class Points:

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.select_number = None
        self.select_symbol = None
        self.selected_number = None
        self.last_selected_symbol = None

        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("24点")

        self.bg_color = (230, 230, 230)
        self.symbol1 = Symbol(self, 'plus')
        self.symbol2 = Symbol(self, 'minus')
        self.symbol3 = Symbol(self, 'mul')
        self.symbol4 = Symbol(self, 'div')

        self.selected_symbol1 = SelectedSymbol(self, 1)
        self.selected_symbol2 = SelectedSymbol(self, 2)
        self.selected_symbol3 = SelectedSymbol(self, 3)

        self.number1 = Number(self, 1, random.randint(1, 10))
        self.number2 = Number(self, 2, random.randint(1, 10))
        self.number3 = Number(self, 3, random.randint(1, 10))
        self.number4 = Number(self, 4, random.randint(1, 10))

        self.selected_number1 = SelectedNumber(self, 1)
        self.selected_number2 = SelectedNumber(self, 2)
        self.selected_number3 = SelectedNumber(self, 3)
        self.selected_number4 = SelectedNumber(self, 4)

        self.check_button = Button(self, (497, 630), "Check")
        self.next_button = Button(self, (680, 630), "Next")

        self.grading = Grading(self, (950, 0))

    def _check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                self.check_button.unselect()
                self.next_button.unselect()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.symbol1.update(event.pos)
                self.symbol2.update(event.pos)
                self.symbol3.update(event.pos)
                self.selected_symbol1.update(event.pos)
                self.selected_symbol2.update(event.pos)
                self.selected_symbol3.update(event.pos)
                self.symbol4.update(event.pos)
                self.number1.update(event.pos)
                self.number2.update(event.pos)
                self.number3.update(event.pos)
                self.number4.update(event.pos)
                self.selected_number1.update(event.pos)
                self.selected_number2.update(event.pos)
                self.selected_number3.update(event.pos)
                self.selected_number4.update(event.pos)
                self.check_button.update(event.pos)
                self.next_button.update(event.pos)

                if self.next_button.is_selected():
                    self._next_round()

                if self.check_button.is_selected():
                    result = self.grading.check(self.selected_number1.number,
                                                self.selected_number2.number,
                                                self.selected_number3.number,
                                                self.selected_number4.number,
                                                self.selected_symbol1.symbol,
                                                self.selected_symbol2.symbol,
                                                self.selected_symbol3.symbol)
                    if result:
                        print("Correct!")
                        self._next_round()
                    else:
                        print("Fault!")

                if self.symbol1.is_selected():
                    self.select_symbol = self.symbol1
                if self.symbol2.is_selected():
                    self.select_symbol = self.symbol2
                if self.symbol3.is_selected():
                    self.select_symbol = self.symbol3
                if self.symbol4.is_selected():
                    self.select_symbol = self.symbol4

                if self.selected_symbol1.is_selected():
                    if not self.last_selected_symbol:
                        self.last_selected_symbol = self.selected_symbol1
                if self.selected_symbol2.is_selected():
                    if not self.last_selected_symbol:
                        self.last_selected_symbol = self.selected_symbol2
                if self.selected_symbol3.is_selected():
                    if not self.last_selected_symbol:
                        self.last_selected_symbol = self.selected_symbol3

                if self.number1.is_selected() and self.number1.number:
                    self.select_number = self.number1
                if self.number2.is_selected() and self.number2.number:
                    self.select_number = self.number2
                if self.number3.is_selected() and self.number3.number:
                    self.select_number = self.number3
                if self.number4.is_selected() and self.number4.number:
                    self.select_number = self.number4

                if self.selected_number1.is_selected() and self.selected_number1.number:
                    self.selected_number = self.selected_number1
                if self.selected_number2.is_selected() and self.selected_number2.number:
                    self.selected_number = self.selected_number2
                if self.selected_number3.is_selected() and self.selected_number3.number:
                    self.selected_number = self.selected_number3
                if self.selected_number4.is_selected() and self.selected_number4.number:
                    self.selected_number = self.selected_number4

                if self.select_symbol:
                    symbol = self.select_symbol.symbol
                    if self.selected_symbol1.is_selected():
                        self.selected_symbol1.set_symbol(symbol)
                        self.selected_symbol1.unselect()
                        self.select_symbol = None
                        self.last_selected_symbol = None
                    if self.selected_symbol2.is_selected():
                        self.selected_symbol2.set_symbol(symbol)
                        self.selected_symbol2.unselect()
                        self.select_symbol = None
                        self.last_selected_symbol = None
                    if self.selected_symbol3.is_selected():
                        self.selected_symbol3.set_symbol(symbol)
                        self.selected_symbol3.unselect()
                        self.select_symbol = None
                        self.last_selected_symbol = None

                if self.last_selected_symbol:
                    symbol = self.last_selected_symbol.symbol
                    if self.selected_symbol1.is_selected() and symbol != self.selected_symbol1.symbol:
                        self.last_selected_symbol.set_symbol(self.selected_symbol1.symbol)
                        self.selected_symbol1.set_symbol(symbol)
                        self.selected_symbol1.unselect()
                        self.select_symbol = None
                        self.last_selected_symbol = None
                    if self.selected_symbol2.is_selected() and symbol != self.selected_symbol2.symbol:
                        self.last_selected_symbol.set_symbol(self.selected_symbol2.symbol)
                        self.selected_symbol2.set_symbol(symbol)
                        self.selected_symbol2.unselect()
                        self.select_symbol = None
                        self.last_selected_symbol = None
                    if self.selected_symbol3.is_selected() and symbol != self.selected_symbol3.symbol:
                        self.last_selected_symbol.set_symbol(self.selected_symbol3.symbol)
                        self.selected_symbol3.set_symbol(symbol)
                        self.selected_symbol3.unselect()
                        self.select_symbol = None
                        self.last_selected_symbol = None

                if self.select_number:
                    number = self.select_number.number
                    if self.selected_number1.is_selected():
                        self.select_number.set_number(self.selected_number1.number)
                        self.selected_number1.set_number(number)
                        self.selected_number1.unselect()
                        self.select_number = None
                        self.selected_number = None
                    if self.selected_number2.is_selected():
                        self.select_number.set_number(self.selected_number2.number)
                        self.selected_number2.set_number(number)
                        self.selected_number2.unselect()
                        self.select_number = None
                        self.selected_number = None
                    if self.selected_number3.is_selected():
                        self.select_number.set_number(self.selected_number3.number)
                        self.selected_number3.set_number(number)
                        self.selected_number3.unselect()
                        self.select_number = None
                        self.selected_number = None
                    if self.selected_number4.is_selected():
                        self.select_number.set_number(self.selected_number4.number)
                        self.selected_number4.set_number(number)
                        self.selected_number4.unselect()
                        self.select_number = None
                        self.selected_number = None

                if self.selected_number:
                    number = self.selected_number.number
                    if self.number1.is_selected():
                        self.selected_number.set_number(self.number1.number)
                        self.number1.set_number(number)
                        self.number1.unselect()
                        self.select_number = None
                        self.selected_number = None
                    if self.number2.is_selected():
                        self.selected_number.set_number(self.number2.number)
                        self.number2.set_number(number)
                        self.number2.unselect()
                        self.select_number = None
                        self.selected_number = None
                    if self.number3.is_selected():
                        self.selected_number.set_number(self.number3.number)
                        self.number3.set_number(number)
                        self.number3.unselect()
                        self.select_number = None
                        self.selected_number = None
                    if self.number4.is_selected():
                        self.selected_number.set_number(self.number4.number)
                        self.number4.set_number(number)
                        self.number4.unselect()
                        self.select_number = None
                        self.selected_number = None

    def _next_round(self):
        self.number1.set_number(random.randint(1, 10))
        self.number2.set_number(random.randint(1, 10))
        self.number3.set_number(random.randint(1, 10))
        self.number4.set_number(random.randint(1, 10))
        self.selected_number1.set_number(None)
        self.selected_number2.set_number(None)
        self.selected_number3.set_number(None)
        self.selected_number4.set_number(None)
        self.selected_symbol1.set_symbol(None)
        self.selected_symbol2.set_symbol(None)
        self.selected_symbol3.set_symbol(None)

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
        self.check_button.blitme()
        self.next_button.blitme()
        self.grading.blitme()
        pg.display.flip()

    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()
