from Operators.BinaryOperator import BinaryOperator

AVERAGE_PRECEDENCE = 5


class Average(BinaryOperator):

    def __init__(self):
        super().__init__(AVERAGE_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
