"""
Problem 22

Using p022.txt, a text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from helper import *

def p22():

	f = open('p022.txt', 'r')

	names = []

	t = 0

	for l in f:

		a = l.split(',')

		for n in a:

			names.append(n.strip('"'))

	names.sort()

	for i in range(len(names)):

		s = nameScore(names[i])

		t += ((i+1) * s)

	return t

if __name__ == "__main__":

	print("Problem 22: %d" % p22())
