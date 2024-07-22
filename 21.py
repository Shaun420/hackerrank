#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
	newarray = a.copy()
	last = 0
	for i in range(k):
		last = newarray.pop()
		newarray.insert(0, last)
	result = []
	for q in queries:
		result.append(newarray[q])
	return result

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = int(first_multiple_input[0])

	k = int(first_multiple_input[1])

	q = int(first_multiple_input[2])

	a = list(map(int, input().rstrip().split()))

	queries = []

	for _ in range(q):
		queries_item = int(input().strip())
		queries.append(queries_item)

	result = circularArrayRotation(a, k, queries)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
