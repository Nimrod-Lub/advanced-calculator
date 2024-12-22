from Operators.BinaryOperator import BinaryOperator

AVERAGE_PRECEDENCE = 5
AVERAGE_SIGN = '@'

class Average(BinaryOperator):

    def __init__(self):
        super().__init__(AVERAGE_PRECEDENCE)

    def calculate(self, num1: float, num2: float):
        return (num1 + num2) / 2

    def validate_calculation(self, num1: float, num2: float):
        ...



def main():
    a = Average()
    print(a.calculate("123", "-203"))

if __name__ == "__main__":
    main()