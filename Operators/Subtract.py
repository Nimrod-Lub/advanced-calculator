from Operators.BinaryOperator import BinaryOperator

SUBTRACT_PRECEDENCE = 1
SUBTRACT_SIGN = '-'

class Subtract(BinaryOperator):

    def __init__(self):
        super().__init__(SUBTRACT_PRECEDENCE)

    def calculate(self, num1: float, num2: float):
        return num1 - num2

    def validate_calculation(self, num1: float, num2: float):
        ...


def main():
    s = Subtract()
    print(s.calculate(3, 2))

if __name__ == "__main__":
    main()