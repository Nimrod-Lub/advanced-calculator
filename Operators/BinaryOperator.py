from abc import abstractmethod

from Operators.Operator import Operator


class BinaryOperator(Operator):

    def __init__(self, precedence: int):
        super().__init__(precedence)

    @abstractmethod
    def calculate(self, *args):
        pass

    @abstractmethod
    def validate_calculation(self, *args):
        pass
