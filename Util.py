OTHER_CHARACTERS = ('.')
OPEN_PARENTHESIS = ('(')
CLOSED_PARENTHESIS = (')')
PARENTHESIS = tuple(OPEN_PARENTHESIS + CLOSED_PARENTHESIS)


def is_number(string: str) -> bool:
    """
    Checks if the given string is a number, returns true if it is, else returns false

    :param string: a token
    :return: true if the token is a number, else false
    """

    for char in string:
        if not (char.isdigit() or char == '.'):
            return False
    return True


def is_paren(string: str) -> bool:
    """
    Checks if the given string is a parenthesis, returns true if it is, else returns false

    :param string: a token
    :return: true if the token is a parenthesis, else false
    """

    return string in PARENTHESIS


def is_open_paren(string: str) -> bool:
    """
    Checks if the given string is an open parenthesis, returns true if it is, else returns false

    :param string: a token
    :return: true if the token is an open parenthesis, else false
    """

    return string in OPEN_PARENTHESIS


def is_close_paren(string: str) -> bool:
    """
    Checks if the given string is a close parenthesis, returns true if it is, else returns false

    :param string: a token
    :return: true if the token is a close parenthesis, else false
    """

    return string in CLOSED_PARENTHESIS


def is_other_character(string: str) -> bool:
    """
    Checks if the given string is a special character, returns true if it is, else returns false

    :param string: a token
    :return: true if the token is a special character, else false
    """

    return string in OTHER_CHARACTERS


def remove_white_spaces(string: str) -> str:
    """
    Removes white spaces from user input

    :param string: user input
    :return: user input without white spaces
    """
    return "".join(string.split())