
# Solution

# This solution is based on the idea that we can use dynamic programming to solve this problem.
# We will use a 2D array to store the number of playlists that can be created with the first i songs
# and with a total duration of j.

# The recurrence relation is as follows:
# dp[i][j] = dp[i-1][j] + dp[i-1][j-t[i]]
# where t[i] is the duration of the ith song.

# The first term in the recurrence relation is the number of playlists that can be created with the first i-1 songs
# and with a total duration of j.

# The second term in the recurrence relation is the number of playlists that can be created with the first i-1 songs
# and with a total duration of j-t[i].

# The second term is added because we can add the ith song to the end of the playlist.

# The recurrence relation can be modified to take into account the constraint that two songs of the same genre
# cannot be played consecutively.

# The recurrence relation is as follows:
# dp[i][j] = dp[i-1][j] + dp[i-1][j-t[i]] - dp[i-2][j-t[i]]
# where t[i] is the duration of the ith song.

# The second term in the recurrence relation is the number of playlists that can be created with the first i-1 songs
# and with a total duration of j-t[i].

# The third term in the recurrence relation is the number of playlists that can be created with the first i-2 songs
# and with a total duration of j-t[i].

# The third term is subtracted because we can add the ith song to the end of the playlist.
# However, if the ith song has the same genre as the (i-1)th song, then we cannot add the ith song to the end of the playlist.
# Thus, we subtract the number of playlists that can be created with the first i-2 songs and with a total duration of j-t[i].

# The time complexity of this solution is O(n*T) where n is the number of songs and T is the total duration.
# The space complexity of this solution is O(n*T).

# The solution is implemented below.

# Importing the required libraries.
import sys

# Defining the modulus.
mod = 10**9 + 7

# Reading the input.
n, T = map(int, input().split())

# Creating the array to store the durations of the songs.
t = [0] * (n + 1)

# Creating the array to store the genres of the songs.
g = [0] * (n + 1)

# Creating the 2D array to store the number of playlists that can be created with the first i songs
# and with a total duration of j.
dp = [[0] * (T + 1) for _ in range(n + 1)]

# Creating the 2D array to store the number of playlists that can be created with the first i songs
# and with a total duration of j.
dp2 = [[0] * (T + 1) for _ in range(n + 1)]

# Creating the 2D array to store the number of playlists that can be created with the first i songs
# and with a total duration of j.
dp3 = [[0] * (T + 1) for _ in range(n + 1)]

# Creating the 2D array to store the number of playlists that can be created with the first i songs
# and with a total duration of j.
dp4 = [[0] * (T + 1) for _ in range(n + 1)]

# Creating the 2D array to store the number of playlists that can be created with the first i songs
# and with a total duration of j.
dp5 = [[0] * (T + 1) for _ in range(n + 1)]

# Creating the 2D array to store the number of playlists that can be created with the first i songs
# and with a total duration of j.
dp6 = [[0] * (T + 1) for _ in range(n + 1)]

# Creating the 2D array to store the number of playlists that can be created with the first i songs
