#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
# https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    sum = 0
    for i in range(n):
        if (i == k):
            continue
        sum += bill[i]
    if (b == (sum / 2)):
        print("Bon Appetit")
    else:
        print(int(bill[k] / 2))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
