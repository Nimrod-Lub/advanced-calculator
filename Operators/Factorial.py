from MyExceptions.ParseException import MathematicalException
from Operators.UnaryOperator import UnaryOperator, RIGHT_SIDE

FACTORIAL_PRECEDENCE = 6
FACTORIAL_SIGN = '!'


class Factorial(UnaryOperator):

    def __init__(self):
        super().__init__(FACTORIAL_PRECEDENCE, RIGHT_SIDE)

    def calculate(self, num: float):
        self.validate_calculation(num)
        return factorial(num)

    def validate_calculation(self, num: float):
        if not num.is_integer():
            raise MathematicalException("Factorial of a non integer number is undefined",
                                        f"{num}{FACTORIAL_SIGN}")
        if num < 0:
            raise MathematicalException("Factorial of a negative number is undefined",
                                        f"{num}{FACTORIAL_SIGN}")


def factorial(num: float):
    result = 1
    for number in range(1, int(num) + 1):
        result *= number
    return result


def main():
    f = Factorial()
    print(f.calculate(6.0))


if __name__ == "__main__":
    main()
