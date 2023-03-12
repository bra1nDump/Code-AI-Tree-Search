
# In this problem, I used the DP approach to solve it.

import sys

# The input
n, T = map(int, sys.stdin.readline().split())

# The songs lengths and genres
songs = []
for i in range(n):
    songs.append(list(map(int, sys.stdin.readline().split())))

# The result
res = 0

# The DP matrix modulo 10^9+7
dp = [[0 for j in range(T+1)] for i in range(n)]

# The DP equation
for i in range(n):
    for j in range(T+1):
        if songs[i][0] == j:
            dp[i][j] = 1
        else:
            if i == 0:
                if j > songs[i][0]:
                    dp[i][j] = 1
            else:
                if j > songs[i][0]:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-songs[i][0]]) % (10**9+7)
                else:
                    dp[i][j] = dp[i-1][j]

# The final result
res = dp[n-1][T]

# The printing
print(res)