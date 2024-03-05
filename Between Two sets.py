#
#There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
#
# Example
#
#
# There are two numbers between the arrays:  and .
# , ,  and  for the first value.
# ,  and ,  for the second value. Return .
#
# Function Description
#
# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
#
# getTotalX has the following parameter(s):
#
# int a[n]: an array of integers
# int b[m]: an array of integers
# Returns
#
# int: the number of integers that are between the sets
# Input Format
#
# The first line contains two space-separated integers,  and , the number of elements in arrays  and .
# The second line contains  distinct space-separated integers  where .
# The third line contains  distinct space-separated integers  where .





#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(a, b):
    """
    Returns the greatest common divisor of two numbers using Euclid's algorithm.
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Returns the least common multiple of two numbers.
    """
    return a * b // gcd(a, b)


def get_factors_of_lcm(arr):
    """
    Returns the factors of the least common multiple of all numbers in the array.
    """
    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    return result


def get_multiples_of_gcd(arr):
    """
    Returns the multiples of the greatest common divisor of all numbers in the array.
    """
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result


def getTotalX(a, b):
    """
    Returns the number of integers that are between the sets.
    """
    lcm_a = get_factors_of_lcm(a)
    gcd_b = get_multiples_of_gcd(b)

    count = 0
    current_num = lcm_a
    while current_num <= gcd_b:
        if gcd_b % current_num == 0:
            count += 1
        current_num += lcm_a
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
