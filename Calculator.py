from OperatorsUtil import OPERATORS, is_unary_operator, get_operator, is_binary_operator
from Util import is_number


def calculate_expression(postfix_expression: list):
    operator_stack = []
    for token in postfix_expression:
        if is_number(token):
            operator_stack.append(token)
        else:
            result = 0.0
            if is_unary_operator(token):
                arg1 = float(operator_stack.pop())
                result = get_operator(token).calculate(arg1)
            elif is_binary_operator(token):
                arg2 = float(operator_stack.pop())
                arg1 = float(operator_stack.pop())
                result = OPERATORS[token].calculate(arg1, arg2)
            operator_stack.append(result)

    return operator_stack.pop()

def main():
    print(calculate_expression(["12", "~", "76", "3", "!", "*", "+"]))

if __name__ == "__main__":
    main()

"""
10! * 76 +-12

If it's an operand, push to operand stack.
If it's an operator:
    a. If it's a unary operator, pop once from operand stack and calculate.
    b. If it's a binary operator, pop twice from operand stack and calculate. Input the first pop as the second argument
"""