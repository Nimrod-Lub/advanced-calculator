from abc import ABC, abstractmethod

LARGEST_PRECEDENCE = 100


class Operator(ABC):
    """
        Base class of operators. Every operator extends this class
    """

    _precedence: float

    def __init__(self, precedence: float):
        self._precedence = precedence

    def get_precedence(self) -> float:
        return self._precedence

    @abstractmethod
    def calculate(self, *args) -> (float, list):
        ...

    @abstractmethod
    def validate_calculation(self, *args) -> list:
        ...

    def validate_individual_operator(self, tokens: list, position: int):
        """
            An operator with specific validity requirements that are not related to
            its type can override this method and makes the extra validity checks

            :param tokens: list of tokens
            :param position: index of current token in token list
            :return: raises exceptions if something invalid is found
        """
        pass
