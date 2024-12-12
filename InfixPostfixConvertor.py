from Util import OPERATORS, is_number
from Operators.Operator import Operator


def compare_precedence(op1: Operator, op2: Operator) -> int:
    return op1.get_precedence() - op2.get_precedence()


def convert_to_postfix(tokens: list) -> list:
    operators_stack = []
    str_postfix = []

    for symbol in tokens:
        if is_number(symbol):
            str_postfix += symbol
        elif symbol == '(':
            operators_stack.append(symbol)
        elif symbol == ')':
            while operators_stack[-1] != '(':
                str_postfix += operators_stack.pop()
            operators_stack.pop() # Get rid of the parenthesis
        else: # Is an operator
            while len(operators_stack) > 0 and compare_precedence(OPERATORS[operators_stack[-1]], OPERATORS[symbol]) > 0:
                str_postfix += operators_stack.pop()
            operators_stack.append(symbol)

    while len(operators_stack) != 0:
        str_postfix += operators_stack.pop()

    return str_postfix


def main():
    print(convert_to_postfix([["1234"],"+", ["12312"]]))

if __name__ == "__main__":
    main()