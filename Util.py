OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6}
PARENTHESIS = ('(', ')')
OTHER_CHARACTERS = ('.')

LEFT_SIDE = "LEFT"
RIGHT_SIDE = "RIGHT"

def is_number(string: str) -> bool:
    return string.isdigit() or string == '.'