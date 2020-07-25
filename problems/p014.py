"""
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from helper import *

limit = 1000000
vals = {1: 1}

def collatzSteps(n):
	
	if n in vals:
		return vals[n]

	if n%2 == 0:

		x = 1 + collatzSteps(int(n/2))

		vals[n] = x

	else:

		x = 2 + collatzSteps(int( ((3*n)+1) / 2 ))

		vals[n] = x


	return vals[n]


def p14():


	l = 0
	j = 1

	for i in range(int(limit/2), limit):

		a = collatzSteps(i+1)

		if a > l:

			l = a
			j = i+1

	return j


if __name__ == "__main__":

	print("Problem 14: %d" % p14())

