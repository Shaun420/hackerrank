#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
	maxheight = 0
	for x in word:
		if (h[ord(x) - 97] > maxheight):
			maxheight = h[ord(x) - 97]
	return (maxheight * len(word))

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	h = list(map(int, input().rstrip().split()))

	word = input()

	result = designerPdfViewer(h, word)

	fptr.write(str(result) + '\n')

	fptr.close()
