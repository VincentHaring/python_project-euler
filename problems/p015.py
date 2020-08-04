"""
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from helper import *


def routes(w, h, grid):

	if w == 0 and h == 0:

		return 0

	elif w == 0 or h == 0:

		return 1

	else: 

		return grid[w-1][h] + grid[w][h-1]


def p15():

	w = 20
	h = 20

	grid = [[-1 for i in range(w+1)] for j in range(h+1)]


	grid[0][0] = 0

	for i in range(w+1):

		for j in range(h+1):

			grid[i][j] = routes(i,j,grid)

	return grid[w][h]


if __name__ == "__main__":

	print("Problem 15: %d" % p15())

