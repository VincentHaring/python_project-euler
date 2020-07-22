"""
Helper Functions

Bunch of custom helper + math functions for use in solving these problems.
I'm sure there are existing libraries with these, but where's the fun in that.
"""

from math import *


# Takes integer n and returns True if n is Prime, False if n is not Prime
def isPrime(n):


	f, p = primeFactors(n)

	if f == [n]:

		return True

	return False

# Takes integer n and returns list f of prime factors and p of powers of factors
def primeFactors(n):

	f = []
	p = []

	if n < 2:

		return f, p

	k = 2


	while n != 1:

		if n%k == 0:

			f.append(k)

			m = 0

			while n%k == 0:

				n /= k
				m += 1

			p.append(m)

		k += 1

	return f, p