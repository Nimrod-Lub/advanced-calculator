from MyExceptions.ParseException import SyntaxException, FormattingException
from Util import remove_white_spaces, is_paren, is_other_character
from OperatorsUtil import is_operator


def check_validity(user_input: str):
    """
    Checks if the user input is a valid input. Checks for general errors
    such as invalid characters and invalid dots, not operator related checks

    :param user_input: user input
    :return: raises exceptions if the input is invalid
    """

    user_input = remove_white_spaces(user_input)
    if check_empty_input(user_input):
        raise FormattingException("Empty expression", user_input) # Error - empty input
    check_valid_characters(user_input)
    check_dots(user_input)
    check_parenthesis(user_input)


def check_empty_input(string: str):
    """
    Checks if the user input is empty

    :param string: user input
    :return: true if user input is empty, else false
    """

    return len(string) == 0


def check_parenthesis(string: str):
    """
    Checks if every opened parenthesis is closed and every closed parenthesis has been opened
    in user input. Raises exceptions if not

    :param string: user input
    :return: raises exception if the parenthesis structure is invalid
    """

    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                raise FormattingException("Closing parenthesis without opening", string)

    if len(stack) > 0:
        raise FormattingException("Opening parenthesis without closing", string)


def check_valid_characters(string: str):
    """
    Checks if every character in the user input is a valid character. If not, raises exceptions

    :param string: user input
    :return: raises exceptions if there is an invalid character
    """

    for index in range(len(string)):
        char = string[index]
        if not char.isdigit() and not is_operator(char) and not is_paren(char) and not is_other_character(char):
            raise SyntaxException(f"Symbol {char} is undefined", string, index)


def check_dots(string: str):
    """
    Checks the validity of every dot in the user input.
    If a dot is not used correctly, an exception is raised

    :param string: user input
    :return: raises exceptions if dots are used incorrectly
    """

    curr_is_number = False
    curr_number_has_decimal = False

    for index in range(len(string)):
        if string[index] == '.':
            if index == 0 or index == len(string) - 1:  # Dot at the end or beginning
                raise SyntaxException("Dot is not used as a decimal point", string, index)

            else:
                if curr_is_number and not curr_number_has_decimal:  # Correct usage
                    curr_number_has_decimal = True
                    curr_is_number = False

                elif not curr_is_number and curr_number_has_decimal:  # Multiple dots in a row
                    raise SyntaxException("Dot is not used as a decimal point", string, index)

                elif not curr_is_number and not curr_number_has_decimal:  # Random usage of dot
                    raise SyntaxException("Dot is not used as a decimal point", string, index)

                else:  # Dot used twice on one string of digits
                    raise SyntaxException("Two dots are used in one number", string, index)

        elif string[index].isdigit():
            curr_is_number = True

        else:
            if not curr_is_number and curr_number_has_decimal: # No digits after a decimal point
                raise SyntaxException("There are no digits after the decimal point", string, index - 1)

            curr_is_number = False
            curr_number_has_decimal = False

