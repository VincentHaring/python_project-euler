"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helper import *

def p10():

	n = 2000000

	p = sieve(n)

	return sum([x+2 for x in [i for i, n in enumerate(p) if n == True]])

	return s


if __name__ == "__main__":

	print("Problem 10: %d" % p10())