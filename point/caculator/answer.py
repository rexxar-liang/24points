import random

from point.caculator import checker

possible_brackets = [(None, None, None, None, None, None),
                     ('(', None, ')', None, None, None),
                     (None, None, None, '(', None, ')'),
                     ('(', None, ')', '(', None, ')'),
                     (None, '(', None, None, ')', None),
                     ('(', None, None, None, ')', None),
                     (None, '(', None, None, None, ')')
                     ]
possible_number_index = [(0, 1, 2, 3),
                         (0, 1, 3, 2),
                         (0, 2, 1, 3),
                         (0, 2, 3, 1),
                         (0, 3, 1, 2),
                         (0, 3, 2, 1),
                         (1, 0, 2, 3),
                         (1, 0, 3, 2),
                         (1, 2, 0, 3),
                         (1, 2, 3, 0),
                         (1, 3, 0, 2),
                         (1, 3, 2, 0),
                         (2, 0, 1, 3),
                         (2, 0, 3, 1),
                         (2, 1, 0, 3),
                         (2, 1, 3, 0),
                         (2, 3, 0, 1),
                         (2, 3, 1, 0),
                         (3, 0, 1, 2),
                         (3, 0, 2, 1),
                         (3, 1, 0, 2),
                         (3, 1, 2, 0),
                         (3, 2, 0, 1),
                         (3, 2, 1, 0)
                         ]
symbols = ["plus", "minus", "mul", "div"]


def gen_possible_symbols():
    possible = []
    for symbol1 in symbols:
        for symbol2 in symbols:
            for symbol3 in symbols:
                possible.append((symbol1, symbol2, symbol3))
    return possible


def gen_possible_numbers(number1, number2, number3, number4):
    possible_numbers = []
    numbers = [number1, number2, number3, number4]
    for possible_index in possible_number_index:
        possible_number = (numbers[possible_index[0]],
                           numbers[possible_index[1]],
                           numbers[possible_index[2]],
                           numbers[possible_index[3]]
                           )
        if possible_number not in possible_numbers:
            possible_numbers.append(possible_number)
    return possible_numbers


def symbol_string(symbol):
    if symbol == "plus":
        return '+'
    if symbol == "minus":
        return '-'
    if symbol == "mul":
        return '*'
    if symbol == "div":
        return '/'


def to_string(answer):
    number1 = answer[0]
    number2 = answer[1]
    number3 = answer[2]
    number4 = answer[3]
    symbol1 = answer[4]
    symbol2 = answer[5]
    symbol3 = answer[6]
    bracket1 = answer[7]
    bracket2 = answer[8]
    bracket3 = answer[9]
    bracket4 = answer[10]
    bracket5 = answer[11]
    bracket6 = answer[12]
    answer_str = ""
    if bracket1 is not None:
        answer_str += '('
    answer_str += str(number1)
    answer_str += symbol_string(symbol1)
    if bracket2 is not None:
        answer_str += '('
    answer_str += str(number2)
    if bracket3 is not None:
        answer_str += ')'
    answer_str += symbol_string(symbol2)
    if bracket4 is not None:
        answer_str += '('
    answer_str += str(number3)
    if bracket5 is not None:
        answer_str += ')'
    answer_str += symbol_string(symbol3)
    answer_str += str(number4)
    if bracket6 is not None:
        answer_str += ')'
    return answer_str


class Answer:
    def __init__(self):
        self.possible_symbols = gen_possible_symbols()
        self.correct_answers = None

    def gen_possible_answers(self, number1, number2, number3, number4):
        possible_answers = []

        possible_numbers = gen_possible_numbers(number1, number2, number3, number4)
        for possible_number in possible_numbers:
            for possible_symbol in self.possible_symbols:
                for possible_bracket in possible_brackets:
                    possible_answer = possible_number + possible_symbol + possible_bracket
                    possible_answers.append(possible_answer)
        return possible_answers

    def get_answers(self, number1, number2, number3, number4):
        correct_answers = []
        possible_answers = self.gen_possible_answers(number1, number2, number3, number4)
        for possible_answer in possible_answers:
            correct = checker.check_only(possible_answer[0],
                                         possible_answer[1],
                                         possible_answer[2],
                                         possible_answer[3],
                                         possible_answer[4],
                                         possible_answer[5],
                                         possible_answer[6],
                                         possible_answer[7],
                                         possible_answer[8],
                                         possible_answer[9],
                                         possible_answer[10],
                                         possible_answer[11],
                                         possible_answer[12])
            if correct and possible_answer not in correct_answers:
                correct_answers.append(possible_answer)
        self.correct_answers = correct_answers
        return correct_answers

    def get_one_answer(self):
        if not self.correct_answers:
            return ""
        count = len(self.correct_answers)
        index = random.randint(1, count)
        answer = self.correct_answers[index]
        return to_string(answer)
