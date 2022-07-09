"""
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from helper import *

def p25():


	fib = []

	fib.append(1)
	fib.append(1)

	i = 2
	l = 1

	while l < 1000:

		n = fib[i-1] + fib[i-2]

		l = len(splitInt(n)[1])

		fib.append(n)

		i += 1

	return i


if __name__ == "__main__":

	print("Problem 25: %d" % p25())
