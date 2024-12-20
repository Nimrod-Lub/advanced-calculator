from Util import is_number, is_open_paren, is_close_paren
from OperatorsUtil import get_operator
from Operators.Operator import Operator


def compare_precedence(op1: Operator, op2: Operator) -> int:
    return op1.get_precedence() - op2.get_precedence()


def convert_to_postfix(tokens: list) -> list:
    operators_stack = []
    str_postfix = []

    for symbol in tokens:
        if is_number(symbol):
            str_postfix.append(symbol)
        elif is_open_paren(symbol):
            operators_stack.append(symbol)
        elif is_close_paren(symbol):
            while not is_open_paren(operators_stack[-1]):
                str_postfix.append(operators_stack.pop())
            operators_stack.pop()  # Get rid of the parenthesis
        else:  # Is an operator
            while (len(operators_stack) > 0
                   and not is_open_paren(operators_stack[-1])
                   and compare_precedence(get_operator(operators_stack[-1]),get_operator(symbol)) > 0):
                str_postfix.append(operators_stack.pop())
            operators_stack.append(symbol)

    while len(operators_stack) != 0:
        str_postfix.append(operators_stack.pop())

    return str_postfix


def main():
    print(convert_to_postfix(["~", "(", "12","+", "(", "76", "*", "3", ")", "!", ")"]))

if __name__ == "__main__":
    main()

