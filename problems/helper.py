"""
Helper Functions

Bunch of custom helper + math functions for use in solving these problems.
I'm sure there are existing libraries with these, but where's the fun in that.
"""

from math import *
import numpy as np

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



#########################################
# Returns all factors for a given integer
#########################################
def factors(n):

	f = []

	for i in range(1,n+1):

		if n%i == 0:

			f.append(i)

	return f





###################################################
# Returns Sieve of Eratosthenes for a given integer
###################################################
def sieve(n):

	a = [True] * (n-1)

	for i in range(2, int(sqrt(n)+1)):

		i_index = i-2

		if a[i_index]:

			j = i*i

			while j <= n:

				j_index = j-2
				a[j_index] = False
				j += i

	return a




###############################################################################
# Splits an integer into a list and sign, ( 1,234 becomes ('+',[1, 2, 3, 4]) )
###############################################################################
def splitInt(n):

	l = []
	s = "+"

	if n == 0:
		l = [0]
		return s, l

	if n < 0:

		n = abs(n)
		s = "-"

	t = str(n)

	for c in t:

		l.append(int(c))

	# p = 10

	# while n > 0:

	# 	l.insert(0,n%p)
	# 	n = int(n/p)

	return s, l



#############################################################
# Returns a long from a list of numbers (reverse of splitInt)
#############################################################
def joinInt(s, l):

	n = 0

	m = 1

	for i in range(len(l)-1,-1,-1):

		n += l[i] * m
		m *= 10

	if s == '-':
		return n * -1

	return n

###################################################
# Checks if a list reads same forwards as backwards
###################################################
def isPalindromic(l):

	r = int(len(l)/2)

	if len(l)%2 == 0:

		r += 1

	for i in range(r):

			if l[i] != l[-(i+1)]:

				return False

	return True



##########################################
# Checks if a given number is a power of n
##########################################
def isPower(n, p):

	return round(n**(1/p))**p == n


#####################################################################
# Reads numbers from a file into list of numbers (in splitInt format)
#####################################################################
def readNumbersIntoList(file):

	f = open(file, 'r')

	n = []


	for l in f:

		a = []

		l = l.strip()

		for c in l:

			a.append(int(c))

		n.append(a)

	f.close()

	return n


######################
#
######################
def removeLeadingZeroes(n):

	while n[0] == 0:

		if len(n) == 1:

			return n

		n.pop(0)

	return n

######################################################################################################
# Reads numbers from an array into list of numbers (in splitInt format) with any leading zeros removed
######################################################################################################
def readNumbersIntoArray(file):

	"""
	12 34
	56 78
	90

	becomes:

	[
	[	[ 1 , 2 ] , [ 3 , 4 ]	],
	[	[ 5 , 6 ] , [ 7 , 8 ]	],
	[	[ 9 , 0 ]	]
	]

	"""

	f = open(file, 'r')

	n = []

	for row in f:

		r = []

		row = row.strip()

		# print(row)

		for num in row.split():

			num = splitInt(int(num))

			num = removeLeadingZeroes(num[1])

			r.append(num)

		n.append(r)

	f.close()

	return n


