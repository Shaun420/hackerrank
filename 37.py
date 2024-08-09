#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# https://www.hackerrank.com/challenges/encryption/problem

def encryption(s):
	r = c = 0
	newstr = ""
	for x in s:
		if x == " ":
			continue
		newstr += x
	n = len(newstr)
	l = int(math.sqrt(n))
	if (l * l == n):
		r = c = l
	elif((l * (l + 1)) >= n):
		r = l
		c = l + 1
	else:
		r = c = (l + 1)
	i = j = 0
	result = ""
	while (i < c):
		j = 0
		while (j < r):
			if(((j * c) + i) < n):
				result += newstr[(j * c) + i]
			j += 1
		result += " "
		i += 1
	return result

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	result = encryption(s)

	fptr.write(result + '\n')

	fptr.close()
