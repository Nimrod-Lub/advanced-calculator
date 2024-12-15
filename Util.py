from Operators.Add import Add
from Operators.Average import Average
from Operators.BinaryOperator import BinaryOperator
from Operators.DigitSum import DigitSum
from Operators.Divide import Divide
from Operators.Factorial import Factorial
from Operators.Maximum import Maximum
from Operators.Minimum import Minimum
from Operators.Modulo import Modulo
from Operators.Multiply import Multiply
from Operators.Negative import Negative
from Operators.Operator import Operator
from Operators.Power import Power
from Operators.Subtract import Subtract
from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE, RIGHT_SIDE

OPERATORS = {'+': Add(), '-': Subtract(), '*': Multiply(), '/': Divide(), '^': Power(), '%': Modulo(), '$': Maximum()
    , '&': Minimum(), '@': Average(), '~': Negative(), '!': Factorial(), '#': DigitSum()}

OTHER_CHARACTERS = ('.')

#TODO add is_unary_operator and is_binary_operator

def is_number(string: str) -> bool:
    for char in string:
        if not (char.isdigit() or char == '.'):
            return False
    return True

def is_paren(string: str) -> bool:
    return is_open_paren(string) or is_close_paren(string)


def is_open_paren(string: str) -> bool:
    return string == '('


def is_close_paren(string: str) -> bool:
    return string == ')'


def is_operator(string: str) -> bool:
    return string in OPERATORS.keys()


def is_binary_operator(string: str) -> bool:
    return is_operator(string) and isinstance(get_operator(string), BinaryOperator)

def is_unary_operator(string: str) -> bool:
    return is_operator(string) and isinstance(get_operator(string), UnaryOperator)

def is_left_unary_operator(string: str) -> bool:
    return is_unary_operator(string) and get_operator(string).get_side() == LEFT_SIDE

def is_right_unary_operator(string: str) -> bool:
    return is_unary_operator(string) and get_operator(string).get_side() == RIGHT_SIDE

def get_operator(string: str) -> Operator:
    return OPERATORS[string]


def is_other_character(string: str) -> bool:
    return string in OTHER_CHARACTERS


def remove_white_spaces(string: str) -> str:
    """
    Removes white spaces from user input

    :param string: user input
    :return: user input without white spaces
    """
    return "".join(string.split())