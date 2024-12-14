from Operators.UnaryOperator import UnaryOperator, RIGHT_SIDE

DIGIT_SUM_PRECEDENCE = 6

class DigitSum(UnaryOperator):

    def __init__(self):
        super().__init__(DIGIT_SUM_PRECEDENCE, RIGHT_SIDE)

    def calculate(self, *args):
        number_str = args[0]
        number_str = number_str.replace('.','')

        sign = 1
        if '-' in args[0]:
            sign = -1
            number_str = number_str.replace('-','')

        digit_sum = 0
        for digit in number_str:
            digit_sum += float(digit)

        return digit_sum * sign


    def validate(self, *args):
        ...

def main():
    dg = DigitSum()
    print(dg.calculate("-23.123"))

if __name__ == "__main__":
    main()
