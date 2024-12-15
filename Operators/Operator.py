from abc import ABC, abstractmethod



class Operator(ABC):
    _precedence: int

    def __init__(self, precedence: int):
        self._precedence = precedence

    def get_precedence(self) -> int:
        return self._precedence

    @abstractmethod
    def calculate(self, *args) -> (float, list):
        ...

    @abstractmethod
    def validate_calculation(self, *args) -> list:
        ...