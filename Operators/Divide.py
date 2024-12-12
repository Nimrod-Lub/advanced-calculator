from Operators.BinaryOperator import BinaryOperator

DIVIDE_PRECEDENCE = 2


class Divide(BinaryOperator):

    def __init__(self):
        super().__init__(DIVIDE_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
