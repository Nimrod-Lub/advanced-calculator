from Issues import Issue
from Util import is_number, OPERATORS, PARENTHESIS, OTHER_CHARACTERS


def check_validity(user_input: str) -> list:
    issues = []
    user_input = remove_white_spaces(user_input)

    return issues


def remove_white_spaces(string: str) -> str:
    """
    Removes white spaces from user input

    :param string: user input
    :return: user input without white spaces
    """
    return "".join(string.split())


# Should support adding more parenthesis types?
def check_parenthesis(string: str) -> list:
    stack = []
    issues = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                ...
                # Report error - close without open
    if len(stack) > 0:
        ...
        # Report error - open without close
    return issues


def check_valid_letters(string: str) -> list:
    issues = []
    for char in string:
        if not char.isdigit() and not char in OPERATORS.keys() and not char in PARENTHESIS and not char in OTHER_CHARACTERS:
            ...
            # Report error - unrecognized character

    return issues


def check_dots(string: str) -> list:
    issues = []
    curr_is_number = False
    curr_number_has_decimal = False

    for index in range(len(string)):
        if string[index] == '.':
            if index == 0 or index == len(string) - 1:  # Dot at the end or beginning
                ...
                # Report error - dot must be used as a decimal point

            else:
                if curr_is_number and not curr_number_has_decimal:  # Correct usage
                    curr_number_has_decimal = True
                    curr_is_number = False

                elif not curr_is_number and curr_number_has_decimal:  # Multiple dots in a row
                    ...
                    # Report error - dot cannot be used multiple times in a row

                elif not curr_is_number and not curr_number_has_decimal:  # Random usage of dot
                    ...
                    # Report error - dot must be used as a decimal point

                else:  # Dot used twice on one string of digits
                    ...
                    # Report error - dot is used twice on one number


        elif string[index].isdigit():
            curr_is_number = True

        else:
            if not curr_is_number and curr_number_has_decimal:
                ...
                # Report error - no digits after a decimal point
            curr_is_number = False
            curr_number_has_decimal = False

    return issues


"""
def check_number_validity(token: str):
    dot_count_edges, dot_count = 0, 0
    if token[0] == '.':
        dot_count_edges += 1
        token = token[1:]
        #handle error
    if token[-1] == '.':
        dot_count_edges += 1
        token = token[:-1]
        #handle error


"""
