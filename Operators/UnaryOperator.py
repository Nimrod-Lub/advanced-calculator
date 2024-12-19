from abc import abstractmethod

from Operators.Operator import Operator

LEFT_SIDE = "LEFT"
RIGHT_SIDE = "RIGHT"


class UnaryOperator(Operator):
    _side: str

    def __init__(self, precedence: float, side: str):
        super().__init__(precedence)
        self._side = side

    def get_side(self):
        return self._side

    @abstractmethod
    def calculate(self, *args):  #TODO make this one operand
        pass

    @abstractmethod
    def validate_calculation(self, *args):
        pass
