"""
https://www.eolymp.com/uk/submissions/15508542
by Vadym Tunik

Problem:
You are given a nonnegative integer in the m-th numeric system. Print this number in the k-th base.

Input data:
The first line of the input file contains two numbers m and k (in decimal notation), the second line contains the number to be converted.
2 ≤ m, k ≤ 36, the digits 10...35 are represented by uppercase Latin letters A...Z respectively, the number of digits does not exceed 1000.

The output:
Print in the output file the required number without leading zeros.
"""


def get_digit(char: str):
    if char.isdigit():
        return char
    else:
        return ord(char) - ord("A") + 10


def to_decimal(number: str, m=2):
    """
    m : old base of number
    """
    decimal_number = 0

    for i, char in enumerate(number[::-1]):
        digit = get_digit(char)
        decimal_number += int(digit) * m**i
    
    return decimal_number


def get_char(digit):
    if digit < 10:
        return str(digit)
    else:
        return chr(ord("A") + digit - 10)

def from_decimal(number: int, k=2):
    """
    k : new base for number
    """
    new_number = ''
    while number != 0:
        r = number % k
        number = number // k
        new_number = get_char(r) + new_number

    if new_number=='':
        return '0'
    return new_number


if __name__ == "__main__":
    m, k = [int(x) for x in input().split()]
    number = input()

    decimal_number = to_decimal(number, m)
    new_number = from_decimal(decimal_number, k)

    print(new_number)