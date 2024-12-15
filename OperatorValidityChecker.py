from Operators.BinaryOperator import BinaryOperator
from Operators.UnaryOperator import LEFT_SIDE, RIGHT_SIDE, UnaryOperator
from Util import is_number, is_open_paren, is_operator, get_operator, is_close_paren, is_binary_operator, \
    is_unary_operator

#TODO go over this again and check if the logic is sound
#TODO convert isinstance commands to util module commands

def check_operators_validity(tokens: list):
    for index in range(len(tokens)):
        if is_operator(tokens[index]):
            validate_operator(tokens, index)


def validate_operator(tokens: list, position: int):
    if isinstance(get_operator(tokens[position]), UnaryOperator):
        validate_unary_operator(tokens, position)
    elif isinstance(get_operator(tokens[position]), BinaryOperator):
        validate_binary_operator(tokens, position)


def validate_binary_operator(tokens: list, position: int):
    if position == 0 or position == len(tokens) - 1:
        exit()  # Do nothing for binary operator at the edges of the expression

    before = tokens[position - 1]

    if not is_number(before) and not is_close_paren(before) and not is_operator(before):
        exit()  # Error - this character cannot be placed before a binary operator

    if is_operator(before):
        if (isinstance(get_operator(before), BinaryOperator)
                or (isinstance(get_operator(before), UnaryOperator) and not get_operator(
                    before).get_side() == RIGHT_SIDE)):
            exit()  # Error - this operator cannot be placed before a binary operator

    after = tokens[position + 1]

    if not is_number(after) and not is_open_paren(after) and not is_operator(after):
        exit()  # Error - this character cannot be placed after a binary operator

    if is_operator(after):
        if (isinstance(get_operator(after), BinaryOperator)
                or (isinstance(get_operator(after), UnaryOperator) and not get_operator(
                    after).get_side() == LEFT_SIDE)):
            exit()  # Error - this operator cannot be placed after a binary operator


def validate_unary_operator(tokens: list, position: int):
    if get_operator(tokens[position]).get_side() == LEFT_SIDE:
        validate_left_unary_operator(tokens, position)
    elif get_operator(tokens[position]).get_side() == RIGHT_SIDE:
        validate_right_unary_operator(tokens, position)


def validate_left_unary_operator(tokens: list, position: int):
    if position == len(tokens) - 1:
        exit()  # Handle error - left unary operator cannot be at the end of the expression

    after = tokens[position + 1]

    if not is_number(after) and not is_open_paren(after) and not is_operator(after):
        exit()  # Handle error - this character cannot be placed after a left unary operator

    if is_operator(after):
        if (isinstance(get_operator(after), BinaryOperator)
                or (isinstance(get_operator(after), UnaryOperator) and not get_operator(after).get_side() == LEFT_SIDE)):
            exit()  # Handle error - this operator cannot be placed after a left unary operator

    if position == 0:  # Don't need to check before the operator if it's at the beginning of the expression
        return

    before = tokens[position - 1]

    if not is_open_paren(before) and not is_operator(before):
        exit()  # Handle error - this character cannot be placed before a left unary operator

    if is_operator(before):
        if not is_binary_operator(before) and is_unary_operator(before) and not get_operator(before).get_side() == LEFT_SIDE:
            exit()  # Handle error - this operator cannot be placed before a left unary operator

def validate_right_unary_operator(tokens: list, position: int):
    if position == 0:
        exit()  # Handle error - right unary operator cannot be at the beginning of the expression

    before = tokens[position - 1]

    if not is_number(before) and not is_close_paren(before) and not is_operator(before):
        exit()  # Handle error - this character cannot be placed before a right unary operator

    if is_operator(before):
        if (isinstance(get_operator(before), BinaryOperator)
                or (isinstance(get_operator(before), UnaryOperator) and not get_operator(before).get_side() == RIGHT_SIDE)):
            exit()  # Handle error - this character cannot be placed before a right unary operator

    if position == len(tokens) - 1:  # Don't need to check after the operator if it's at the end of the expression
        return

    after = tokens[position + 1]

    if not is_close_paren(after) and not is_operator(after):
        exit()  # Handle error - this character cannot be placed after a right unary operator

    if is_operator(after):
        if not is_binary_operator(after) and is_unary_operator(after) and not get_operator(after).get_side() == RIGHT_SIDE:
            exit()  # Handle error - this operator cannot be placed after a right unary operator


def main():
    check_operators_validity(["5", "!", "!", "~", "1", ])


if __name__ == "__main__":
    main()
