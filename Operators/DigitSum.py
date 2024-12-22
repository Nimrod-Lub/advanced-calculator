from MyExceptions.ParseException import MathematicalException
from Operators.UnaryOperator import UnaryOperator, RIGHT_SIDE

DIGIT_SUM_PRECEDENCE = 6
DIGIT_SUM_SIGN = '#'

class DigitSum(UnaryOperator):

    def __init__(self):
        super().__init__(DIGIT_SUM_PRECEDENCE, RIGHT_SIDE)

    def calculate(self, num: float):
        self.validate_calculation(num)

        number_str = num
        number_str = str(number_str).replace('.','')

        digit_sum = 0
        for digit in number_str[:]:
            digit_sum += float(digit)

        return digit_sum


    def validate_calculation(self, num: float):
        if num < 0:
            raise MathematicalException(f"{DIGIT_SUM_SIGN} operator is undefined for negative numbers",
                                        f"{num}{DIGIT_SUM_SIGN}")

def main():
    dg = DigitSum()
    print(dg.calculate(-23.123))

if __name__ == "__main__":
    main()
