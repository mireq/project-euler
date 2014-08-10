#!/usr/bin/env python

# An irrational decimal fraction is created by concatenating
# the positive integers:
# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If d_n represents the nth digit of the fractional part, find the
# value of the following expression.
# d_1 X d_10 X d_100 X d_1000 X d_10000 X d_100000 X d_1000000

import operator

from python.decorators import euler_timer

def num_digs_with_up_to_d_digits(d):
    # The smallest number with d + 1 digits is 10**d
    # S = sum_(i = 1)^d i*9*10**(i - 1) = 0.9 * sum_(i = 1)^d i 10**i
    # 10S - S = 0.9 sum_(i = 1)^d i 10**(i + 1) - 0.9 sum_(i = 1)^d i 10**i
    # 10S = sum_(i = 2)^(d + 1) (i - 1) 10**i - sum_(i = 1)^d i 10**i
    # 10S = d*10**(d + 1) - sum_(i = 1)^d 10**i
    # 90S = 9*d*10**(d + 1) - 10**(d + 1) + 10
    # 9S = (9*d - 1)*10**d + 1
    return ((9*d - 1)*pow(10, d) + 1)/9

def nth_digit_of_frac_part(n):
    num_digits = 1
    while num_digs_with_up_to_d_digits(num_digits) < n:
        num_digits += 1

    # We know the nth digit occurs in the block of integers with num_digits
    # digits. We want to determine which digit in the block it is
    place_in_digits = n - num_digs_with_up_to_d_digits(num_digits - 1)
    digit_place_in_number = (place_in_digits - 1) % num_digits + 1
    # intended to be integer division
    numbers_prior = (place_in_digits - 1)/num_digits

    # Since there are numbers_prior numbers of num_digits digits prior to
    # the number we are interested in, we need to calculate which number it is
    # The smallest number with num_digits digits is 10**(num_digits - 1)
    num_of_interest = str(pow(10, (num_digits - 1)) + numbers_prior)
    return int(num_of_interest[digit_place_in_number - 1])

def main(verbose=False):
    # d_1 X d_10 X d_100 X d_1000 X d_10000 X d_100000 X d_1000000
    result = [nth_digit_of_frac_part(pow(10, exponent)) for exponent in range(7)]
    digit_display = ['d_%s = %s' % (pow(10, i), digit)
                     for i, digit in enumerate(result)]
    if verbose:
        return '%s.\nThe digits are as follows: %s' % (
            reduce(operator.mul, result), ', '.join(digit_display))
    else:
        return reduce(operator.mul, result)

if __name__ == '__main__':
    print euler_timer(40)(main)(verbose=True)
