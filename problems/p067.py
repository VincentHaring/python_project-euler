"""
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in p067.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether!
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

from helper import *

def p67():

	n = readNumbersIntoArray('p067.txt')



	for row in range(len(n)-2,-1,-1):

		for num in range(len(n[row])):

			n[row][num] = splitInt(joinInt('+',n[row][num]) + max(joinInt('+',n[row+1][num]), joinInt('+',n[row+1][num+1])))[1]

	return joinInt('+',n[0][0])


if __name__ == "__main__":

	print("Problem 67: %d" % p67())
