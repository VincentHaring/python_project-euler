"""
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from helper import *
from functools import reduce


def p5():
	
	n = 20

	factors = []
	powers = []
	total = 1

	for i in range(n,0,-1):

		f, p = primeFactors(i)

		for j in range(len(f)):

			if f[j] not in factors:
				factors.append(f[j])
				powers.append(p[j])
			else:
				index = factors.index(f[j])

				if powers[index] < p[j]:

					powers[index] = p[j]


	for i in range(len(factors)):
		total *= factors[i] ** powers[i]

	return total

if __name__ == "__main__":

	print("Problem 5: %d" % p5())