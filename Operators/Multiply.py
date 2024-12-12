from Operators.BinaryOperator import BinaryOperator

MULTIPLY_PRECEDENCE = 2


class Multiply(BinaryOperator):

    def __init__(self):
        super().__init__(MULTIPLY_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
