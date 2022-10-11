# Write a function or class to transpose a given N-Dimension Array. Please use your own assumptions to define an N-Dimension array data strucutre.
# When an 1D array is given, the function should throw an exception or an error as you cannot transpose an 1D array.
# When any other dimension array other than 1D is given, it should take another argument of array of integers how the axes have to be arranged.
# transpose of a matrix

N = 4
def transpose(A, B):
	for i in range(N):
		for j in range(N):
			B[i][j] = A[j][i]

# Driver code
if __name__ == '__main__':
    A = [[1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]]

# restore the written code.
B = [[0 for x in range(N)] for y in range(N)]

# function calling...!
transpose(A, B)
print("Result: ")
for i in range(N):
	for j in range(N):
		print(B[i][j], " ", end='')
	print()
