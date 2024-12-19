from Operators.Operator import LARGEST_PRECEDENCE
from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE

SIGN_MINUS_PRECEDENCE = LARGEST_PRECEDENCE
SIGN_MINUS_SIGN = 'sign_minus'

class SignMinus(UnaryOperator):

    def __init__(self):
        super().__init__(SIGN_MINUS_PRECEDENCE, LEFT_SIDE)


    def calculate(self, *args):
        return -args[0]

    def validate_calculation(self, *args):
        pass