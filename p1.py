"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""



def p1():
	
	n = 1000

	a = 3
	b = 5

	t = 0

	for i in range(n):
		if i%a == 0:
			t = t + i
		elif i%b ==0:
			t = t + i

	return t


if __name__ == "__main__":

	print('Problem 1: %d' % p1())