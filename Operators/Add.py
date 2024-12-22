from Operators.BinaryOperator import BinaryOperator

ADD_PRECEDENCE = 1
ADD_SIGN = '+'

class Add(BinaryOperator):

    def __init__(self):
        super().__init__(ADD_PRECEDENCE)

    def calculate(self, num1: float, num2: float):
        return num1 + num2

    def validate_calculation(self, num1: float, num2: float):
        ...


def main():
    a = Add()
    print(a.calculate("123", "-203"))

if __name__ == "__main__":
    main()