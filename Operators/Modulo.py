from MyExceptions.ParseException import MathematicalException
from Operators.BinaryOperator import BinaryOperator

MODULO_PRECEDENCE = 4
MODULO_SIGN = '%'

class Modulo(BinaryOperator):

    def __init__(self):
        super().__init__(MODULO_PRECEDENCE)

    def calculate(self, num1: float, num2: float):
        self.validate_calculation(num1, num2)
        return  num1 % num2

    def validate_calculation(self, num1: float, num2: float):
        if num2 == 0:
            raise MathematicalException("Modulo by 0 is undefined", f"{num1}{MODULO_SIGN}{num2}")


def main():
    m = Modulo()
    print(m.calculate(-1.5, 2))

if __name__ == "__main__":
    main()
