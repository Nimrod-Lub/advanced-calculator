from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE

NEGATIVE_PRECEDENCE = 6
NEGATIVE_SIGN = '~'

class Negative(UnaryOperator):

    def __init__(self):
        super().__init__(NEGATIVE_PRECEDENCE, LEFT_SIDE)

    def calculate(self, *args):
        return -args[0]

    def validate_calculation(self, *args):
        ...


def main():
    n = Negative()
    print(n.calculate(5))

if __name__ == "__main__":
    main()