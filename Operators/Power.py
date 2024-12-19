import math

from Operators.BinaryOperator import BinaryOperator

POWER_PRECEDENCE = 3
POWER_SIGN = '^'

class Power(BinaryOperator):

    def __init__(self):
        super().__init__(POWER_PRECEDENCE)

    def calculate(self, *args):
        return math.pow(args[0], args[1])

    def validate_calculation(self, *args):
        ...


def main():
    p = Power()
    print(p.calculate(10, 308))

if __name__ == "__main__":
    main()