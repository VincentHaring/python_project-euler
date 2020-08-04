"""
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle in p018.txt

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
and requires a clever method! ;o)
"""

from helper import *

def p18():

	n = readNumbersIntoArray('p018.txt')



	for row in range(len(n)-2,-1,-1):

		for num in range(len(n[row])):

			n[row][num] = splitInt(joinInt('+',n[row][num]) + max(joinInt('+',n[row+1][num]), joinInt('+',n[row+1][num+1])))[1]

	return joinInt('+',n[0][0])


if __name__ == "__main__":

	print("Problem 18: %d" % p18())
