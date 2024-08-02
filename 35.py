#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases, width):
	result = []
	for c in cases:
		i = c[0]
		min = 3
		while i <= c[1]:
			if (min > width[i]):
				min = width[i]
			i += 1
		result.append(min)
	return result

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = int(first_multiple_input[0])

	t = int(first_multiple_input[1])

	width = list(map(int, input().rstrip().split()))

	cases = []

	for _ in range(t):
		cases.append(list(map(int, input().rstrip().split())))

	result = serviceLane(n, cases, width)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
