"""
Problem 63

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""



"""
Maths:

For any integer x, power/length n, must obide:

10**(n-1) <= x**n <= 10**n

Therefore x < 10

Also:

When 10**(n-1) = x**n:

Therefore n = (1-log10(x))**(-1)

Max when x is max (i.e. x = 9)

Therefore n_max = int(21.8) = 21
"""

from helper import *

def p63():


	count = 0
	
	for n in range(1,22):

		for i in range(1,10):

			a = splitInt(i**n)[1]

			if len(a) == n:

				count += 1

	return count


if __name__ == "__main__":

	print("Problem 63: %d" % p63())
