#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, b):
	max = -1
	for x in keyboards:
		for y in drives:
			if (x + y) > b:
				continue
			elif (x + y) > max:
				max = (x + y)
	return max

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	bnm = input().split()

	b = int(bnm[0])

	n = int(bnm[1])

	m = int(bnm[2])

	keyboards = list(map(int, input().rstrip().split()))

	drives = list(map(int, input().rstrip().split()))

	#
	# The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
	#

	moneySpent = getMoneySpent(keyboards, drives, b)

	fptr.write(str(moneySpent) + '\n')

	fptr.close()
