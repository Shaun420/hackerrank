#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
# https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
	factors = []
	for i in range(max(a), min(b) + 1):
		flag = False
		for x in a:
			if i % x != 0:
				flag = True
				break
		if flag == True:
			continue
		for x in b:
			if x % i != 0:
				flag = True
				break
		if flag == False:
			factors.append(i)
			continue
	return len(factors)

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = int(first_multiple_input[0])

	m = int(first_multiple_input[1])

	arr = list(map(int, input().rstrip().split()))

	brr = list(map(int, input().rstrip().split()))

	total = getTotalX(arr, brr)

	fptr.write(str(total) + '\n')

	fptr.close()
