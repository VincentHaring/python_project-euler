"""
Helper Functions

Bunch of custom helper + math functions for use in solving these problems.
I'm sure there are existing libraries with these, but where's the fun in that.
"""

from math import *
import numpy as np
import itertools
import collections

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

	f = [1]

	r = floor(sqrt(n))

	if n%2 == 0:

		start = 2
		step = 1

	else:

		start = 3
		step = 2

	for i in range(start,r+1,step):

		if n%i == 0:

			f.append(i)

			j = int(n/i)

			if i != j:

				f.append(j)

	f.sort()

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





#########################################
# List all primes up to a given integer n
#########################################
def primesBelow(n):

	s = sieve(n)

	a = []

	for i, j in enumerate(s):
		if j:
			a.append(i+2)

	return a




#####################################################
# Returns all unique permutations for a given integer
#####################################################
def uniquePermutations(n):

	s, a = splitInt(n)

	p_list = list(itertools.permutations(a))

	p = []

	for l in p_list:
		if l[0] != 0:
			t = joinInt(s,l)
			if t not in p:
				p.append(t)

	p.sort()

	return p



##########################################################################
# Returns the differences between all ints in an array and their frequency
##########################################################################
def deltas(a):

	d = []


	l = len(a)

	if l < 2:
		return a

	for x in range(0,l-1):
		c = []
		for y in range(x+1,l):
			c.append(abs(a[x]-a[y]))
		
		for z in c:
			d.append(z)

	f = collections.Counter(d)

	return dict(f)


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



###########################################################
# Returns b**p as a list, if d provided, then last d digits
###########################################################
def listPower(b,p,d=0):

	bs = str(bin(p).replace("0b",""))
	l = len(bs)
	t = 1

	powers = []

	for i in range(0,l):
		powers.insert(0,b**(2**i))

	for i, j in enumerate(bs):
		if j=="1":
			t *= powers[i]

	if d > 0:	

		t = t%(10**d)

	e = splitInt(t)[1]

	return e


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


###############################################################
# Removes leading zeros for a given number (in splitInt format)
###############################################################
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


########################################################
# Returns value of word/name using a=1, b=2, etc scoring
########################################################
def nameScore(n):

	return sum([ord(c) - 96 for c in n.lower()])



#################################################
#Returns vector as tuple given 2 points as tuples
#################################################
def vector(a,b):

	return (b[0]-a[0],b[1]-a[1])


###################################
#Returns dot product of two vectors
###################################
def dotProduct(a,b):

	return a[0]*b[0]+a[1]*b[1]


############################################################
# Returns boolean whether given points form a right triangle
############################################################
def isRightTriangle(a,b,c):

	ab = vector(a,b)
	bc = vector(b,c)
	ac = vector(a,c)

	dotProducts = []

	dotProducts.append(dotProduct(ab,bc))
	dotProducts.append(dotProduct(bc,ac))
	dotProducts.append(dotProduct(ab,ac))

	if 0 in dotProducts:
		return True

	else:
		return False


############################################################################
# Returns boolean of whether given point falls in triangle given by 3 points
############################################################################
def pointInTriangle(a,b,c,p):

	AP_AB = crossProduct(vector(a,p),vector(a,b))
	BP_BC = crossProduct(vector(b,p),vector(b,c))
	CP_CA = crossProduct(vector(c,p),vector(c,a))

	signs = [sign(AP_AB),sign(BP_BC),sign(CP_CA)]

	# Point on corner
	if signs.count(0) == 2:

		return True

	# Point inside Triangle
	if signs.count(0) == 1:

		x = filter (lambda a: a != 0, signs)

		if x[0] == x[1]:

			return True

	if signs.count(0) == 0:

		if signs[0] == signs[1] and signs[1] == signs[2]:

			return True


	return False


############################################
# Returns cross product of two vectors A x B
############################################
def crossProduct(A,B):

	return (A[0] * B[1]) - (A[1] * B[0])


##########################
# Returns sign of a number
##########################
def sign(a):

	if a > 0:
		return 1
	elif a == 0:
		return 0
	else:
		return -1



######################################################
# Returns reciprocal of n with number repeating digits
######################################################
def recip(n):

	reciprocal = 0
	digits = 0

	remainders = []

	rem = 1
	index = 0

	rep = False

	for i in range(n):

		if rem == 0:
			break

		while rem <= n:
			index += 1
			rem *= 10

		if rem in remainders:
			rep = True
			s = remainders.index(rem)
			break

		remainders.append(rem)

		new_rem = rem%n

		reciprocal += 10**(-1*index) * ((rem-new_rem)/n)

		rem = new_rem


	if rep:
		digits = len(remainders) - s


	return (reciprocal,digits)


############################################################################
# Returns roots of a quadratic ax**2 + bx + c = 0 as array of complex tuples
############################################################################

def solveQuadratic(a,b,c):


	dis = b*b - 4*a*c


	if dis > 0:

		r1 = ((-b + dis**0.5)/(2*a),0)
		r2 = ((-b - dis**0.5)/(2*a),0)

		r = [r1,r2]

	elif dis == 0:

		r1 = (-b/(2*a),0)

		r = [r1,r1]

	else:

		r1 = (-b/(2*a),(abs(dis)**0.5)/(2*a))
		r2 = (-b/(2*a),-(abs(dis)**0.5)/(2*a))

		r = [r1,r2]

	return r



#############################################
# Return whether a given number is pentagonal
#############################################
def isPentagonal(pn):

	r = solveQuadratic(1.5,-0.5,-pn)

	for root in r:

		if root[0].is_integer() and root[1] == 0:

			return True

	return False


###############################################
# Returns pentagonal number pn for given base n
###############################################

def pentagonal(n):

	return n*(3*n-1)/2









