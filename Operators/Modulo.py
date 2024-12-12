from Operators.BinaryOperator import BinaryOperator

MODULO_PRECEDENCE = 4


class Modulo(BinaryOperator):

    def __init__(self):
        super().__init__(MODULO_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
