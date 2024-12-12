from Operators.BinaryOperator import BinaryOperator

SUBTRACT_PRECEDENCE = 1


class Subtract(BinaryOperator):

    def __init__(self):
        super().__init__(SUBTRACT_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
