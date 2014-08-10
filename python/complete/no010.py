#!/usr/bin/env python

# Find the sum of all the primes below two million.

from python.decorators import euler_timer
from python.functions import sieve


def my_sum(iterable):
    s = 0
    for val in iterable:
        s = s + val
    return s


def main(verbose=False):
    return my_sum(sieve(2000000 - 1))

if __name__ == '__main__':
    print euler_timer(10)(main)(verbose=True)
