from MyExceptions.InvalidDots import NonDecimalDot, NoDigitsAfterDecimalPoint, TwoDecimalPointsOneNumber
from MyExceptions.InvalidParenthesis import ClosingUnopenedParenthesis, OpenParenthesis
from Util import remove_white_spaces, is_paren, is_operator, is_other_character


def check_validity(user_input: str):
    user_input = remove_white_spaces(user_input)
    check_valid_letters(user_input)
    check_dots(user_input)
    check_parenthesis(user_input)

# Should support adding more parenthesis types?
def check_parenthesis(string: str):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                raise ClosingUnopenedParenthesis()

    if len(stack) > 0:
        raise OpenParenthesis()


def check_valid_letters(string: str):
    for char in string:
        if not char.isdigit() and not is_operator(char) and not is_paren(char) and not is_other_character(char):
            raise ValueError("Symbol " + char + " is undefined")


def check_dots(string: str):
    curr_is_number = False
    curr_number_has_decimal = False

    for index in range(len(string)):
        if string[index] == '.':
            if index == 0 or index == len(string) - 1:  # Dot at the end or beginning
                raise NonDecimalDot()

            else:
                if curr_is_number and not curr_number_has_decimal:  # Correct usage
                    curr_number_has_decimal = True
                    curr_is_number = False

                elif not curr_is_number and curr_number_has_decimal:  # Multiple dots in a row
                    raise NonDecimalDot()

                elif not curr_is_number and not curr_number_has_decimal:  # Random usage of dot
                    raise NonDecimalDot()

                else:  # Dot used twice on one string of digits
                    raise TwoDecimalPointsOneNumber()

        elif string[index].isdigit():
            curr_is_number = True

        else:
            if not curr_is_number and curr_number_has_decimal: # No digits after a decimal point
                raise NoDigitsAfterDecimalPoint()

            curr_is_number = False
            curr_number_has_decimal = False

