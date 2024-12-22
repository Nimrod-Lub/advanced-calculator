from MyExceptions.ParseException import FormattingException
from Operators.SignMinus import SIGN_MINUS_SIGN
from Operators.UnaryOperator import UnaryOperator, LEFT_SIDE
from Util import is_number, is_open_paren

NEGATIVE_PRECEDENCE = 6
NEGATIVE_SIGN = '~'

class Negative(UnaryOperator):

    def __init__(self):
        super().__init__(NEGATIVE_PRECEDENCE, LEFT_SIDE)

    def calculate(self, num: float):
        return -num

    def validate_calculation(self, num: float):
        ...

    def validate_individual_operator(self, tokens: list, position: int):
        index = position + 1

        while index < len(tokens) - 1 and not is_number(tokens[index]) and not is_open_paren(tokens[index]):
            if tokens[index] != SIGN_MINUS_SIGN:
                raise FormattingException(f"{NEGATIVE_SIGN} can only be before a number", ''.join(tokens))
            index += 1



def main():
    n = Negative()
    print(n.calculate(5))

if __name__ == "__main__":
    main()