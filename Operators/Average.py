from Operators.BinaryOperator import BinaryOperator

AVERAGE_PRECEDENCE = 5


class Average(BinaryOperator):

    def __init__(self):
        super().__init__(AVERAGE_PRECEDENCE)

    def calculate(self, *args):
        return (float(args[0]) + float(args[1])) / 2

    def validate_calculation(self, *args):
        ...



def main():
    a = Average()
    print(a.calculate("123", "-203"))

if __name__ == "__main__":
    main()