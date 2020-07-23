"""
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from helper import *

def p9():

	n = 1000

	for a in range(1,400):
		for b in range(1,400):

			c2 = a**2 + b**2

			if isSquare(c2):

				c = sqrt(c2)

				if (a + b + c) == 1000:

					return a*b*c

	return 0


if __name__ == "__main__":

	print("Problem 9: %d" % p9())