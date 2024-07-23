#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
	jumps = 0
	n = len(c)
	i = 0
	while i < (n - 1):
		if c[i + 1] == 1:
			i += 2
		elif i < n - 2:
			if (c[i + 1] == 0) and (c[i + 2] == 0):
				i += 2
			else:
				i += 1
		else:
			i += 1
		jumps += 1
	return jumps

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	c = list(map(int, input().rstrip().split()))

	result = jumpingOnClouds(c)

	fptr.write(str(result) + '\n')

	fptr.close()
