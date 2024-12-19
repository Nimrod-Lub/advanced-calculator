from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE

UNARY_MINUS_PRECEDENCE = 2.5
UNARY_MINUS_SIGN = 'unary_minus'

class UnaryMinus(UnaryOperator):

    def __init__(self):
        super().__init__(UNARY_MINUS_PRECEDENCE, LEFT_SIDE)


    def calculate(self, *args):
        return -args[0]

    def validate_calculation(self, *args):
        pass