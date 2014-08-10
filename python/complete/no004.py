#!/usr/bin/env python

# Find the largest palindrome made from the
# product of two 3-digit numbers

# 100**2 = 10000 <= a*b <= 998001 = 999**2

from python.decorators import euler_timer
from python.functions import apply_to_list
from python.functions import is_palindrome


def mul(a, b):
    return a * b


def main(verbose=False):
    products = apply_to_list(mul, range(100,1000))
    max_elt = 0
    for elt in products:
        max_elt = elt
        #if is_palindrome(elt) and elt > max_elt:
        #    max_elt = elt
    return max_elt

if __name__ == '__main__':
    print euler_timer(4)(main)(verbose=True)

