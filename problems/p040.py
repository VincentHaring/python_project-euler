"""
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from helper import *

def p40():

	n = []

	a = 1

	while len(n) < 1000000:

		n += splitInt(a)[1]

		a += 1

	b = n[0] * n[9] * n[99] * n[999] * n[9999] * n[99999] * n[999999]

	return b


if __name__ == "__main__":

	print("Problem 40: %d" % p40())
