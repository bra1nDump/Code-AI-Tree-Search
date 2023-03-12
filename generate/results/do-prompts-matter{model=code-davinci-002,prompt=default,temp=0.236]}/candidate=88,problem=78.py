
# Solution

# The idea is to use dynamic programming.
# Let's define $dp[i][j]$ as the number of ways to play the first $i$ songs and the last song is of genre $j$.
# Then, we can iterate through all the songs and update the $dp$ array.
# The answer is the sum of all the values in the last row of the $dp$ array.

# Implementation

n, T = map(int, input().split())

t = []
g = []

for i in range(n):
    ti, gi = map(int, input().split())
    t.append(ti)
    g.append(gi)

dp = [[0 for i in range(4)] for j in range(n + 1)]

dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(1, 4):
        if g[i - 1] == j:
            for k in range(1, 4):
                if k != j:
                    dp[i][j] += dp[i - 1][k]
        else:
            dp[i][j] = dp[i - 1][j]

ans = 0

for i in range(1, 4):
    ans += dp[n][i]

print(ans)