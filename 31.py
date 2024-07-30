#!/bin/python3

import numpy as np

def rowObstacle(oblist, col):
	for o in oblist:
		if o[1] == col:
			return True
	return False

def colObstacle(oblist, row):
	for o in oblist:
		if o[0] == row:
			return True
	return False

def diagObstacle(oblist, r, c):
	for o in oblist:
		if o[0] == r and o[1] == c:
			return True
	return False

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
	res = 0
	samerow = np.array([])
	samecol = np.array([])
	diag = np.array([[], []])
	k = r_q + c_q
	obstacles = np.array(obstacles)
	for o in obstacles:
		if o[0] == r_q:
			samerow.append(o)
		elif o[1] == c_q:
			samecol.append(o)
		elif (o[0] + o[1]) == k:
			diag[1].append(o)
		elif ((o[0] + o[1]) - k) % 2 == 0:
			diag[0].append(o)

	i = j = 0
	for i in range(c_q - 1, 0, -1):
		if rowObstacle(samerow, i):
			break
		res += 1
	for i in range(c_q + 1, n + 1):
		if rowObstacle(samerow, i):
			break
		res += 1
	for i in range(r_q - 1, 0, -1):
		if colObstacle(samecol, i):
			break
		res += 1
	for i in range(r_q + 1, n + 1):
		if colObstacle(samecol, i):
			break
		res += 1

	# print("1) res:", res)

	# Principal Diagonal
	i = r_q - 1
	j = c_q - 1
	while (i != 0 and j != 0):
		if diagObstacle(diag[0], i, j):
			break
		res += 1
		i -= 1
		j -= 1
	# print("2) res:", res)

	i = r_q + 1
	j = c_q + 1
	while (i != (n + 1) and j != (n + 1)):
		if diagObstacle(diag[0], i, j):
			break
		res += 1
		i += 1
		j += 1
	# print("3) res:", res)

	# Other Diagonal
	i = r_q + 1
	j = c_q - 1
	while (i != (n + 1) and j != 0):
		if diagObstacle(diag[1], i, j):
			break
		res += 1
		i += 1
		j -= 1
	# print("4) res:", res)

	i = r_q - 1
	j = c_q + 1
	while (i != 0 and j != (n + 1)):
		if diagObstacle(diag[1], i, j):
			break
		res += 1
		i -= 1
		j += 1
	# print("5) res:", res)

	return res

if __name__ == '__main__':
	fptr = open("output.txt", 'w')
	infile = open("input.txt", "r")

	first_multiple_input = infile.readline().rstrip().split()

	n = int(first_multiple_input[0])

	k = int(first_multiple_input[1])

	second_multiple_input = infile.readline().rstrip().split()

	r_q = int(second_multiple_input[0])

	c_q = int(second_multiple_input[1])

	obstacles = []

	for _ in range(k):
		obstacles.append(list(map(int, infile.readline().rstrip().split())))

	result = queensAttack(n, k, r_q, c_q, obstacles)

	fptr.write(str(result) + '\n')

	infile.close()
	fptr.close()
