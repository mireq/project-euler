#!/usr/bin/env python

# There exists exactly one Pythagorean triplet for which
# a + b + c = 1000. Find the product abc.

import operator

from python.decorators import euler_timer

def my_reduce(iterable):
    acc = 1
    for val in iterable:
        acc = acc * val
    return acc

def first_triplet(total):
    for a in range(1, total - 1):
        for b in range(1, total - a):
            c = total - a - b
            if a*a + b*b == c*c:
                return [a,b,c]

    return []

def main(verbose=False):
    return my_reduce(first_triplet(1000))

if __name__ == '__main__':
    print euler_timer(9)(main)(verbose=True)
