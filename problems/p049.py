"""
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the
4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting
this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from helper import *

def p49():


	l = 10000

	d = 3330

	n = 1487

	options = []

	m = 3

	primes = primesBelow(l)

	for prime in primes:
		if prime == n:
			continue
		perms = uniquePermutations(prime)

		o1 = prime + d
		o2 = prime + 2*d

		if o1 in primes and o2 in primes:
			if o1 in perms and o2 in perms:
				options.append([prime,o1,o2])


	a = []

	for p in options[0]:
		a.append(str(p))

	return ''.join(a)


if __name__ == "__main__":

	print("Problem 49: %s" % p49())
