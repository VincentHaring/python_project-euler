"""
Problem 13

Work out the first ten digits of the sum of the one-hundred 50-digit numbers in the file p013.txt.
"""

from helper import *

def p13():

	n = readNumbersIntoList('p013.txt')

	carry = 0

	t = []

	for j in range(len(n[0])-1,-1,-1):

		c = [item[j] for item in n]

		s = sum(c) + carry

		r = s%10

		carry = (s-r)/10

		t.insert(0, r)

	t = splitInt(carry)[1] + t

	return joinInt('+', t[0:10])


if __name__ == "__main__":

	print("Problem 13: %d" % p13())



