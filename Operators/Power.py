import math

from Operators.BinaryOperator import BinaryOperator

POWER_PRECEDENCE = 3


class Power(BinaryOperator):

    def __init__(self):
        super().__init__(POWER_PRECEDENCE)

    def calculate(self, *args):
        return math.pow(args[0], args[1])

    def validate(self, *args):
        ...


def main():
    p = Power()
    print(p.calculate(2, 10))

if __name__ == "__main__":
    main()