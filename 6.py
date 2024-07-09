#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    frequency = [0, 0, 0, 0, 0]
    for x in arr:
        frequency[x - 1] += 1
    print(frequency)
    max = 0
    ids = []
    for i in range(len(frequency)):
        if frequency[i] > max:
            ids.clear()
            ids.append(i + 1)
            max = frequency[i]
        elif frequency[i] == max:
            ids.append(i + 1)
    return min(ids)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
