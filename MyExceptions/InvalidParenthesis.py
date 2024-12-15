class InvalidParenthesis(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ClosingUnopenedParenthesis(InvalidParenthesis):
    def __init__(self):
        super().__init__("Closing parenthesis without opening")


class OpenParenthesis(InvalidParenthesis):
    def __init__(self):
        super().__init__("There is an open parenthesis")
