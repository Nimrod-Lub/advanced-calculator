from Operators.BinaryOperator import BinaryOperator

ADD_PRECEDENCE = 1


class Add(BinaryOperator):

    def __init__(self):
        super().__init__(ADD_PRECEDENCE)

    def calculate(self, *args):
        return float(args[0]) + float(args[1])

    def validate(self, *args):
        ...


def main():
    a = Add()
    print(a.calculate("123", "-203"))

if __name__ == "__main__":
    main()