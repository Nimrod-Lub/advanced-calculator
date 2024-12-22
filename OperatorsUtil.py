from Operators.Add import ADD_SIGN, Add
from Operators.Average import AVERAGE_SIGN, Average
from Operators.BinaryOperator import BinaryOperator
from Operators.DigitSum import DIGIT_SUM_SIGN, DigitSum
from Operators.Divide import DIVIDE_SIGN, Divide
from Operators.Factorial import FACTORIAL_SIGN, Factorial
from Operators.Maximum import MAXIMUM_SIGN, Maximum
from Operators.Minimum import MINIMUM_SIGN, Minimum
from Operators.Modulo import MODULO_SIGN, Modulo
from Operators.Multiply import MULTIPLY_SIGN, Multiply
from Operators.Negative import NEGATIVE_SIGN, Negative
from Operators.Operator import Operator
from Operators.Power import POWER_SIGN, Power
from Operators.SignMinus import SIGN_MINUS_SIGN, SignMinus
from Operators.Subtract import SUBTRACT_SIGN, Subtract
from Operators.UnaryMinus import UNARY_MINUS_SIGN, UnaryMinus
from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE, RIGHT_SIDE

OPERATORS = {ADD_SIGN: Add(), SUBTRACT_SIGN: Subtract(), MULTIPLY_SIGN: Multiply(), DIVIDE_SIGN: Divide()
    , UNARY_MINUS_SIGN: UnaryMinus(), POWER_SIGN: Power(), MODULO_SIGN: Modulo()
    , MAXIMUM_SIGN: Maximum(), MINIMUM_SIGN: Minimum(), AVERAGE_SIGN: Average(), NEGATIVE_SIGN: Negative()
    , FACTORIAL_SIGN: Factorial(), DIGIT_SUM_SIGN: DigitSum(), SIGN_MINUS_SIGN: SignMinus()}


def is_operator(string: str) -> bool:
    """
    Checks if a string represents an operator, and returns true if it is, else returns false

    :param string: a token from the list of tokens
    :return: true if string represents an operator, else false
    """
    return string in OPERATORS.keys()


def is_binary_operator(string: str) -> bool:
    """
    Checks if a string represents a binary operator, and returns true if it is, else returns false

    :param string: a token from the list of tokens
    :return: true if string represents a binary operator, else false
    """

    return is_operator(string) and isinstance(get_operator(string), BinaryOperator)


def is_unary_operator(string: str) -> bool:
    """
    Checks if a string represents a unary operator, and returns true if it is, else returns false

    :param string: a token from the list of tokens
    :return: true if string represents a unary operator, else false
    """

    return is_operator(string) and isinstance(get_operator(string), UnaryOperator)


def is_left_unary_operator(string: str) -> bool:
    """
    Checks if a string represents a left unary operator, and returns true if it is, else returns false

    :param string: a token from the list of tokens
    :return: true if string represents a left unary operator, else false
    """

    return is_unary_operator(string) and get_operator(string).get_side() == LEFT_SIDE


def is_right_unary_operator(string: str) -> bool:
    """
    Checks if a string represents a right unary operator, and returns true if it is, else returns false

    :param string: a token from the list of tokens
    :return: true if string represents a right unary operator, else false
    """

    return is_unary_operator(string) and get_operator(string).get_side() == RIGHT_SIDE


def get_operator(string: str) -> Operator:
    """
    Returns an operator object whose sign is the string given by the user

    :param string: a token from the list of tokens representing an operator
    :return: the operator object the token represents
    """

    return OPERATORS[string]
