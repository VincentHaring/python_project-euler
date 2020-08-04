"""
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

from helper import *

def p30():

	n = []

	p = 5

	l = 200000

	for i in range(2,l):

		a = splitInt(i)

		b = [int(i)**p for i in a[1]]

		if sum(b) == i:

			n.append(i)

	return sum(n)


if __name__ == "__main__":

	print("Problem 30: %d" % p30())



