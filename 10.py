#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
# https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(steps, path):
    valleys = 0
    altitude = 0
    for step in path:
        if step == "U":
            altitude += 1
            if (altitude == 0):
                valleys += 1
        elif step == "D":
            altitude -= 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
