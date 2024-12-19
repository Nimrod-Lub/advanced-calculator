from Operators.BinaryOperator import BinaryOperator

MINIMUM_PRECEDENCE = 5
MINIMUM_SIGN = '&'

class Minimum(BinaryOperator):

    def __init__(self):
        super().__init__(MINIMUM_PRECEDENCE)

    def calculate(self, *args):
        return min(args[0], args[1])

    def validate_calculation(self, *args):
        ...



def main():
    m = Minimum()
    print(m.calculate(10.35, 10.5))

if __name__ == "__main__":
    main()
