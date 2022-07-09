"""
Problem 48

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

from helper import *

def p48():

	n = 1000

	t = 0

	for i in range(n):

		t += (i+1)**(i+1)

	x = splitInt(t)

	y = joinInt('+',x[1][-10:])

	return y


if __name__ == "__main__":

	print("Problem 48: %d" % p48())
