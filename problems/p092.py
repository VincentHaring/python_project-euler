"""
Problem 92

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

from helper import *

def p92():


	lim = 10000000
	chain = set()
	chain.add(89)

	ends = set()
	ends.add(89)
	ends.add(1)

	for i in range(1,lim):

		temp_chain = set()
		temp_chain.add(i)

		if i in chain:
			continue

		nj = i

		# for k in range(10):

		while nj not in ends and nj not in chain:

			s = 0

			ns = splitInt(nj)[1]

			for j in range(len(ns)):

				s += ns[j]**2

			nj = s

			temp_chain.add(nj)

			if nj in chain:

				for m in temp_chain:

					chain.add(m)

	return len(chain)

if __name__ == "__main__":

	print("Problem 92: %d" % p92())
