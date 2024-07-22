#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
# https://www.hackerrank.com/challenges/save-the-prisoner/problem

def saveThePrisoner(n, m, s):
	x = m % n
	if (x + s - 1) == 0:
		return n
	if (x + s - 1) > n:
		return (x + s - n - 1)
	return (x + s - 1)

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input().strip())

	for t_itr in range(t):
		first_multiple_input = input().rstrip().split()

		n = int(first_multiple_input[0])

		m = int(first_multiple_input[1])

		s = int(first_multiple_input[2])

		result = saveThePrisoner(n, m, s)

		fptr.write(str(result) + '\n')

	fptr.close()
