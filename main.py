from Calculator import calculate_expression
from ExpressionParser import parse_expression
from InfixPostfixConvertor import convert_to_postfix
from MyExceptions.InvalidDots import InvalidDots
from MyExceptions.InvalidParenthesis import InvalidParenthesis
from OperatorValidityChecker import check_operator_validity
from ValidityChecker import check_validity


def input_expressions():
    while True:

        user_input = input('Enter an expression and the solution of the expression will be printed. Enter "exit" to stop: ')
        if user_input == "exit":
            exit()

        try:
            check_validity(user_input)
        except ValueError as ve:
            print("Error:", str(ve))
        except InvalidDots as id:
            print("Error:", str(id))
        except InvalidParenthesis as ip:
            print("Error:", str(ip))
        else:
            expression_tokens = parse_expression(user_input)
            check_operators_validity(expression_tokens)
            postfix_expression = convert_to_postfix(expression_tokens)
            result = calculate_expression(postfix_expression)
            print("Result: " + str(result))




input_expressions()