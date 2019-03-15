import sys
from math import sqrt


def prime_check(n: int) -> bool:
    """
    Check to see if n is a prime number or not
    :param n: an integer to prime-check
    :return: boolean
    """

    if n < 2:
        return False

    limit = int(sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False  # return False if a divisor is found

    return True  # return True if no divisor is found


if __name__ == '__main__':
    input_ = input('Enter a number: ')  # get user input

    # handle invalid inputs
    try:
        num = int(input_)
    except ValueError:
        print('A number was not entered.')
        sys.exit(0)  # quit if the input is invalid

    # print out the result
    if prime_check(num):
        print('It is a prime number.')
    else:
        print('It is not a prime number.')
