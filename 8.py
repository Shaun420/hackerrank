#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    pairs = 0
    socks = [0 for x in range(100)]
    for i in range(len(ar)):
        socks[ar[i] - 1] += 1
    for i in range(len(socks)):
        pairs += int(socks[i] / 2)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
