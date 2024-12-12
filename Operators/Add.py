from Operators.BinaryOperator import BinaryOperator

ADD_PRECEDENCE = 1


class Add(BinaryOperator):

    def __init__(self):
        super().__init__(ADD_PRECEDENCE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
