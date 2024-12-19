from Operators.Add import Add, ADD_SIGN
from Operators.Average import Average, AVERAGE_SIGN
from Operators.BinaryOperator import BinaryOperator
from Operators.DigitSum import DigitSum, DIGIT_SUM_SIGN
from Operators.Divide import Divide, DIVIDE_SIGN
from Operators.Factorial import Factorial, FACTORIAL_SIGN
from Operators.Maximum import Maximum, MAXIMUM_SIGN
from Operators.Minimum import Minimum, MINIMUM_SIGN
from Operators.Modulo import Modulo, MODULO_SIGN
from Operators.Multiply import Multiply, MULTIPLY_SIGN
from Operators.Negative import Negative, NEGATIVE_SIGN
from Operators.Operator import Operator
from Operators.Power import Power, POWER_SIGN
from Operators.SignMinus import SignMinus, SIGN_MINUS_SIGN
from Operators.Subtract import Subtract, SUBTRACT_SIGN
from Operators.UnaryMinus import UnaryMinus, UNARY_MINUS_SIGN
from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE, RIGHT_SIDE

OPERATORS = {ADD_SIGN: Add(), SUBTRACT_SIGN: Subtract(), MULTIPLY_SIGN: Multiply(), DIVIDE_SIGN: Divide()
    , UNARY_MINUS_SIGN: UnaryMinus(), POWER_SIGN: Power(), MODULO_SIGN: Modulo()
    , MAXIMUM_SIGN: Maximum(), MINIMUM_SIGN: Minimum(), AVERAGE_SIGN: Average(), NEGATIVE_SIGN: Negative()
    , FACTORIAL_SIGN: Factorial(), DIGIT_SUM_SIGN: DigitSum(), SIGN_MINUS_SIGN: SignMinus()}

OTHER_CHARACTERS = ('.')
OPEN_PARENTHESIS = ('(')
CLOSED_PARENTHESIS = (')')
PARENTHESIS = list(OPEN_PARENTHESIS + CLOSED_PARENTHESIS)


def is_number(string: str) -> bool:
    for char in string:
        if not (char.isdigit() or char == '.'):
            return False
    return True


def is_paren(string: str) -> bool:
    return string in PARENTHESIS


def is_open_paren(string: str) -> bool:
    return string in OPEN_PARENTHESIS


def is_close_paren(string: str) -> bool:
    return string in CLOSED_PARENTHESIS


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
