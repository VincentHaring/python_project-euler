"""
Problem 91

The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.


Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""

from helper import *

def p91():

	boundary = 50
	count = 0

	for i in range(boundary+1):
		for j in range(boundary+1):
			
			if (i == 0 and j == 0):
				continue

			coord1 = (i,j)

			for a in range(boundary+1):
				for b in range(boundary+1):

					if (a == 0 and b == 0):
						continue

					coord2 = (a,b)

					if coord1 == coord2:
						continue

					if isRightTriangle((0,0),coord1,coord2):
						count = count + 1

	return count/2


if __name__ == "__main__":

	print("Problem 91: %d" % p91())
