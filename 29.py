#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
	if k >= (len(s) + len(t)):
		return "Yes"
	i = 0
	op = 0
	while i < (min(len(s), len(t))):
		if s[i] == t[i]:
			i += 1
		else:
			break
	op += len(s) - i
	op += len(t) - i
	#print("op:", op)
	if k >= op:
		if ((k - op) % 2 == 0):
			return "Yes"
		else:
			return "No"
	else:
		return "No"

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	t = input()

	k = int(input().strip())

	result = appendAndDelete(s, t, k)

	fptr.write(result + '\n')

	fptr.close()
