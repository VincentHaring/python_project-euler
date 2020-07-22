"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

from helper import *

def p7():
	
	n = 10001
	upper = 105000

	s = sieve(upper)

	return [i for i, n in enumerate(s) if n == True][n-1] + 2


if __name__ == "__main__":

	print("Problem 7: %d" % p7())