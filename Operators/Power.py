import math

from MyExceptions.ParseException import MathematicalException
from Operators.BinaryOperator import BinaryOperator

POWER_PRECEDENCE = 3
POWER_SIGN = '^'

class Power(BinaryOperator):

    def __init__(self):
        super().__init__(POWER_PRECEDENCE)

    def calculate(self, num1: float, num2: float):
        self.validate_calculation(num1, num2)
        return math.pow(num1, num2)

    def validate_calculation(self, num1: float, num2: float):
        if num1 < 0 and -1 < num2 < 1:
            raise MathematicalException("Root of negative number is undefined", f"{num1}{POWER_SIGN}{num2}")
        if num1 == 0 and num2 == 0:
            raise MathematicalException("0 to the power of 0 is undefined", f"{num1}{POWER_SIGN}{num2}")


def main():
    p = Power()
    print(p.calculate(10, 308))

if __name__ == "__main__":
    main()