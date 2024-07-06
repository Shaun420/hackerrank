#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

def dayOfProgrammer(year):
	day = 0
	month = 9
	if(year < 1918):
		if(year % 4 == 0):
			day = 12
		else:
			day = 13
	elif(year > 1918):
		if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
			day = 12
		else:
			day = 13
	else:
		day = 26
	return "{0:2}.{1:0>2}.{2:4}".format(day, month, year)

if __name__ == '__main__':
	fptr = open(os.environ.get('OUTPUT_PATH', "output"), 'w')

	year = int(input().strip())

	result = dayOfProgrammer(year)

	fptr.write(result + '\n')

	fptr.close()
