from abc import abstractmethod

from Operators.Operator import Operator


class BinaryOperator(Operator):
    """
        Base class of binary operators. Every binary operator extends this class
    """

    def __init__(self, precedence: float):
        super().__init__(precedence)

    @abstractmethod
    def calculate(self, num1: float, num2: float):
        pass

    @abstractmethod
    def validate_calculation(self, num1: float, num2: float):
        pass
