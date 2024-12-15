from Operators.UnaryOperator import UnaryOperator, RIGHT_SIDE

FACTORIAL_PRECEDENCE = 6


class Factorial(UnaryOperator):

    def __init__(self):
        super().__init__(FACTORIAL_PRECEDENCE, RIGHT_SIDE)

    def calculate(self, *args):
        if args[0].is_integer():
            return factorial(int(args[0]))
        return -1 # TODO handle

    def validate_calculation(self, *args):
        ...

def factorial(num):
    result = 1
    for number in range(1, num + 1):
        result *= number
    return result

def main():
    f = Factorial()
    print(f.calculate(6.0))

if __name__ == "__main__":
    main()
