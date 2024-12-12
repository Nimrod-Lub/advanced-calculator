from Operators.BinaryOperator import BinaryOperator

MAXIMUM_PRECEDENCE = 5


class Maximum(BinaryOperator):

    def __init__(self):
        super().__init__(MAXIMUM_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
