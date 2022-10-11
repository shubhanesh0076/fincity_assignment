# Problem: Groot's pie finder
# While Groot is good at heart, he is not intelligent. He loves pies but cannot find the right amount of sweetness. Groot doesn't want to eat a too sweet or bland pie. If a pie is too sweet, he wants to eat it with a pie that is bland to get to the right amount of sweetness he desires.

# Task:
# You must write a function or method that returns which pies Groot has to consume to get the right amount of sweetness.

# Input:
# One of the inputs is the sweetness values of the available pies and the other is the desired sweetness.

# Example:
# findPies([1, 2, 3, 2, 1], 6)
# returns [0, 1, 2] or [2, 1, 0]


# Function to find the minimum cost of sweets
def find(m, n, adj):
	sweet = [0] * (n + 1)
	dp = [[[ 0 for i in range(n + 1)] for i in range(n + 1)] for i in range(n + 1)]
	sweet[0] = 0

	# again assign the array into sweet
	for i in range(1, m + 1):
		sweet[i] = adj[i - 1]

	# assign the base case to the DP array
	for i in range(m + 1):
		for k in range(n + 1):
			dp[i][0][k] = 0

		for k in range(1, n + 1):
			dp[i][k][0] = -1


	for i in range(m + 1):
		for j in range(1, n + 1):
			for k in range(1, n + 1):
				dp[i][j][k] = -1
				if (i > 0 and j >= k and sweet[k] > 0 and dp[i - 1][j - k][k] != -1):
					dp[i][j][k] = dp[i - 1][j - k][k] + sweet[k]
     
				if (dp[i][j][k] == -1 or (dp[i][j][k - 1] != -1 and dp[i][j][k] > dp[i][j][k - 1])):
					dp[i][j][k] = dp[i][j][k - 1]

	# If there is solution exist.
	if (dp[m][n][n] == -1):
		return 0

	else:
		return dp[m][n][n]

m = 3
adj = [2, 1, 3, 0, 4, 10]
n = len(adj)

# CALL THE FUNCTION.....
print(find(m, n, adj))
