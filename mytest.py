import pytest
from Calculator import Calculator
from MyExceptions.ParseException import FormattingException, SyntaxException, MathematicalException

calculator = Calculator()


@pytest.mark.parametrize("expression", [
    "2*^3",
    "2++3",
    "5*/3",
    "6^*2",
    "7//3",
    "(1+2"
])
def test_syntax_errors(expression):
    with pytest.raises(FormattingException):
        calculator.calculate_expression(expression)


@pytest.mark.parametrize("expression, expected_exception", [
    ("asdlkj!@#$%", SyntaxException),
    ("1234qwerty", SyntaxException),
    ("abc123!xyz", SyntaxException),
    ("💀", SyntaxException),
    ("@#*$&", FormattingException),
    ("   ", FormattingException)
])
def test_gibberish(expression, expected_exception):
    with pytest.raises(expected_exception):
        calculator.calculate_expression(expression)


@pytest.mark.parametrize("expression", [
    "   \t\n    \t\n ",
    "                          ",
    "\t\t       \n   ",
    "\n\n\n\n",
    "   "
])
def test_whitespaces(expression):
    with pytest.raises(FormattingException):
        calculator.calculate_expression(expression)


def test_empty_string():
    with pytest.raises(FormattingException):
        calculator.calculate_expression("")


@pytest.mark.parametrize("expression, expected", [
    ("3+5", 8),
    ("10-2", 8),
    ("2*3", 6),
    ("8/2", 4),
    ("2^3", 8),
    ("10%\n\t   3", 1),
    ("5$7", 7),
    ("6&4", 4),
    ("4@6", 5),
    ("~5", -5),
    ("3! ", 6),
    ("501# ", 6),
    ("2^3+--4", 12),
    ("3^2*2", 18),
    ("10/2^2", 2.5),
    ("4!", 24),
    ("--(1)", 1),
    ("~43", -43),
    ("5^0", 1),
    ("0^10", 0),
    ("0!", 1),
    ("1!", 1),

])
def test_simple_equations(expression, expected):
    assert calculator.calculate_expression(expression) == expected


@pytest.mark.parametrize("expression, expected", [
    (" (3+5)*2-(7/2)^2+4-3+100 ", 104.75),
    ("  5^3+ (8*2)-10/2+6*300-200 ", 1736.0),
    (" (7+5)*(3^2-40  )+8-3+2 ", -365),
    (" 10 * 5 + (2^3)-4*(6/2)+1111    ", 1157.0),
    (" (2 ^3)* 5-(7+2)^2+3-8 ", -46),
    (" (6-2)^2+55*3-10/2+1-3 ", 174.0),
    (" (9+5)^2-10*200  +4+3 ", -1797),
    (" (10+5)*(3^2-2)-7+3*2 ", 104),
    (" 5*(6-2)+8/2-(3^2)+7-4 ", 18.0),
    (" 10^2+5*3-(4*6)+2-1+8 ", 100),
    (" (3+7)^2*2-(10/2)+6+5 ", 206.0),
    (" (10-2)*3+(4^2-5)*2+1-2 ", 45),
    (" (4+6)^2-3*5+(2^3-6) ", 87),
    (" (999 *2+3*5)-6^3+4*2 ", 1805),
    (" (341+444*2) ^ 2-10+  6/3*2 ", 1510435.0),
    (" (666*3)^2+4*5-(2^3*3)+90 ", 3992090),
    (" 10^2*333+(5*2)-44 +6/2 ", 33269.0),
    ("~(- 5 + 3 )  * 4+2^2-1+5", 16),
    (" 5*~3+7-(2^3*2) + 3    +----5 ", -16),
    ("23.45# $ 67.89# - 6 - 8 - 9", 7),
    ("(70 $ 500 $ 250) - ( 50 & 30) + ~20", 450),
    ("((8 + 2) * (11 - 1) ^ 3 / 4) @ 2500 @ 3500", 3000),
    (" ~-- 5+( -3*2)^3-41*6  ", -467),
    (" ~(3 + 5 * 4) - 2^3 + 10*2 ", -11),
])
def test_long_calculator_expressions(expression, expected):
    assert calculator.calculate_expression(expression) == expected


@pytest.mark.parametrize("expression, exception_type", [
    ('5+', FormattingException),
    ("5!10.2", FormattingException),
    ("5~-3", FormattingException),
    ("5~", FormattingException),
    ("8!~3", FormattingException),
    ("!7", FormattingException),
    ("5! / (0.1 $ 0.2 - 0.2) ", MathematicalException),
    ("5 % (0.1 $ 0.2 - 0.2) ", MathematicalException),
    ("~5 ^ 0.3 ", MathematicalException),
    ("~5 ^ (0.3 - 1) ", MathematicalException),
    ("0.3!" , MathematicalException),
])
def test_edge_cases(expression, exception_type):
    with pytest.raises(exception_type):
        calculator.calculate_expression(expression)

