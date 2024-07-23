#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
# https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
	answer = []
	while len(arr) > 0:
		answer.append(len(arr))
		length = min(arr)
		i = 0
		while i < len(arr):
			if (arr[i] == length):
				arr.pop(i)
			else:
				arr[i] -= 1
				i += 1
	# answer.append(1)
	return answer

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	arr = list(map(int, input().rstrip().split()))

	result = cutTheSticks(arr)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
