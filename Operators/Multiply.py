from Operators.BinaryOperator import BinaryOperator

MULTIPLY_PRECEDENCE = 2
MULTIPLY_SIGN = '*'

class Multiply(BinaryOperator):

    def __init__(self):
        super().__init__(MULTIPLY_PRECEDENCE)

    def calculate(self, num1: float, num2: float):
        return num1 * num2

    def validate_calculation(self, num1: float, num2: float):
        ...


def main():
    m = Multiply()
    print(m.calculate(-1.5, 2))

if __name__ == "__main__":
    main()