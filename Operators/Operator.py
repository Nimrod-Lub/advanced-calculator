from abc import ABC, abstractmethod

LARGEST_PRECEDENCE = 100


class Operator(ABC):
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
        pass
