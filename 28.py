#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
def jumpingOnClouds(c, k):
	energy = 99
	n = len(c)
	i = k
	if k == n:
		if c[0] == 1:
			return 97
		else:
			return 98
	while (i != 0):
		# print("i:", i, "energy:", energy)
		if c[i] == 1:
			energy -= 2
		energy -= 1
		i += k
		if i > (n - 1):
			i -= n
	if c[i] == 1:
		energy -= 2

	return energy


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	c = list(map(int, input().rstrip().split()))

	result = jumpingOnClouds(c, k)

	fptr.write(str(result) + '\n')

	fptr.close()
