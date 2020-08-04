"""
Problem 16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

from helper import *

def p16():

	n = 1000

	return sum(splitInt(2**n)[1])


if __name__ == "__main__":

	print("Problem 16: %d" % p16())
