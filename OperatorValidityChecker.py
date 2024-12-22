from MyExceptions.ParseException import FormattingException
from OperatorsUtil import is_operator, is_binary_operator, \
    is_unary_operator, is_right_unary_operator, is_left_unary_operator, get_operator
from Util import is_number, is_open_paren, is_close_paren


def check_operators_and_parenthesis_validity(tokens: list):
    """
       Makes more extensive checks to find out if the user input is a valid input.
       Checks for operator related issues such as invalid placement and
       checks for parenthesis related issues such as empty parenthesis.
       Also checks operator-specific validation requirements such as negation (~)

       :param tokens: list of tokens
       :return: raises exceptions if the input is invalid
    """

    for index in range(len(tokens)):
        if is_operator(tokens[index]):
            validate_operator(tokens, index)
        elif is_close_paren(tokens[index]):
            validate_close_parenthesis(tokens, index)
        elif is_open_paren(tokens[index]):
            validate_open_parenthesis(tokens, index)


def validate_open_parenthesis(tokens: list, position: int):
    """
       Checks that the character before open parenthesis is valid.
       An exception is raised if it's not valid

       :param tokens: list of tokens
       :param position: index of current token in token list
       :return: raises exceptions if the character before is invalid
    """

    if position != 0:
        if is_number(tokens[position - 1]):
            raise FormattingException(f"{tokens[position - 1]} cannot be placed before {tokens[position]}"
                                      , ''.join(tokens))


def validate_close_parenthesis(tokens: list, position: int):
    """
       Makes multiple validity checks regarding the closed parenthesis.
       An exception is raised if something invalid is found

       :param tokens: list of tokens
       :param position: index of current token in token list
       :return: raises exceptions if something invalid is found
    """

    if is_open_paren(tokens[position - 1]):
        raise FormattingException("There are empty parenthesis", ''.join(tokens))

    if position != len(tokens) - 1:
        if is_open_paren(tokens[position + 1]) or is_number(tokens[position + 1]):
            raise FormattingException(f"{tokens[position + 1]} cannot be placed after {tokens[position]}"
                                      , ''.join(tokens))


def validate_operator(tokens: list, position: int):
    """
       Makes multiple validity checks regarding the operators.
       An exception is raised if something invalid is found

       :param tokens: list of tokens
       :param position: index of current token in token list
       :return: raises exceptions if something invalid is found
    """

    if is_unary_operator(tokens[position]):
        validate_unary_operator(tokens, position)
    elif is_binary_operator(tokens[position]):
        validate_binary_operator(tokens, position)

    get_operator(tokens[position]).validate_individual_operator(tokens, position)


def validate_binary_operator(tokens: list, position: int):
    """
           Makes multiple validity checks regarding the binary operators.
           An exception is raised if something invalid is found

           :param tokens: list of tokens
           :param position: index of current token in token list
           :return: raises exceptions if something invalid is found
    """

    if position == 0 or position == len(tokens) - 1:
        raise FormattingException(f"{tokens[position]} cannot be placed at the edge of the expression"
                                  , ''.join(tokens))

    before = tokens[position - 1]

    if not is_number(before) and not is_close_paren(before) and not is_operator(before):
        raise FormattingException(f"{before} cannot be placed before {tokens[position]}"
                                  , ''.join(tokens))

    if is_operator(before):
        if (is_binary_operator(before)
                or (is_unary_operator(before) and not is_right_unary_operator(before))):
            raise FormattingException(f"{before} cannot be placed before {tokens[position]}"
                                      , ''.join(tokens))

    after = tokens[position + 1]

    if not is_number(after) and not is_open_paren(after) and not is_operator(after):
        raise FormattingException(f"{after} cannot be placed after {tokens[position]}"
                                  , ''.join(tokens))

    if is_operator(after):
        if (is_binary_operator(after)
                or (is_unary_operator(after) and not is_left_unary_operator(after))):
            raise FormattingException(f"{after} cannot be placed after {tokens[position]}"
                                      , ''.join(tokens))


def validate_unary_operator(tokens: list, position: int):
    """
       Makes multiple validity checks regarding the unary operators.
       An exception is raised if something invalid is found

       :param tokens: list of tokens
       :param position: index of current token in token list
       :return: raises exceptions if something invalid is found
    """

    if is_left_unary_operator(tokens[position]):
        validate_left_unary_operator(tokens, position)
    elif is_right_unary_operator(tokens[position]):
        validate_right_unary_operator(tokens, position)


def validate_left_unary_operator(tokens: list, position: int):
    """
       Makes multiple validity checks regarding the left unary operators.
       An exception is raised if something invalid is found

       :param tokens: list of tokens
       :param position: index of current token in token list
       :return: raises exceptions if something invalid is found
    """

    if position == len(tokens) - 1:
        raise FormattingException(f"{tokens[position]} cannot be placed at the end of the expression"
                                  , ''.join(tokens))

    after = tokens[position + 1]

    if not is_number(after) and not is_open_paren(after) and not is_operator(after):
        raise FormattingException(f"{after} cannot be placed after {tokens[position]}"
                                  , ''.join(tokens))

    if is_operator(after):
        if (is_binary_operator(after)
                or (is_unary_operator(after) and not is_left_unary_operator(after))):
            raise FormattingException(f"{after} cannot be placed after {tokens[position]}"
                                      , ''.join(tokens))

    if position == 0:  # Don't need to check before the operator if it's at the beginning of the expression
        return

    before = tokens[position - 1]

    if not is_open_paren(before) and not is_operator(before):
        raise FormattingException(f"{before} cannot be placed before {tokens[position]}"
                                  , ''.join(tokens))

    if is_operator(before):
        if (not is_binary_operator(before)
                and is_unary_operator(before) and not is_left_unary_operator(before)):
            raise FormattingException(f"{before} cannot be placed before {tokens[position]}"
                                      , ''.join(tokens))


def validate_right_unary_operator(tokens: list, position: int):
    """
       Makes multiple validity checks regarding the right unary operators.
       An exception is raised if something invalid is found

       :param tokens: list of tokens
       :param position: index of current token in token list
       :return: raises exceptions if something invalid is found
    """

    if position == 0:
        raise FormattingException(f"{tokens[position]} cannot be placed at the beginning of the expression"
                                  , ''.join(tokens))

    before = tokens[position - 1]

    if not is_number(before) and not is_close_paren(before) and not is_operator(before):
        raise FormattingException(f"{before} cannot be placed before {tokens[position]}"
                                  , ''.join(tokens))

    if is_operator(before):
        if (is_binary_operator(before)
                or (is_unary_operator(before) and not is_right_unary_operator(before))):
            raise FormattingException(f"{before} cannot be placed after {tokens[position]}"
                                      , ''.join(tokens))

    if position == len(tokens) - 1:  # Don't need to check after the operator if it's at the end of the expression
        return

    after = tokens[position + 1]

    if not is_close_paren(after) and not is_operator(after):
        raise FormattingException(f"{after} cannot be placed after {tokens[position]}"
                                  , ''.join(tokens))

    if is_operator(after):
        if not is_binary_operator(after) and is_unary_operator(after) and not is_right_unary_operator(after):
            raise FormattingException(f"{after} cannot be placed after {tokens[position]}"
                                      , ''.join(tokens))


def main():
    check_operators_and_parenthesis_validity(["5", "!", "!", "~", "1", ])


if __name__ == "__main__":
    main()
