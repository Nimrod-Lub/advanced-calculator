from Operators.BinaryOperator import BinaryOperator

MODULO_PRECEDENCE = 4
MODULO_SIGN = '%'

class Modulo(BinaryOperator):

    def __init__(self):
        super().__init__(MODULO_PRECEDENCE)

    def calculate(self, *args): #TODO fix this
        return  args[0] % args[1]

    def validate_calculation(self, *args):
        ...


def main():
    m = Modulo()
    print(m.calculate(-1.5, 2))

if __name__ == "__main__":
    main()
