from Operators.BinaryOperator import BinaryOperator

MINIMUM_PRECEDENCE = 5


class Minimum(BinaryOperator):

    def __init__(self):
        super().__init__(MINIMUM_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
