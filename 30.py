#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
# https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):
	count = s.count("a")
	m = len(s)
	extra = n % m
	repeat = (n // m) - 1
	count += (count * repeat)
	count += s[:extra].count("a")
	return count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	n = int(input().strip())

	result = repeatedString(s, n)

	fptr.write(str(result) + '\n')

	fptr.close()
