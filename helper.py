"""
Helper Functions

Bunch of custom helper + math functions for use in solving these problems.
I'm sure there are existing libraries with these, but where's the fun in that.
"""

from math import *

################################################################################
# Takes integer n and returns list f of prime factors and p of powers of factors
################################################################################
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



#########################################################################
# Takes integer n and returns True if n is Prime, False if n is not Prime
#########################################################################
def isPrime(n):


	f, p = primeFactors(n)

	if f == [n]:

		return True

	return False



###############################################################################
# Splits an integer into a list and sign, ( 1,234 becomes ([1, 2, 3, 4], "+") )
###############################################################################
def splitInt(n):

	l = []
	s = "+"

	if n == 0:

		return [0]

	if n < 0:

		n = abs(n)
		s = "-"

	p = 10

	while n > 0:

		l.insert(0,n%p)
		n = int(n/p)

	return s, l



###################################################
# Checks if a list reads same forwards as backwards
###################################################
def isPalindromic(l):

	# TO-DO

	pass

	if len(l)%2 == 0:

		r = int(len(l)/2) + 1

	else:

		r = int(len(l)/2)


	for i in range(r):

			if l[i] != l[-(i+1)]:

				return False

	return True





