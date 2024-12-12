from Operators.Add import Add
from Operators.Average import Average
from Operators.DigitSum import DigitSum
from Operators.Divide import Divide
from Operators.Factorial import Factorial
from Operators.Maximum import Maximum
from Operators.Minimum import Minimum
from Operators.Modulo import Modulo
from Operators.Multiply import Multiply
from Operators.Negative import Negative
from Operators.Power import Power
from Operators.Subtract import Subtract


OPERATORS = {'+': Add(), '-': Subtract(), '*': Multiply(), '/': Divide(), '^': Power(), '%': Modulo(), '$': Maximum()
    , '&': Minimum(), '@': Average(), '~': Negative(), '!': Factorial(), '#': DigitSum()}

PARENTHESIS = ('(', ')')
OTHER_CHARACTERS = ('.')


def is_number(string: str) -> bool:
    for char in string:
        if not (char.isdigit() or char == '.'):
            return False
    return True
