from Operators.BinaryOperator import BinaryOperator

POWER_PRECEDENCE = 3


class Power(BinaryOperator):

    def __init__(self):
        super().__init__(POWER_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
