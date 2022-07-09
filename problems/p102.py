"""
Problem 102
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random"
triangles, find the number of triangles for which the interior contains the origin.
"""

from helper import *

def p102():

	sum = 0

	f = open('p102.txt','r')

	for row in f:
		points = row.split(',')
		a = (int(points[0]),int(points[1]))
		b = (int(points[2]),int(points[3]))
		c = (int(points[4]),int(points[5]))

		if pointInTriangle(a,b,c,(0,0)):
			sum += 1

	f.close()

	return sum


if __name__ == "__main__":

	print("Problem 102: %d" % p102())
