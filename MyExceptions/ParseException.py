from abc import abstractmethod


class ParseException(Exception):
    """
        Custom exception class with the print_exception method
        that is used for printing the error
    """

    def __init__(self, *args):
        super().__init__(args)

    @abstractmethod
    def print_exception(self):
        pass


class SyntaxException(ParseException):
    """
        Custom exception that is used when the exact placement
        of the problematic character can be identified.
        Prints the error message, the user input and an arrow pointing at the
        problematic character
    """

    def __init__(self, message: str, user_input: str, position: int):
        super().__init__(message, user_input, position)

    def print_exception(self):
        info = self.args[0]

        print(f"Error: {info[0]}")  # Message
        user_input = info[1]
        user_input = user_input.replace("unary_minus", "-")
        user_input = user_input.replace("sign_minus", "-")
        print(user_input)  # User input
        print(' ' * info[2] + '^')  # Arrow below the position of error-causing character


class FormattingException(ParseException):
    """
        Custom exception that is used when the exact placement
        of the problematic character cannot be identified.
        Prints the error message and the user input
    """

    def __init__(self, message: str, user_input: str):
        super().__init__(message, user_input)

    def print_exception(self):
        info = self.args[0]
        user_input = info[1]
        user_input = user_input.replace("unary_minus", "-")
        user_input = user_input.replace("sign_minus", "-")

        print(f"Error: {info[0]}")  # Message
        print(user_input)  # User input


class MathematicalException(ParseException):
    """
        Custom exception that is used for mathematical errors
        such as division by zero
        Prints the error message and the problematic expression
    """

    def __init__(self, message: str, expression: str):
        super().__init__(message, expression)

    def print_exception(self):
        info = self.args[0]

        print(f"Error: {info[0]}")  # Message
        print(f"invalid expression: {info[1]}")  # expression


