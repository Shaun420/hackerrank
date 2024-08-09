#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# https://www.hackerrank.com/challenges/minimum-distances/problem

def minimumDistances(a):
	n = len(a)
	d = n
	for i in range(n):
		j = i + 1
		while ((j < (d + i)) and (j < n)):
			if (a[j] == a[i]):
				d = (j - i)
				break
			j += 1
	if (d == n):
		return -1
	else:
		return d
				

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	a = list(map(int, input().rstrip().split()))

	result = minimumDistances(a)

	fptr.write(str(result) + '\n')

	fptr.close()
