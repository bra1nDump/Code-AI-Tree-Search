
# Solution

# Python 3 program to count number of 
# sequences of songs such that there 
# are no two consecutive songs of 
# same genre and total duration is T 

# Number of songs 
n = 3

# Total duration 
T = 3

# Genre of ith song 
genre = [1, 2, 3]

# Duration of ith song 
duration = [1, 1, 1]

# dp[i][j] stores count of sequences 
# of songs such that there are no two 
# consecutive songs of same genre and 
# total duration is j 
dp = [[0 for i in range(T + 1)] 
		for i in range(n + 1)] 

# Initializing dp[i][0] 
for i in range(n + 1): 
	dp[i][0] = 1

# Initializing dp[0][j] 
for j in range(1, T + 1): 
	dp[0][j] = 0

# Filling dp[i][j] 
for i in range(1, n + 1): 
	for j in range(1, T + 1): 
		
		# If duration of current song is 
		# greater than j, then we cannot 
		# include ith song 
		if (duration[i - 1] > j): 
			dp[i][j] = dp[i - 1][j] 
		
		# If duration of current song is 
		# less than or equal to j, then 
		# we have two options: 
		# 1) We include ith song in the 
		# sequence 
		# 2) We don't include ith song 
		# in the sequence 
		else: 
			
			# If we include ith song, then 
			# we have to find sequences of 
			# length j - duration[i - 1] 
			# and we can't have two 
			# consecutive songs of same 
			# genre 
			include = dp[i - 1][j - duration[i - 1]] 
			
			# If we don't include ith song, 
			# then we have to find sequences 
			# of length j and we can't have 
			# two consecutive songs of same 
			# genre 
			exclude = dp[i - 1][j] 
			
			# If ith song has same genre as 
			# (i - 1)th song, then we have 
			# to subtract all the sequences 
			# which have (i - 1)th song as 
			# part of them 
			if (genre[i - 1] == genre[i - 2]): 
				exclude -= dp[i - 2][j] 
			
			# Adding the two cases 
			dp[i][j] = include + exclude 

# Result will be stored in dp[n][T] 
print(dp[n][T]) 

# This code is contributed by 
# Surendra_Gangwar