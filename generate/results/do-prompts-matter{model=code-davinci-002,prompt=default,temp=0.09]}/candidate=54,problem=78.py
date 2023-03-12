
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of playlists that can be created with the first i songs and a total duration of j.
# We will use the following recurrence relation to fill the array:
# dp[i][j] = dp[i-1][j] + dp[i-1][j-t[i]] + dp[i-1][j-2*t[i]] + ... + dp[i-1][j-k*t[i]]
# where k is the maximum number of times the ith song can be repeated in the playlist.
# We can use the following recurrence relation to calculate k:
# k = (j - (j % t[i])) / t[i]
# We can also use the following recurrence relation to calculate the number of playlists that can be created with the first i songs and a total duration of j:
# dp[i][j] = dp[i-1][j] + dp[i-1][j-t[i]] + dp[i-1][j-2*t[i]] + ... + dp[i-1][j-k*t[i]] - dp[i-2][j-t[i]] - dp[i-2][j-2*t[i]] - ... - dp[i-2][j-k*t[i]]
# This is because we don't want to count the playlists that have two consecutive songs of the same genre.
# We can use the following recurrence relation to calculate the number of playlists that can be created with the first i songs and a total duration of j:
# dp[i][j] = dp[i-1][j] + dp[i-1][j-t[i]] + dp[i-1][j-2*t[i]] + ... + dp[i-1][j-k*t[i]] - dp[i-2][j-t[i]] - dp[i-2][j-2*t[i]] - ... - dp[i-2][j-k*t[i]]
# This is because we don't want to count the playlists that have two consecutive songs of the same genre.
# We can use the following recurrence relation to calculate the number of playlists that can be created with the first i songs and a total duration of j:
# dp[i][j] = dp[i-1][j] + dp[i-1][j-t[i]] + dp[i-1][j-2*t[i]] + ... + dp[i-1][j-k*t[i]] - dp[i-2][j-t[i]] - dp[i-2][j-2*t[i]] - ... - dp[i-2][j-k*t[i]]
# This is because we don't want to count the playlists that have two consecutive songs of the same genre.
# We can use the following recurrence relation to calculate the number of playlists that can be created with the first i songs and a total duration of j:
# dp[i][j] = dp[i-1][j] + dp[i-1][j-t[i]] + dp[i-1][j-2*t[i]] + ... + dp[i-1][j-k*t[i]] - dp[i-2][j-t[i]] - dp[i-2][j-2*t[i]] - ... - dp[i-2][j-k*t[i]]
# This is because we don't want to count the playlists that have two consecutive songs of the same genre.
# We can use the following recurrence relation to calculate the number of playlists that can be created with the first i songs and a total duration of j:
# dp[i][j] = dp[i-1][j] + dp[i-1][j-t[i]] + dp[i-1][j-2*t[i]] + ... + dp[i-1][j-k*t[i]] - dp[i-2][j-t[i]] - dp[i-2][j-2*t[i]] - ... - dp[i-2][j