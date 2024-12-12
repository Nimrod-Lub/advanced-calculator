from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE

NEGATIVE_PRECEDENCE = 6


class Negative(UnaryOperator):

    def __init__(self):
        super().__init__(NEGATIVE_PRECEDENCE, LEFT_SIDE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
