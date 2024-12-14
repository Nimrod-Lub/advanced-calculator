from Operators.BinaryOperator import BinaryOperator

DIVIDE_PRECEDENCE = 2


class Divide(BinaryOperator):

    def __init__(self):
        super().__init__(DIVIDE_PRECEDENCE)

    def calculate(self, *args):
        return float(args[0]) / float(args[1])

    def validate(self, *args):
        ...


def main():
    d = Divide()
    print(d.calculate("20", "10"))

if __name__ == "__main__":
    main()
