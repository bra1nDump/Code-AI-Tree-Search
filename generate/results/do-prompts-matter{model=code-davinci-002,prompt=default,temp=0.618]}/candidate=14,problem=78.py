
# Solution
# I'm using dynamic programming
# Let dp[i][j] be the number of ways to make a playlist for the first i songs with total length j
# Then, dp[i][j] = sum(dp[i - 1][j - k]) where k is the length of each song in the ith song's genre
# And, dp[0][0] = 1
# Also, dp[0][j] = 0 for all j > 0
# And, dp[i][j] = 0 for all j < 0

# This solution is correct but it TLEs.
# To optimize, we can improve the runtime complexity of the second loop by only iterating over minimum and maximum lengths of songs
# since the number of ways to make a playlist is 0 if the total length is less than the minimum length of all songs or more than the maximum length of all songs

# The optimized solution passes

import sys

# sys.stdin = open('in.txt', 'r')  # Comment this line for local development

n, T = map(int, input().split())
songs = []
min_len = sys.maxsize
max_len = 0
for i in range(n):
    t, g = map(int, input().split())
    min_len = min(min_len, t)
    max_len = max(max_len, t)
    songs.append((t, g))

MOD = 10 ** 9 + 7

dp = [[0] * (T + 1) for _ in range(n + 1)]

dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(min_len, T + 1):
        t, g = songs[i - 1]
        # add the number of ways to make a playlist for i - 1 songs with total length j - k
        # where k is the length of each song in the ith song's genre
        dp[i][j] = sum(dp[i - 1][j - k] for k in range(t, T + 1) if k % g == 0)
        dp[i][j] %= MOD

print(dp[n][T])