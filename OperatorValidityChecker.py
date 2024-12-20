from Operators.Negative import NEGATIVE_SIGN
from OperatorsUtil import is_operator, is_binary_operator, \
    is_unary_operator, is_right_unary_operator, is_left_unary_operator, get_operator
from Util import is_number, is_open_paren, is_close_paren


#TODO go over this again and check if the logic is sound - operators!!!!
#TODO go over this again and check if the logic is sound - parenthesis



def check_operators_and_parenthesis_validity(tokens: list):
    for index in range(len(tokens)):
        if is_operator(tokens[index]):
            validate_operator(tokens, index)
        elif is_close_paren(tokens[index]):
            validate_parenthesis(tokens, index)


def validate_parenthesis(tokens: list, position: int):
    if is_open_paren(tokens[position - 1]):
        exit() # Error - empty parenthesis

    if position != len(tokens) - 1:
        if is_open_paren(tokens[position + 1]):
            exit() # Error - No operator between two parenthesis



def validate_operator(tokens: list, position: int):
    if is_unary_operator(tokens[position]):
        validate_unary_operator(tokens, position)
    elif is_binary_operator(tokens[position]):
        validate_binary_operator(tokens, position)

    get_operator(tokens[position]).validate_individual_operator(tokens, position)


def validate_binary_operator(tokens: list, position: int):
    if position == 0 or position == len(tokens) - 1:
        exit()  # Error - binary operator cannot be placed at the edge of the expression

    before = tokens[position - 1]

    if not is_number(before) and not is_close_paren(before) and not is_operator(before):
        exit()  # Error - this character cannot be placed before a binary operator

    if is_operator(before):
        if (is_binary_operator(before)
                or (is_unary_operator(before) and not is_right_unary_operator(before))):
            exit()  # Error - this operator cannot be placed before a binary operator

    after = tokens[position + 1]

    if not is_number(after) and not is_open_paren(after) and not is_operator(after):
        exit()  # Error - this character cannot be placed after a binary operator

    if is_operator(after):
        if (is_binary_operator(after)
                or (is_unary_operator(after) and not is_left_unary_operator(after))):
            exit()  # Error - this operator cannot be placed after a binary operator


def validate_unary_operator(tokens: list, position: int):
    if is_left_unary_operator(tokens[position]):
        validate_left_unary_operator(tokens, position)
    elif is_right_unary_operator(tokens[position]):
        validate_right_unary_operator(tokens, position)


def validate_left_unary_operator(tokens: list, position: int):
    if position == len(tokens) - 1:
        exit()  # Handle error - left unary operator cannot be at the end of the expression

    after = tokens[position + 1]

    if not is_number(after) and not is_open_paren(after) and not is_operator(after):
        exit()  # Handle error - this character cannot be placed after a left unary operator

    if is_operator(after):
        if (is_binary_operator(after)
                or (is_unary_operator(after) and not is_left_unary_operator(after))):
            exit()  # Handle error - this operator cannot be placed after a left unary operator

    if position == 0:  # Don't need to check before the operator if it's at the beginning of the expression
        return

    before = tokens[position - 1]

    if not is_open_paren(before) and not is_operator(before):
        exit()  # Handle error - this character cannot be placed before a left unary operator

    if is_operator(before):
        if (not is_binary_operator(before)
                and is_unary_operator(before) and not is_left_unary_operator(before)):
            exit()  # Handle error - this operator cannot be placed before a left unary operator


def validate_right_unary_operator(tokens: list, position: int):
    if position == 0:
        exit()  # Handle error - right unary operator cannot be at the beginning of the expression

    before = tokens[position - 1]

    if not is_number(before) and not is_close_paren(before) and not is_operator(before):
        exit()  # Handle error - this character cannot be placed before a right unary operator

    if is_operator(before):
        if (is_binary_operator(before)
                or (is_unary_operator(before) and not is_right_unary_operator(before))):
            exit()  # Handle error - this character cannot be placed before a right unary operator

    if position == len(tokens) - 1:  # Don't need to check after the operator if it's at the end of the expression
        return

    after = tokens[position + 1]

    if not is_close_paren(after) and not is_operator(after):
        exit()  # Handle error - this character cannot be placed after a right unary operator

    if is_operator(after):
        if not is_binary_operator(after) and is_unary_operator(after) and not is_right_unary_operator(after):
            exit()  # Handle error - this operator cannot be placed after a right unary operator

def validate_extra_operators(tokens: list, position: int):
    if tokens[position] == NEGATIVE_SIGN:
        validate_operator()

def main():
    check_operators_and_parenthesis_validity(["5", "!", "!", "~", "1", ])


if __name__ == "__main__":
    main()
