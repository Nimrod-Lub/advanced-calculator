from abc import abstractmethod

from Operators.Operator import Operator

LEFT_SIDE = "LEFT"
RIGHT_SIDE = "RIGHT"


class UnaryOperator(Operator):
    """
        Base class of unary operators. Every unary operator extends this class
    """

    _side: str

    def __init__(self, precedence: float, side: str):
        super().__init__(precedence)
        self._side = side

    def get_side(self):
        return self._side

    @abstractmethod
    def calculate(self, num: float):
        pass

    @abstractmethod
    def validate_calculation(self, num: float):
        pass
