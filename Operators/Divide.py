from MyExceptions.ParseException import MathematicalException
from Operators.BinaryOperator import BinaryOperator

DIVIDE_PRECEDENCE = 2
DIVIDE_SIGN = '/'

class Divide(BinaryOperator):

    def __init__(self):
        super().__init__(DIVIDE_PRECEDENCE)

    def calculate(self, num1: float, num2: float):
        self.validate_calculation(num1, num2)
        return num1 / num2

    def validate_calculation(self, num1: float, num2: float):
        if num2 == 0:
            raise MathematicalException("Division by 0 is undefined", f"{num1}{DIVIDE_SIGN}{num2}")


def main():
    d = Divide()
    print(d.calculate(20, 10))

if __name__ == "__main__":
    main()
