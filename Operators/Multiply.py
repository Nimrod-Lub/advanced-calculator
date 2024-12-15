from Operators.BinaryOperator import BinaryOperator

MULTIPLY_PRECEDENCE = 2


class Multiply(BinaryOperator):

    def __init__(self):
        super().__init__(MULTIPLY_PRECEDENCE)

    def calculate(self, *args):
        return args[0] * args[1]

    def validate_calculation(self, *args):
        ...


def main():
    m = Multiply()
    print(m.calculate(-1.5, 2))

if __name__ == "__main__":
    main()