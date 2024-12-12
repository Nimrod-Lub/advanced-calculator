from Util import is_number

def parse_expression(user_input: str) -> list:
    """
    Turns user input into a list of tokens

    :param: user_input: user input
    :return: list of tokens
    """
    token_list = []
    number = ""
    for char in user_input:
        if is_number(char):
            number += char

        else:
            if len(number) > 0:
                token_list.append(number)
                number = ""

            token_list.append(char)

    if len(number) > 0:
        token_list.append(number)

    return token_list


def main():
    print(parse_expression("1234*(444!)+123.123"))

if __name__ == "__main__":
    main()


