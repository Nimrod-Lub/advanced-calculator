from Calculator import Calculator
from MyExceptions.ParseException import ParseException
from Operators.Add import ADD_SIGN
from Operators.Average import AVERAGE_SIGN
from Operators.DigitSum import DIGIT_SUM_SIGN
from Operators.Divide import DIVIDE_SIGN
from Operators.Maximum import MAXIMUM_SIGN
from Operators.Minimum import MINIMUM_SIGN
from Operators.Modulo import MODULO_SIGN
from Operators.Multiply import MULTIPLY_SIGN
from Operators.Negative import NEGATIVE_SIGN
from Operators.Power import POWER_SIGN
from Operators.Subtract import SUBTRACT_SIGN


#TODO add maximum number
def info():
    print("List of available operators:")

    print(f"\t Addition      {ADD_SIGN}")
    print(f"\t Subtract      {SUBTRACT_SIGN}")
    print(f"\t Multiply      {MULTIPLY_SIGN}")
    print(f"\t Divide        {DIVIDE_SIGN}")
    print(f"\t Power         {POWER_SIGN}")
    print(f"\t Modulo        {MODULO_SIGN}")
    print(f"\t Maximum       {MAXIMUM_SIGN}")
    print(f"\t Minimum       {MINIMUM_SIGN}")
    print(f"\t Average       {AVERAGE_SIGN}")
    print(f"\t Negative      {NEGATIVE_SIGN}")
    print(f"\t Sum of digits {DIGIT_SUM_SIGN}")

    print("Extra features:")
    print("\tParenthesis, decimal point, unary minus")

def input_expressions():
    """
    Receives expressions from user and attempts to calculate the result of the expressions.
    If it's a valid expression, it prints the result of the expression, else it prints a
    fitting error message. Continues until the phrase "exit" is written

    """
    print('Welcome!\ntype "info" for list of operators\ntype "exit" to exit')

    while True:

        try:
            user_input = input(
                'Enter an expression or "exit" to exit: ')
            if user_input == "exit":
                exit()
            elif user_input == "info":
                info()
                continue

            calculator = Calculator()
            result = calculator.calculate_expression(user_input)
        except ParseException as pe:
            pe.print_exception()
        except KeyboardInterrupt:
            print("\nExiting program, received keyboard interrupt.")
            exit()
        except EOFError:
            print("\nExiting program, reached EOF")
            exit()
        else:

            print("Result: " + str(result))


if __name__ == "__main__":
    input_expressions()


