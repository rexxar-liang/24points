invaild_number = 1000000


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


valid_brackets = [(None, None, None, None, None, None),
                  ('(', None, None, None, None, ')'),
                  ('(', None, ')', None, None, None),
                  (None, None, None, '(', None, ')'),
                  ('(', None, ')', '(', None, ')'),
                  (None, '(', None, None, ')', None),
                  ('(', None, None, None, ')', None),
                  (None, '(', None, None, None, ')')
                  ]


def _validate_brackets(bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
    brackets = (bracket1, bracket2, bracket3, bracket4, bracket5, bracket6)
    if brackets in valid_brackets:
        return True

    return False


def _validate_inputs(number1, number2, number3, number4,
                     symbol1, symbol2, symbol3,
                     bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
    if not _validate_numbers(number1, number2, number3, number4):
        return False
    if not _validate_symbols(symbol1, symbol2, symbol3):
        return False
    if not _validate_brackets(bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
        return False
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
        if number2 == 0:
            return invaild_number
        else:
            return number1 / number2


# 穷举如下所有的可能出现的运算优先级顺序，计算结果是否等于24，如果等于返回True，否则返回False
# number symbol number symbol number symbol number
# (number symbol number symbol number symbol number)
def _check1(number1, number2, number3, number4, symbol1, symbol2, symbol3):
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


# (number symbol number) symbol number symbol number
def _check2(number1, number2, number3, number4, symbol1, symbol2, symbol3):
    # (number symbol number) * number * number
    if _higher(symbol2) and _higher(symbol3):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2),
                                 number4, symbol3)
    # (number symbol number) * number + number
    if _higher(symbol2) and not _higher(symbol3):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2),
                                 number4, symbol3)
    # (number symbol number) + number * number
    if not _higher(symbol2) and _higher(symbol3):
        return 24.0 == _caculate(_caculate(number1, number2, symbol1), _caculate(number3, number4, symbol3), symbol2)
    # (number symbol number) + number + number
    if not _higher(symbol2) and not _higher(symbol3):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2),
                                 number4, symbol3)


# number symbol number symbol (number symbol number)
def _check3(number1, number2, number3, number4, symbol1, symbol2, symbol3):
    # number * number * (number symbol number)
    if _higher(symbol1) and _higher(symbol2):
        return 24.0 == _caculate(_caculate(number1, number2, symbol1), _caculate(number3, number4, symbol3), symbol2)
    # number * number + (number symbol number)
    if _higher(symbol1) and not _higher(symbol2):
        return 24.0 == _caculate(_caculate(number1, number2, symbol1), _caculate(number3, number4, symbol3), symbol2)
    # number + number * (number symbol number)
    if not _higher(symbol1) and _higher(symbol2):
        return 24.0 == _caculate(number1, _caculate(number2, _caculate(number3, number4, symbol3), symbol2), symbol1)
    # number + number + (number symbol number)
    if not _higher(symbol1) and not _higher(symbol2):
        return 24.0 == _caculate(_caculate(number1, number2, symbol1), _caculate(number3, number4, symbol3), symbol2)


# (number symbol number) symbol (number symbol number)
def _check4(number1, number2, number3, number4, symbol1, symbol2, symbol3):
    # (number * number) * (number symbol number)
    # (number * number) + (number symbol number)
    return 24.0 == _caculate(_caculate(number1, number2, symbol1), _caculate(number3, number4, symbol3), symbol2)


# number symbol (number symbol number) symbol number
def _check5(number1, number2, number3, number4, symbol1, symbol2, symbol3):
    # number * (number symbol number) * number)
    if _higher(symbol1) and _higher(symbol3):
        return 24.0 == _caculate(_caculate(number1, _caculate(number2, number3, symbol2), symbol1), number4, symbol3)
    # number * (number symbol number) + number)
    if _higher(symbol1) and not _higher(symbol3):
        return 24.0 == _caculate(_caculate(number1, _caculate(number2, number3, symbol2), symbol1), number4, symbol3)
    # number + (number symbol number) * number)
    if not _higher(symbol1) and _higher(symbol3):
        return 24.0 == _caculate(number1, _caculate(_caculate(number2, number3, symbol2), number4, symbol3), symbol1)
    # number + (number symbol number) + number)
    if not _higher(symbol1) and not _higher(symbol3):
        return 24.0 == _caculate(_caculate(number1, _caculate(number2, number3, symbol2), symbol1), number4, symbol3)
    pass


# (number symbol number symbol number) symbol number
def _check6(number1, number2, number3, number4, symbol1, symbol2, symbol3):
    # (number * number * number) symbol number
    if _higher(symbol1) and _higher(symbol2):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2), number4, symbol3)
    # (number * number + number) symbol number
    if _higher(symbol1) and not _higher(symbol2):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2), number4, symbol3)
    # (number + number * number) symbol number
    if not _higher(symbol1) and _higher(symbol2):
        return 24.0 == _caculate(_caculate(number1, _caculate(number2, number3, symbol2), symbol1), number4, symbol3)
    # (number + number + number) symbol number
    if not _higher(symbol1) and not _higher(symbol2):
        return 24.0 == _caculate(_caculate(_caculate(number1, number2, symbol1), number3, symbol2), number4, symbol3)


# number symbol (number symbol number symbol number)
def _check7(number1, number2, number3, number4, symbol1, symbol2, symbol3):
    # number symbol (number * number * number)
    if _higher(symbol2) and _higher(symbol3):
        return 24.0 == _caculate(number1, _caculate(_caculate(number2, number3, symbol2), number4, symbol3), symbol1)
    # number symbol (number * number + number)
    if _higher(symbol2) and not _higher(symbol3):
        return 24.0 == _caculate(number1, _caculate(_caculate(number2, number3, symbol2), number4, symbol3), symbol1)
    # number symbol (number + number * number)
    if not _higher(symbol2) and _higher(symbol3):
        return 24.0 == _caculate(number1, _caculate(number2, _caculate(number3, number4, symbol3), symbol2), symbol1)
    # number symbol (number + number + number)
    if not _higher(symbol2) and not _higher(symbol3):
        return 24.0 == _caculate(number1, _caculate(_caculate(number2, number3, symbol2), number4, symbol3), symbol1)


# Check按钮的处理函数，计算是否24，如果有空的格子，直接返回错误，如果计算正确，总分加10分
def check(number1, number2, number3, number4,
          symbol1, symbol2, symbol3,
          bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
    if not _validate_inputs(number1, number2, number3, number4,
                            symbol1, symbol2, symbol3,
                            bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
        return False
    return check_only(number1, number2, number3, number4,
                      symbol1, symbol2, symbol3,
                      bracket1, bracket2, bracket3, bracket4, bracket5, bracket6)


def check_only(number1, number2, number3, number4,
               symbol1, symbol2, symbol3,
               bracket1, bracket2, bracket3, bracket4, bracket5, bracket6):
    brackets = (bracket1, bracket2, bracket3, bracket4, bracket5, bracket6)
    if brackets == valid_brackets[0] or brackets == valid_brackets[1]:
        return _check1(number1, number2, number3, number4, symbol1, symbol2, symbol3)
    elif brackets == valid_brackets[2]:
        return _check2(number1, number2, number3, number4, symbol1, symbol2, symbol3)
    elif brackets == valid_brackets[3]:
        return _check3(number1, number2, number3, number4, symbol1, symbol2, symbol3)
    elif brackets == valid_brackets[4]:
        return _check4(number1, number2, number3, number4, symbol1, symbol2, symbol3)
    elif brackets == valid_brackets[5]:
        return _check5(number1, number2, number3, number4, symbol1, symbol2, symbol3)
    elif brackets == valid_brackets[6]:
        return _check6(number1, number2, number3, number4, symbol1, symbol2, symbol3)
    elif brackets == valid_brackets[7]:
        return _check7(number1, number2, number3, number4, symbol1, symbol2, symbol3)

    print("Assert Error!")


def test_check():
    # number symbol number symbol number symbol number
    print(check(1, 2, 3, 4, "mul", "mul", "mul", None, None, None, None, None, None))
    print(check(3, 3, 2, 6, "mul", "mul", "plus", None, None, None, None, None, None))
    print(check(3, 4, 3, 4, "mul", "plus", "mul", None, None, None, None, None, None))
    print(check(3, 4, 6, 6, "mul", "plus", "plus", None, None, None, None, None, None))
    print(check(6, 2, 3, 3, "plus", "mul", "mul", None, None, None, None, None, None))
    print(check(6, 3, 4, 6, "plus", "mul", "plus", None, None, None, None, None, None))
    print(check(6, 6, 3, 4, "plus", "plus", "mul", None, None, None, None, None, None))
    print(check(6, 6, 6, 6, "plus", "plus", "plus", None, None, None, None, None, None))

    # (number symbol number symbol number symbol number)
    print(check(1, 2, 3, 4, "mul", "mul", "mul", '(', None, None, None, None, ')'))
    print(check(3, 3, 2, 6, "mul", "mul", "plus", '(', None, None, None, None, ')'))
    print(check(3, 4, 3, 4, "mul", "plus", "mul", '(', None, None, None, None, ')'))
    print(check(3, 4, 6, 6, "mul", "plus", "plus", '(', None, None, None, None, ')'))
    print(check(6, 2, 3, 3, "plus", "mul", "mul", '(', None, None, None, None, ')'))
    print(check(6, 3, 4, 6, "plus", "mul", "plus", '(', None, None, None, None, ')'))
    print(check(6, 6, 3, 4, "plus", "plus", "mul", '(', None, None, None, None, ')'))
    print(check(6, 6, 6, 6, "plus", "plus", "plus", '(', None, None, None, None, ')'))

    # (number symbol number) symbol number symbol number
    print(check(1, 2, 2, 4, "plus", "mul", "mul", '(', None, ')', None, None, None))
    print(check(1, 2, 6, 6, "plus", "mul", "plus", '(', None, ')', None, None, None))
    print(check(2, 4, 3, 6, "plus", "plus", "mul", '(', None, ')', None, None, None))
    print(check(2, 8, 6, 8, "plus", "plus", "plus", '(', None, ')', None, None, None))

    # number symbol number symbol (number symbol number)
    print(check(2, 4, 1, 2, "mul", "mul", "plus", None, None, None, '(', None, ')'))
    print(check(3, 6, 2, 4, "mul", "plus", "plus", None, None, None, '(', None, ')'))
    print(check(6, 6, 1, 2, "plus", "mul", "plus", None, None, None, '(', None, ')'))
    print(check(7, 9, 3, 5, "plus", "plus", "plus", None, None, None, '(', None, ')'))

    # (number symbol number) symbol (number symbol number)
    print(check(4, 4, 1, 2, "plus", "mul", "plus", '(', None, ')', '(', None, ')'))
    print(check(4, 8, 6, 6, "plus", "plus", "plus", '(', None, ')', '(', None, ')'))

    # number symbol (number symbol number) symbol number
    print(check(2, 1, 2, 4, "mul", "plus", "mul", None, '(', None, None, ')', None))
    print(check(6, 1, 2, 6, "mul", "plus", "plus", None, '(', None, None, ')', None))
    print(check(3, 1, 2, 7, "plus", "plus", "mul", None, '(', None, None, ')', None))
    print(check(7, 2, 6, 9, "plus", "plus", "plus", None, '(', None, None, ')', None))

    # (number symbol number symbol number) symbol number
    print(check(2, 3, 3, 6, "mul", "mul", "plus", '(', None, None, None, ')', None))
    print(check(3, 4, 4, 8, "mul", "plus", "plus", '(', None, None, None, ')', None))
    print(check(4, 3, 4, 8, "plus", "mul", "plus", '(', None, None, None, ')', None))
    print(check(6, 4, 6, 8, "plus", "plus", "plus", '(', None, None, None, ')', None))

    # number symbol (number symbol number symbol number)
    print(check(6, 2, 3, 3, "plus", "mul", "mul", None, '(', None, None, None, ')'))
    print(check(4, 3, 4, 8, "plus", "mul", "plus", None, '(', None, None, None, ')'))
    print(check(8, 4, 3, 4, "plus", "plus", "mul", None, '(', None, None, None, ')'))
    print(check(8, 6, 4, 6, "plus", "plus", "plus", None, '(', None, None, None, ')'))
