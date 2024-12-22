from Operators.SignMinus import SIGN_MINUS_SIGN
from Operators.Subtract import SUBTRACT_SIGN
from Operators.UnaryMinus import UNARY_MINUS_SIGN
from OperatorsUtil import is_binary_operator, is_left_unary_operator
from Util import is_number, remove_white_spaces, is_open_paren

def parse_expression(user_input: str) -> list:
    """
    Tokenizes the expression

    :param user_input: str - user input
    :return: a list of tokens. Each token is either an operator, parenthesis, or a number
    """
    tokens = tokenize_expression(user_input)
    convert_minus(tokens)
    return tokens


def tokenize_expression(user_input: str) -> list:
    """
    Creates a single token for every operator, parenthesis and number,
    stores them in a list in order and returns the list

    :param: user_input: str - user input
    :return: list of tokens
    """
    user_input = remove_white_spaces(user_input)
    token_list = []
    number = ""
    for char in user_input:
        if is_number(char):
            number += char

        else:
            if len(number) > 0:
                token_list.append(number)
                number = ""

            token_list.append(char)

    if len(number) > 0:
        token_list.append(number)

    return token_list


def convert_minus(tokens: list):
    """
    Receives the list of tokens, and replaces binary minus tokens with
    unary minus and sign minus tokens when necessary

    :param tokens: list of tokens
    :return: list of tokens with unary minus and sign minus tokens
    """
    if tokens[0] == SUBTRACT_SIGN:
        tokens[0] = UNARY_MINUS_SIGN

    for index in range(1, len(tokens) - 1):
        if tokens[index] == SUBTRACT_SIGN:
            check_if_special_minus(tokens, index)


def check_if_special_minus(tokens: list, index: int):
    """
    If the current minus is a unary minus or a sign minus, replaces the binary minus
    with the correct minus

    :param tokens: list of tokens
    :param index: the index of the current minus being checked
    """
    if not check_if_unary_minus(tokens, index):
        check_if_sign_minus(tokens, index)


def check_if_unary_minus(tokens: list, index: int) -> bool:
    """
    If the current minus is a unary minus, replaces the binary minus
    with a unary minus

    :param tokens: list of tokens
    :param index: the index of the current minus being checked
    """

    if is_open_paren(tokens[index - 1]) or tokens[index - 1] == UNARY_MINUS_SIGN:
        tokens[index] = UNARY_MINUS_SIGN
        return True

    return False


def check_if_sign_minus(tokens: list, index: int) -> bool:
    """
    If the current minus is a sign minus, replaces the binary minus
    with a sign minus

    :param tokens: list of tokens
    :param index: the index of the current minus being checked
    """
    if is_binary_operator(tokens[index - 1]) or is_left_unary_operator(tokens[index - 1]):
        tokens[index] = SIGN_MINUS_SIGN
        return True
    return False


def main():
    """tokens = tokenize_expression("---1234*(444!)+--123.123")
    print(tokens)
    tokens = parse_expression("---1234*(-44--4!)+--123.123")
    print(tokens)"""

    tokens = tokenize_expression("~--~--3#")
    print(tokens)
    tokens = parse_expression("~--~--3#")
    print(tokens)


if __name__ == "__main__":
    main()
