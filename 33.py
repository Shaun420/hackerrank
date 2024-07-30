#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
# https://www.hackerrank.com/challenges/acm-icpc-team/problem

def acmTeam(topic):
	t = len(topic)
	l = len(topic[0])
	i = 0
	maxtopics = 0
	n = 0
	while (i < t):
		j = 0
		while (j < i):
			topics = 0
			k = 0
			if (i == j):
				j += 1
				continue
			while(k < l):
				if (topic[i][k] == "1" or topic[j][k] == "1"):
					topics += 1
				k += 1
			if (topics == maxtopics):
				n += 1
			elif (topics > maxtopics):
				maxtopics = topics
				n = 1
			j += 1
		i += 1
	print(topic)
	return maxtopics, n

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = int(first_multiple_input[0])

	m = int(first_multiple_input[1])

	topic = []

	for _ in range(n):
		topic_item = input()
		topic.append(topic_item)

	result = acmTeam(topic)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
