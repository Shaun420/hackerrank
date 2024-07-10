#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
# https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
	turns = 0
	if n == p:
		return 0
	if (p <= (n - p)):
		for i in range(1, p, 2):
			turns += 1
	else:
		if n % 2 == 0:
			for i in range(p + 1, n + 1, 2):
				turns += 1
		else:
			for i in range(p + 1, n, 2):
				turns += 1
	return turns

if __name__ == '__main__':
	n = int(input("Enter n: ").strip())
	p = int(input("Enter p: ").strip())

	result = pageCount(n, p)
	print(result)

