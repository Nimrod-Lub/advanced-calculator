from MyExceptions.ParseException import FormattingException
from Operators.Operator import LARGEST_PRECEDENCE
from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE
from Util import is_number, is_open_paren

SIGN_MINUS_PRECEDENCE = LARGEST_PRECEDENCE
SIGN_MINUS_SIGN = 'sign_minus'

class SignMinus(UnaryOperator):

    def __init__(self):
        super().__init__(SIGN_MINUS_PRECEDENCE, LEFT_SIDE)


    def calculate(self, num: float):
        return -num

    def validate_calculation(self, num: float):
        pass

    def validate_individual_operator(self, tokens: list, position: int):
        index = position + 1

        while index < len(tokens) - 1 and not is_number(tokens[index]) and not is_open_paren(tokens[index]):
            if tokens[index] != SIGN_MINUS_SIGN:
                raise FormattingException(f"{tokens[index]} cannot be placed after a sign minus"
                                          , ''.join(tokens))
            index += 1
