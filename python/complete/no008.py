#!/usr/bin/env python

# Find the greatest product of five consecutive
# digits in the 1000-digit number.

from python.decorators import euler_timer
from python.functions import get_data


def my_reduce(iterable):
    acc = 1
    for val in iterable:
        acc = acc * val
    return acc


def my_max(iterable):
    maximum = 0
    for val in iterable:
        if val > maximum:
            maximum = val
    return maximum


def product_consec_digits(number, consecutive):
    """
    Returns the largest product of "consecutive"
    consecutive digits from number
    """
    digits = [int(dig) for dig in str(number)]
    max_start = len(digits) - consecutive
    return [my_reduce(digits[i:i + consecutive])
            for i in range(max_start + 1)]

def main(verbose=False):
    lines = [line.strip() for line in get_data(8).split('\n')]
    n = "".join(lines)

    return my_max(product_consec_digits(n, 5))

if __name__ == '__main__':
    print euler_timer(8)(main)(verbose=True)
