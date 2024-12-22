from Util import is_number, is_open_paren, is_close_paren
from OperatorsUtil import get_operator, is_unary_operator, is_left_unary_operator
from Operators.Operator import Operator


def compare_precedence(op1: Operator, op2: Operator) -> float:
    """
    Returns a positive number if the first operator has greater precedence than the second,
    a negative number if the second operator has greater precedence than the first,
    and zero if the operators have equal precedence

    :param op1: First operator
    :param op2: Second operator
    :return: a number symbolizing which operator has a larger precedence
    """
    return op1.get_precedence() - op2.get_precedence()


def convert_to_postfix(tokens: list) -> list:
    """
    Converts a list of tokens in infix notation to a list of tokens in
    postfix notation, and returns the new list

    :param tokens: list of tokens that symbolize the expression
    :return: list of tokens, this time in postfix notation rather than infix
    """

    operators_stack = []
    str_postfix = []

    for symbol in tokens:
        if is_number(symbol):
            str_postfix.append(symbol)
        elif is_open_paren(symbol):
            operators_stack.append(symbol)
        elif is_close_paren(symbol):
            while not is_open_paren(operators_stack[-1]):
                str_postfix.append(operators_stack.pop())

            operators_stack.pop()  # Get rid of the parenthesis
        else:  # Is an operator
            if is_left_unary_operator(symbol):
                operators_stack.append(symbol)
            else:
                while (len(operators_stack) > 0
                       and not is_open_paren(operators_stack[-1])
                       and compare_precedence(get_operator(operators_stack[-1]),get_operator(symbol)) >= 0):
                    str_postfix.append(operators_stack.pop())
                operators_stack.append(symbol)

    while len(operators_stack) != 0:
        str_postfix.append(operators_stack.pop())

    return str_postfix


def main():
    print(convert_to_postfix(["~", "(", "12","+", "(", "76", "*", "3", ")", "!", ")"]))

if __name__ == "__main__":
    main()

""" previous_token = None  # To track the previous token for unary check
for symbol in tokens:
    if is_number(symbol):
        str_postfix.append(symbol)

    elif is_open_paren(symbol):
        operators_stack.append(symbol)

    elif is_close_paren(symbol):
        # Pop operators until we see an open parenthesis
        while operators_stack and not is_open_paren(operators_stack[-1]):
            str_postfix.append(operators_stack.pop())
        operators_stack.pop()  # Pop the open parenthesis

    else:  # The token is an operator
        # Check if the operator is a left unary operator
        if is_left_unary_operator(symbol):
            # It's a left unary operator
            operators_stack.append(symbol)  # Handle other unary operators
        else:
            # It's a binary operator
            while (operators_stack and not is_open_paren(operators_stack[-1]) and
                   compare_precedence(get_operator(operators_stack[-1]), get_operator(symbol)) >= 0):
                str_postfix.append(operators_stack.pop())
            operators_stack.append(symbol)

    # Update the previous token tracker
    previous_token = symbol

# Pop remaining operators
while operators_stack:
    str_postfix.append(operators_stack.pop())

return str_postfix"""
