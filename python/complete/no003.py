#!/usr/bin/env python

# What is the largest prime factor of the number 600851475143

from python.decorators import euler_timer
from python.functions import prime_factors_simple

def main(verbose=False):
    max_factor = 0
    for factor in prime_factors_simple(600851475143):
        if factor > max_factor:
            max_factor = factor
    return max_factor

if __name__ == '__main__':
    print euler_timer(3)(main)(verbose=True)
