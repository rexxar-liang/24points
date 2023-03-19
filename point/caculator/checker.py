
def _validate_numbers(number1, number2, number3, number4):
    if (number1 is None
            or number2 is None
            or number3 is None
            or number4 is None):
        return False
    return True


def _validate_symbols(symbol1, symbol2, symbol3):
    if (symbol1 is None
            or symbol2 is None
            or symbol3 is None):
        return False
    return True


def _validate_brackets(bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
    if (bracket1 is None
            or bracket1 is None
            or bracket1 is None):
        return False
    return True


def _validate_inputs(number1, number2, number3, number4,
                     symbol1, symbol2, symbol3,
                     bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
    if not _validate_numbers(number1, number2, number3, number4):
        return False
    if not _validate_symbols(symbol1, symbol2, symbol3):
        return False
    # if not self._validate_brackets(bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
    # return False
    return True


# 判断符号优先级，先乘除后加减
def _higher(symbol):
    if symbol == 'plus' or symbol == 'minus':
        return False
    else:
        return True


# 计算两个数的加减乘除的数值
def _caculate(number1, number2, symbol):
    if symbol == "plus":
        return number1 + number2
    elif symbol == "minus":
        return number1 - number2
    elif symbol == "mul":
        return number1 * number2
    elif symbol == "div":
        return number1 / number2


# 穷举所有的可能出现的运算优先级顺序，计算结果是否等于24，如果等于返回True，否则返回False
def _check(number1, number2, number3, number4, symbol1, symbol2, symbol3):
    # * * *  1 2 3 4
    if _higher(symbol1) and _higher(symbol2) and _higher(symbol3):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2),
                                 number4, symbol3)
    # * * +  1 2 3 4
    elif _higher(symbol1) and _higher(symbol2) and not _higher(symbol3):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2),
                                 number4, symbol3)
    # * + *  1 2    3 4
    elif _higher(symbol1) and not _higher(symbol2) and _higher(symbol3):
        return 24.0 == _caculate(_caculate(number1, number2, symbol1),
                                 _caculate(number3, number4, symbol3), symbol2)
    # * + +  1 2 3 4
    elif _higher(symbol1) and not _higher(symbol2) and not _higher(symbol3):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2),
                                 number4, symbol3)
    # + * *  2 3  4
    elif not _higher(symbol1) and _higher(symbol2) and _higher(symbol3):
        return 24.0 == _caculate(number1,
                                 _caculate(_caculate(number2, number3, symbol2), number4, symbol3),
                                 symbol1)
    # + * +  2 3  1  4
    elif not _higher(symbol1) and _higher(symbol2) and not _higher(symbol3):
        return 24.0 == _caculate(_caculate(number1, _caculate(number2, number3, symbol2), symbol1),
                                 number4, symbol3)
    # + + *  3 4  1  2
    elif not _higher(symbol1) and not _higher(symbol2) and _higher(symbol3):
        return 24.0 == _caculate(_caculate(number1, number2, symbol1),
                                 _caculate(number3, number4, symbol3), symbol2)
    # + + +  1 2 3 4
    elif not _higher(symbol1) and not _higher(symbol2) and not _higher(symbol3):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2),
                                 number4, symbol3)


# Check按钮的处理函数，计算是否24，如果有空的格子，直接返回错误，如果计算正确，总分加10分
def check(number1, number2, number3, number4,
          symbol1, symbol2, symbol3,
          bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
    if not _validate_inputs(number1, number2, number3, number4,
                            symbol1, symbol2, symbol3,
                            bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
        return False

    # print(self._check(1, 2, 3, 4, "mul", "mul", "mul"))
    # print(self._check(3, 3, 2, 6, "mul", "mul", "plus"))
    # print(self._check(3, 4, 3, 4, "mul", "plus", "mul"))
    # print(self._check(3, 4, 6, 6, "mul", "plus", "plus"))
    # print(self._check(6, 2, 3, 3, "plus", "mul", "mul"))
    # print(self._check(6, 3, 4, 6, "plus", "mul", "plus"))
    # print(self._check(6, 6, 3, 4, "plus", "plus", "mul"))
    # print(self._check(6, 6, 6, 6, "plus", "plus", "plus"))

    return _check(number1, number2, number3, number4, symbol1, symbol2, symbol3)
