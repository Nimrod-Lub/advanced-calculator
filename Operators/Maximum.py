from Operators.BinaryOperator import BinaryOperator

MAXIMUM_PRECEDENCE = 5
MAXIMUM_SIGN = '$'

class Maximum(BinaryOperator):

    def __init__(self):
        super().__init__(MAXIMUM_PRECEDENCE)

    def calculate(self, *args):
        return max(args[0],args[1])

    def validate_calculation(self, *args):
        ...


def main():
    m = Maximum()
    print(m.calculate(-10.5, 10.35))

if __name__ == "__main__":
    main()
