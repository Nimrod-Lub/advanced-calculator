from Operators.UnaryOperator import UnaryOperator, RIGHT_SIDE

FACTORIAL_PRECEDENCE = 6


class Factorial(UnaryOperator):

    def __init__(self):
        super().__init__(FACTORIAL_PRECEDENCE, RIGHT_SIDE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
