#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
# https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
	frequency = [-1 for i in range(101)]
	for x in arr:
		if frequency[x] == -1:
			frequency[x] = arr.count(x)
	max_freq = -1
	max_no = 0
	for i in range(1, len(frequency)):
		if max_freq < frequency[i]:
			max_freq = frequency[i]
			max_no = i
	deletions = 0
	for i in range(1, len(frequency)):
		if frequency[i] != -1 and i != max_no:
			deletions += frequency[i]
	return deletions

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	arr = list(map(int, input().rstrip().split()))

	result = equalizeArray(arr)

	fptr.write(str(result) + '\n')

	fptr.close()
