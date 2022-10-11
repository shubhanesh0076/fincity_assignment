# Problem: Ironman's legacy in trouble
# Design a data structure to help Avengers handle massive data from the cosmic receptors installed on the roof of the new Avengers building by Ironman before his untimely demise.

# These receptors can listen to an 'N' number of planets anytime. It starts with 'N' zeros and then adds the number received for the planet range. Blackwidow finally tallies and sees what planet range received the highest numbers and asks one of the avengers to visit that planet range to see if everything is ok. She then resets it to zeros, and the cosmic receptors will start adding the numbers.

# When Ironman installed these receptors, he didn't consider the number of planets they would monitor. With Captain Marvel joining the band of Avengers, the receptors cannot keep up with the naive algorithm written.

# Task:
# The naive method involves taking an array of numbers filled with zeros and adding the number received for the range of indexes. But with millions of planets sending numbers, this approach is not viable. You should design a data structure to handle this range of indexes better.

# Input:
# Write a function or method to take the number of planets and array of reception. Each reception is an array of three numbers from and to (excluded) range of planets and a number to add. This function will return the range of planets with the largest number and the number.

# Example:
# findTheRange(5, [[2, 4, 5], [1, 3, 6], [2, 4, 7]]) returns [2, 3, 18]

# Explanation:
# Initially, it starts with

# [0, 0, 0, 0, 0]

# After receiving [2, 4, 5]

# [0, 0, 5, 5, 0]

# After receiving [1, 3, 6]

# [0, 6, 11, 5, 0]

# Finally, after receiving [2, 4, 7]

# [0, 6, 18, 12, 0]

# Since 18 is the largest and falls in the range [2, 3, 18] that is returned

#WRITE SOLUTION HERE......................
import sys
def maximizeExpr(a, n, x, y, z):

	# Traverse the whole array and compute left maximum for every index.
	L = [0] * n
	L[0] = x * a[0]
	for i in range(1, n):
		L[i] = max(L[i - 1], x * a[i])

	# Compute right maximum for every index.
	R = [0] * n
	R[n - 1] = z * a[n - 1]
	for i in range(n - 2, -1, -1):
		R[i] = max(R[i + 1], z * a[i])

	ans = -sys.maxsize
	for i in range(0, n):
		ans = max(ans, L[i] + y * a[i] + R[i])
	return ans
a = [-1, -2, -3, -4, -5]
n = len(a)
x = 1
y = 2
z = -3
print(maximizeExpr(a, n, x, y, z))
