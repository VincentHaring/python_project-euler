"""
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from helper import *

def p24():

	lim = 1000000
	num = [0,1,2,3,4,5,6,7,8,9]
	lim -= 1
	l = len(num)
	ans = []

	for i in range(l):

		j = factorial(l-i-1)

		t = lim%j

		index = int((lim - t)/j)

		ans.append(num.pop(index))

		lim = t

	return joinInt('+',ans)

if __name__ == "__main__":

	print("Problem 24: %d" % p24())
