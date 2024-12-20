OTHER_CHARACTERS = ('.')
OPEN_PARENTHESIS = ('(')
CLOSED_PARENTHESIS = (')')
PARENTHESIS = tuple(OPEN_PARENTHESIS + CLOSED_PARENTHESIS)


def is_number(string: str) -> bool:
    for char in string:
        if not (char.isdigit() or char == '.'):
            return False
    return True


def is_paren(string: str) -> bool:
    return string in PARENTHESIS


def is_open_paren(string: str) -> bool:
    return string in OPEN_PARENTHESIS


def is_close_paren(string: str) -> bool:
    return string in CLOSED_PARENTHESIS


def is_other_character(string: str) -> bool:
    return string in OTHER_CHARACTERS


def remove_white_spaces(string: str) -> str:
    """
    Removes white spaces from user input

    :param string: user input
    :return: user input without white spaces
    """
    return "".join(string.split())
