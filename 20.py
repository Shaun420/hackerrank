#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def reverse(x):
	rev = 0
	while (x > 0):
		rev = (rev * 10) + (x % 10)
		x //= 10
	return rev

def beautifulDays(i, j, k):
	count = 0
	for num in range(i, j + 1):
		if (abs(num - reverse(num)) % k == 0):
			count += 1
	return count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	i = int(first_multiple_input[0])

	j = int(first_multiple_input[1])

	k = int(first_multiple_input[2])

	result = beautifulDays(i, j, k)

	fptr.write(str(result) + '\n')

	fptr.close()
