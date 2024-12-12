from Operators.UnaryOperator import UnaryOperator, RIGHT_SIDE

DIGIT_SUM_PRECEDENCE = 6

class DigitSum(UnaryOperator):

    def __init__(self):
        super().__init__(DIGIT_SUM_PRECEDENCE, RIGHT_SIDE)

    def calculate(self, *args):
        pass

    def validate(self, *args):
        ...
