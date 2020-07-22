"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from helper import *


def p3():
	
	n = 600851475143

	f, p = primeFactors(n)

	return max(f)


if __name__ == "__main__":

	print("Problem 3: %d" % p3())