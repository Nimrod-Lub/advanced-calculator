from ExpressionParser import parse_expression
from InfixPostfixConvertor import convert_to_postfix
from MyExceptions.ParseException import MathematicalException, FormattingException
from OperatorValidityChecker import check_operators_and_parenthesis_validity
from OperatorsUtil import OPERATORS, is_unary_operator, get_operator, is_binary_operator, is_left_unary_operator
from Util import is_number
from ValidityChecker import check_validity

PRECISION = 10

class Calculator:
    def calculate_postfix_expression(self, postfix_expression: list):
        """
        Solves the expression and returns the answer. The algorithm strategy:
        If it's an operand, push to operand stack.
        If it's an operator:
            a. If it's a unary operator, pop once from operand stack and calculate.
            b. If it's a binary operator, pop twice from operand stack and calculate. Input the first pop as the second argument
            Push the result back inside the operator stack
        Return the number inside the operand stack at the end

        :param postfix_expression: list containing the expression in postfix notation
        :return: the result of the expression
        """

        operator_stack = []
        for token in postfix_expression:
            if is_number(token):
                operator_stack.append(token)
            else:
                try:
                    result = 0.0
                    if is_unary_operator(token):
                        arg1 = operator_stack.pop()
                        result = get_operator(token).calculate(float(arg1))

                    elif is_binary_operator(token):
                        arg2 = operator_stack.pop()
                        arg1 = operator_stack.pop()
                        result = get_operator(token).calculate(float(arg1), float(arg2))
                    result = round(result, PRECISION)
                    operator_stack.append(result)
                except OverflowError:
                    raise MathematicalException("Number is too big or too small"
                                                ,f"problematic operator: {token}")

        if len(operator_stack) > 1:
            raise FormattingException("Not enough binary operators in expression", "")

        return operator_stack.pop()


    def calculate_expression(self, user_input: str):
        """
        Validates the user input, tokenizes the expression, converts it to postfix,
        calculates the answer of the expression, and returns the answer.
        If there was a problem along the way, the program raises an exception

        :param user_input: user input
        :return: the answer of the expression the user inputted if it's a valid expression, else will raise an exception
        """

        check_validity(user_input)
        expression_tokens = parse_expression(user_input)
        check_operators_and_parenthesis_validity(expression_tokens)
        postfix_expression = convert_to_postfix(expression_tokens)
        result = self.calculate_postfix_expression(postfix_expression)
        return result



def main():
    calculator = Calculator()
    print(calculator.calculate_postfix_expression(["12", "~", "76", "3", "!", "*", "+"]))

if __name__ == "__main__":
    main()
