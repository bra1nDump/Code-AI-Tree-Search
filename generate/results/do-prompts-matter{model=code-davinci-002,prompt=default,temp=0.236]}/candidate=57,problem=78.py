
# Solution

# Python 3 program to count number of ways 
# to play a playlist of songs 

# modulo value 
mod = 1000000007

# dp[i][j] is going to store count of playlist 
# of length i with last song genre j. 
dp = [[0 for i in range(4)] 
		for i in range(16)] 

# Function to count number of playlist of length 
# n with last song genre j. 
def countplaylist(n, j): 

	# If we have reached end of playlist. 
	if (n == 0): 
		return 1

	# If value is already computed. 
	if (dp[n][j] != 0): 
		return dp[n][j] 

	ans = 0

	# Recur for all possible previous 
	# song genres. 
	for i in range(1, 4): 

		# If two consecutive songs have 
		# same genre then ignore. 
		if (i != j): 
			ans = (ans + countplaylist(n - 1, i)) 

	# Store result and return it. 
	dp[n][j] = ans 
	return ans 

# Driver Code 
n = 3
T = 3

# Initialize all entries of dp as 0. 
dp = [[0 for i in range(4)] 
		for i in range(16)] 

# Call function to count number of playlist 
# of length T with no two consecutive 
# songs of same genre. 
ans = 0
for i in range(1, 4): 
	ans = (ans + countplaylist(T, i)) 

# Print result. 
print(ans) 

# This code is contributed by mits