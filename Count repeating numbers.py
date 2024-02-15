#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countNumbers function below.
def countNumbers(arr):
    def find_prefix_array():
        MAXIMUM = 10**6
        prefix_array = [0] * (MAXIMUM + 1)
        count = 0
        for i in range(MAXIMUM + 1):
            if is_repeated_digit_not_present(i):
                count += 1
            prefix_array[i] = count
        return prefix_array

    def is_repeated_digit_not_present(n):
        digit_set = set()
        while n != 0:
            x = n % 10
            if x in digit_set:
                return False
            digit_set.add(x)
            n //= 10
        return True

    prefix_array = find_prefix_array()
    for lower, upper in arr:
        print(prefix_array[upper] - prefix_array[lower - 1])

if __name__ == '__main__':
    q = int(input().strip())
    arr = []
    for _ in range(q):
        lower, upper = map(int, input().split())
        arr.append((lower, upper))

    countNumbers(arr)
