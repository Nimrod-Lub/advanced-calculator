class InvalidDots(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class NonDecimalDot(InvalidDots):
    def __init__(self):
        super().__init__("Dot is not used as a decimal point")


class NoDigitsAfterDecimalPoint(InvalidDots):
    def __init__(self):
        super().__init__("There are no digits after a decimal point")


class TwoDecimalPointsOneNumber(InvalidDots):
    def __init__(self):
        super().__init__("There are two decimal points in one number")